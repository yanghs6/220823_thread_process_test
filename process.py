import multiprocessing as mp
import time


def worker_process(queue, idx, s, e, std_print):
    print(f"[{idx:03d} process] start")
    
    list_iter = [i for i in range(s, e)]
    for i in list_iter:
        if i % std_print == 0:
            print(f"[{idx:03d} process] {s:9d} ~ {e-1:9d}, now: {i:9d}")
    print(f"[{idx:03d} process] End")
    
    return list_iter
    # queue.put(list_iter)
    

def exam_multiprocessing(queue, cnt_process, epoch, std_print):
    print(f"========== [ example {cnt_process:3d} processes start ] ==========")
    
    # pools = mp.Pool(cnt_process)
    
    # pools.starmap(worker_process, [(i, i*epoch, (i+1)*epoch, std_print) for i in range(cnt_process)])
    
    # pools.close()
    # pools.join()
    
    # exam_p = mp.Process(target=worker_process, args=(1, epoch, 2*epoch, std_print))
    # print(exam_p)
    # exam_p.start()
    
    exam_process = [mp.Process(name=f"{i+1} process", target=worker_process, args=(queue, i, i*epoch, (i+1)*epoch, std_print)) for i in range(cnt_process)]
    print(exam_process)
    for p in exam_process:
        p.start()
    for p in exam_process:
        p.join()
    print(exam_process[0].get())

    print(f"========== [ example {cnt_process:3d} processes end ] ==========")

if __name__ == "__main__":
    q = mp.Queue()
    proc = mp.current_process()
    # print()
    exam_multiprocessing(q, 2, 10**5, 10**4)

