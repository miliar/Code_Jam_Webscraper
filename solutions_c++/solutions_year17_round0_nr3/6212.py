#include <iostream>
#include <string>
#include <queue>

using namespace std;



int main()
{
    std::ios::sync_with_stdio(false);
    
    int t,T;
    cin >> T;
    for (t=0; t<T; t++)
    {
        int N,K;
        cin>>N>>K;
        priority_queue<int> pq;
        pq.push(N);
        int a1=0,a2=0;
        for (int i=0; i<K; i++)
        {
            int num = pq.top();
            pq.pop();
            //cout<<"Testing :: "<<num<<endl;
            num--;
            if(num == 0)
            {
                a1 = 0;
                a2 = 0;
            }
            else if(num == 1)
            {
                a1 = 1;
                a2 = 0;
                pq.push(1);
            }
            else if(num%2 == 0)
            {
                pq.push(num/2);
                pq.push(num/2);
                a1 = num/2;
                a2 = num/2;
            }
            else
            {
                pq.push(num/2);
                pq.push((num/2)+1);
                a1 = num/2 + 1;
                a2 = num/2;
            }
        }
        cout <<"Case #"<<t+1<<": "<< a1 <<' '<< a2 <<endl;
        
        
    }
    
    return 0;
}

