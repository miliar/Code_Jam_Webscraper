#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
int t;
cin>>t;
int caseno =0;
while(t--)
{
    double k[1005],s[1003];
double n,d;
cin>>d>>n;
for(int i=0;i<n;i++)
{
    cin>>k[i]>>s[i];
}
double maxtime = 0.0;
for(int i=0;i<n;i++)
{
    double timee = (d-k[i])/s[i];
    if(timee>maxtime)
    {
        maxtime = timee;
    }
}
double ans = d/maxtime;
printf("Case #%d: %.6lf\n",++caseno,ans);
//Case #1: 101.000000
}

    return 0;
}
