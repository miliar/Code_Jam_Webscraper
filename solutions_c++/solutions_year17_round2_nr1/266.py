#include <bits/stdc++.h>

using namespace std;

long long n,d,arr[2][1009];

bool check(long double x)
{
    for(int f=0;f<n;f++)
    {
        long double temp=1.0*arr[0][f]*x/(x-arr[1][f]);
        if(x>arr[1][f]&&temp<d)
            return 0;
    }
    return 1;
}

long double bs(long double a,long double b,int c)
{
    long double mid=(a+b)/2;
    if(!c)
        return mid;
    if(check(mid))
        return bs(mid,b,c-1);
    return bs(a,mid,c-1);
}

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int T;
    cin>>T;
    for(int tc=1;tc<=T;tc++){
        cin>>d>>n;
        for(int f=0;f<n;f++)
            cin>>arr[0][f]>>arr[1][f];
        cout<<"Case #"<<tc<<": ";
        cout<<setprecision(6)<<fixed<<bs(0,1e15,100)<<endl;
    }
}
