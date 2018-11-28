/** source code by coolreshab **/

#include<bits/stdc++.h>
using namespace std;

priority_queue<long long>LOL;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,dragon=1;
    long long N,K,i,a,b;
    cin>>T;
    while(T-->0)
    {
        cin>>N>>K;
        LOL.push(N);
        for(i=0;i<K;++i)
        {
            if(LOL.top()&1)
            {
                a=LOL.top()/2;
                b=LOL.top()/2;
            }
            else
            {
                a=LOL.top()/2;
                b=a-1;
            }
            LOL.push(a);
            LOL.push(b);
            LOL.pop();
        }
        while(!LOL.empty())
            LOL.pop();
        cout<<"Case #"<<dragon<<": "<<a<<" "<<b<<endl;
        dragon+=1;
    }
    return 0;
}
