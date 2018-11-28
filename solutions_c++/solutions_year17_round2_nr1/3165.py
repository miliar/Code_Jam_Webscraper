#include<bits/stdc++.h>
using namespace std;
long long int t,d,n,k,s;
double ans,mina;
int main()
{
    freopen("input.IN","r",stdin);
freopen("outxyz.txt","w",stdout);
cin>>t;
int j=1;
while(t--)
{ans=0;
    cin>>d>>n;
    mina=-1;
    for(int i=0;i<n;i++)
    {
        cin>>k>>s;
        ans=(double)(((double)(d-k))/(double)s);
        if(ans>mina)
            mina=ans;
    }
    ans=d/mina;
    printf("Case #%d: %.6lf\n",j,ans);

    j++;
}
return 0;
}
