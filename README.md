<h1>Round Robin Scheduling Algorithm</h1>




This project is based on python programming language, to implement the Round Robin scheduling algoritm.

### `General Introduction:`

CPU scheduling is a complete process which allows one process to use the CPU resources while the execution of another process is paused due to unavailability of resources or based on priority of processes. The main aim of CPU scheduling is to make the system faster and more efficient.
There are certain algorithms which are used to schedule the execution of processes, which are either preemptive or non-preemptive. Preemptive scheduling is based on priority, where a low priority process will be put in the execution queue when a high priority process enters the into ready state. On the other hand, non-preemptive works on the First Come First Out (FIFO) principle. Once a process starts, it will not stop until it finished in allotted time.
Round Robin is one of the Preemptive process scheduling. Each process is provided with a fixed time to execute, which is known as quantum. Once a process is executed for a given period of time, it is paused, and other process is executed for the same period of time. When it has gone through all the process, it will come back to the first process. Same cycle will continue until all the processes achieve their execution time.

### `Analysis of the Algorithm:`

Round Robin Scheduling is one the mostly used CPU scheduling algorithm. It gives better result in comparison to other scheduling algorithms, but it also has some disadvantages, which we will discuss along with the pros below.
Advantages: Each process, in this scheduling algorithm, is provided with a fixed quantum time by the CPU, so all the processes have same priority. No process is left behind based on its priority. Secondly, each process gets a chance to run and CPU resources are shared between all process due to which no starvation occurs. Its implementation can be simple using FIFO queue system and processes with the same priority are handled better using this algorithm.
Disadvantages: Using this scheduling algorithm, low priority processes may execute first as this process doesn’t depends on priority level. Moreover, if time quantum is shorter than needed, then the number of times that CPU switches from one process to another increases, which will eventually decrease the efficiency of CPU. And, if quantum time is longer, then it will behave the same way as FIFO does. In addition, longer processes will have to wait more which will cause starvation.


