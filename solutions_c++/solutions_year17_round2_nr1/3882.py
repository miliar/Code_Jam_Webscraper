#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
	cin.tie(NULL);
	freopen("A-large (2).in","r",stdin);
	freopen("out.txt","w",stdout);
	ll t,n,a,p,q;
	cin>>t;
	for(int test=1;test<=t;test++)
    {
        cin>>a>>n;
        long double mp=LLONG_MAX,mq=LLONG_MAX,res=LLONG_MAX;
        for(int i=0;i<n;i++)
        {
            cin>>p>>q;
            mp=p;mq=q;
            long double temp=a-mp;
            long double r=(long double)temp/(long double)mq;
            long double re=(long double)a/r;
            if(re<res)
                res=re;
        }
        cout<<"Case #"<<test<<": ";
        printf("%lf\n",res);
    }
	return 0;
}
