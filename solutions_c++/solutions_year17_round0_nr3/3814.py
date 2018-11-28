#include<bits/stdc++.h>
using namespace std;

main()
{
    freopen("input-3.txt","r",stdin);
    freopen("output-3.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        long long n,k;
        cin>>n>>k;
        long long p=k,countt=0;
        if(p==1)
        {
            cout<<(n/2)<<" "<<(n-1)/2<<endl;
            continue;
        }

        while(p!=1)
        {
            p/=2;
            countt++;
        }

        long long r = pow(2,countt+1);
        n = n - r +1;
        if(n <= 0)
        {
            cout<<0<<" "<<0<<endl;
            continue;
        }
        long long extra = n%(r/2);
        long long extra2 = n%r;
        long long minn = n/r;
        if(k<(r/2)+extra && extra2>extra)
        {
            cout<<minn+1<<" "<<minn+1<<endl;
        }
        else if(k>=(r/2)+extra && extra2==extra)
        {
            cout<<minn<<" "<<minn<<endl;
        }
        else
        {
            cout<<minn+1<<" "<<minn<<endl;
        }
    }
}
