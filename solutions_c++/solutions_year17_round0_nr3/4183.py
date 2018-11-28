#include<iostream>
#include<cmath>
#include<queue>
using namespace std;
main()
{
    int t;
    cin>>t;
    for(int ii=1;ii<=t;ii++)
    {
        long long n,k;
        cin>>n>>k;
        long long df = 1<<((int)ceil(log2(1+k)));
        long long nf = df-(df-k)*2;
        long long a1 = (n-(k-df/2))/df;
        long long b1 = (n-k)/df;
        cout<<"Case #"<<ii<<": ";
        cout<<(n-(k-df/2))/df<<" "<<(n-k)/df<<endl;

        /*
        priority_queue<int> q;
        q.push(n);
        long long kk = k;
        while(!q.empty())
        {
            long long v = q.top();
            q.pop();
            kk-=1;
            a = v/2;b = (v-1)/2;
            if(kk==0)
                break;
            q.push(a);
            q.push(b);
        }
        //for(auto &aa: m)
            //cout<<aa.first.first<<" "<<aa.first.second<<" "<<aa.second<<endl;
        //cout<<"Case #"<<ii<<": ";
        if(a1!=a||b1!=b)
            cout<<"FUCK\n";
        //cout<<a<<" "<<b<<endl;
        */
    }
}
