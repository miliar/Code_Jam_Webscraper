#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for (int ii=1; ii<=t; ii++)
    {
        long long n, k;
        cin>>n>>k;

        int cnt=0;
        for (int i=k; i; i/=2)
            cnt++;

        long long x=1ll<<(cnt-1);
        long long a=(n+1)/x;
        long long c2=(n+1)%x;
        long long c1=x-c2;
        long long lim=x+c2;

        long long res=(k<lim ? a+1 : a );
        cout<<"Case #"<<ii<<": "<<(res+1)/2-1<<" "<<res/2-1<<endl;
    }
}
