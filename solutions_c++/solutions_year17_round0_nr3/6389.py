#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

static long long int testCase, N, K, num, MAX, MIN;
static priority_queue<long long int> Queue;

ifstream fin("C-small-2-attempt0.in");
ofstream fout("output.txt");

void queue_push(long long int num)
{
    if (num % 2 == 0)
    {
        Queue.push(num / 2);
        Queue.push((num / 2) - 1);
    }
    
    else
    {
        Queue.push((num - 1) / 2);
        Queue.push((num - 1) / 2);
    }
}

int main(void)
{
    fin >> testCase;
    
    for (int i = 0; i < testCase; i++)
    {
        fin >> N >> K;
        //cout << N << ", " << K << ": ";
        if (K > 1) queue_push(N);
        else Queue.push(N);
            
        K--;
        
        while (K > 1)
        {
            num = Queue.top();
            Queue.pop();
            
            if (num == 0) break;
            
            queue_push(num);
            
            K--;
        }
        
        num = Queue.top();
        //cout << num << endl;
        if (num % 2 == 0 && num != 0)
        {
            MAX = num / 2;
            MIN = (num / 2) - 1;
        }
        
        else
        {
            num--;
            MIN = MAX = num / 2;
        }
        
        fout << "Case #" << i + 1 << ": " << MAX << " " << MIN << endl;
        
        while (!Queue.empty()) Queue.pop();
    }
    
    return 0;
}
