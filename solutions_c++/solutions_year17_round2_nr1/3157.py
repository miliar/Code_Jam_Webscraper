#include<iostream>
#include<cstdio>
#include<cmath>
#include <iomanip>
using namespace std;

int main()
{
    int T;
    freopen("A-large.in","r",stdin);
    freopen("aout.txt","w",stdout);
    cin>>T;
    for (int x=1;x<=T;x++)
    {
        long long d;
        int n;
        cin>>d>>n;
        long long k;
        int s;
        long double tm =0, tm1=0, ans = 0;
        for (int i=0;i<n;i++)
        {
            cin>>k>>s;
            tm = (d-k)/(double)s * pow(10,6);
            if (tm > tm1)
                tm1 = tm;
        }
        tm1 = tm1 / pow(10,6);
        ans = d/tm1;
        cout<<"Case #"<<x<<": ";
        cout<<fixed;
        cout<<setprecision(6);
        cout<<ans<<endl;
    }
}
