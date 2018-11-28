typedef long long ll;
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <utility>
#define pb push_back
#define mp make_pair
#define pll pair<ll,ll> 
#define plll pair<ll,pair<ll,ll> >

using namespace std;
double a[1007];
int main()
{
    ll t,n,k,w=1,i,pos,flag=0,j;
    double u,p,res,sum,val;
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld %lld",&n,&k);
        scanf("%lf",&u);
        for(i=0;i<n;i++)
        scanf("%lf",&a[i]);
        sort(a,a+n);
      //  cout<<a[3]<<endl;
        for(i=n-1;i>=0;i--)
        {
            sum=0;
            flag=0;
            for(j=i-1;j>=0;j--)
            {
                sum+=a[i]-a[j];
                if(sum>u)
                {
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                pos=i;
                res=sum;
                break;
            }
        }
      //  cout<<pos<<endl;
        for(i=0;i<pos;i++)
        a[i]=a[pos];
        u-=res;
        val=u/(pos+1);
        for(i=0;i<=pos;i++)
        a[i]+=val;
       
        p=1;
        for(i=0;i<n;i++)
        p*=a[i];
        printf("Case #%lld: %.6lf\n",w++,p);
    }
	return 0;
}