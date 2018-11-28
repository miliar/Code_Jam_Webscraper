#include<iostream>
#include<stdio.h>
#include <iomanip>
#include<fstream>
using namespace std;
#define ll long long
int main()
{
    ll t,l;
    ifstream input;
    input.open("A-large.in");
    ofstream output;
    output.open("codejam1.txt");
    input>>t;
    l=t;
    while (t--)
    {
        ll n,i;
        double d,max=0,ans;
        input>>d>>n;
        double k[n],p,s[n];
        for (i=0;i<n;i++)
        {
            input>>k[i]>>s[i];
            k[i]=d-k[i];
            p=k[i]/s[i];
            if (p>max)
            {
                max=p;
            }
       // cout<<max;
        }
        ans=d/max;
        output<<"Case #"<<l-t<<": ";
        output<<fixed<<setprecision(6)<<ans<<endl;
        //printf("%lf\n",ans);
    }
}
