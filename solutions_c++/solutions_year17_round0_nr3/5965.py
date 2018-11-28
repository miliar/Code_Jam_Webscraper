#include <bits/stdc++.h>

using namespace std;




int main()
{
 
    int t;
    
    cin >> t;
    
    int count = 0;
    while(t--)
    {
        long long a,b;
        cin >> a >> b;
        priority_queue<long long > cola ;
        cola.push(a);    
        long test =0;
        count ++;
        int c =0;
        while(!cola.empty())
        {c++;
            int q = cola.top();
           
            cola.pop();
            if(q<1)
            continue;
            if(c==b)
            {
            test=q;
            break;
            }
            if(q%2!=0)
            {
                if(q/2)
                {
                cola.push(q/2);
                cola.push(q/2);
                }
            }
            else
            {
                if(q/2)
                cola.push(q/2);
                if(q/2-1)
                cola.push(q/2-1);
                
            }
        }
        
        
      
        a=test;
       printf("Case #%d: %lld %lld\n",count,a/2,max(0LL,a%2==0?(a/2-1):a/2));      
    }
    
    return 0;
}