#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T,i,t=1,k;
    cin>>T;
    while(T--)
    {
        long long int N,K,temp,a,b;
        cin>>N>>K;
        priority_queue<long long int> q;
        q.push(N);
        for(i=1;i<K;i++)
           {
            temp=q.top();
            q.pop();
            q.push(temp/2);
            if(temp%2==1)
            {
                q.push(temp/2);
            }
            else
                q.push((temp/2)-1);
           }
           temp=q.top();
           if(temp==1)
                a=b=0;
           else if(temp%2)
                a=b=(temp/2);
           else
           {
               a=(temp/2)-1;
               b=temp/2;
           }

        cout<<"Case #"<<t<<": "<<b<<" "<<a<<endl;
            t++;
    }

    return 0;
}
