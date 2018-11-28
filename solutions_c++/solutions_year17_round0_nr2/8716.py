#include "cstdio"
#include "iostream"
#include "algorithm"
#include "string"
#include "cstring"
#include "queue"
#include "cmath"
#include "vector"
#include "map"
#include "stdlib.h"
#include "set"
#define mj
#define db double
#define ll long long
using  namespace std;
const int N=1e4+5;
const int mod=1e9+7;
const ll inf=1e16+10;
ll a[20];
char s[22];
int p;
void f(ll x)
{
    sprintf(s,"%lld",x);
    p=strlen(s);
    for(int i=0;i<p;i++){
        a[i]=s[i]-'0';
    }
}
int main()
{
    ll t,n;
    scanf("%lld",&t);
    for(ll i=1;i<=t;i++){
        scanf("%lld",&n);
        f(n);
        for(int j=0;j<100;j++){
            for(int k=0;k<p;k++){
                if(k+1<p&&a[k]>a[k+1])
                {
                    a[k]--;
                    for(int l=k+1;l<p;l++){
                        a[l]=9;
                    }
                }
            }
        }
//        sscanf(s,a,"%d");
        ll ans=0,d=1;
        for(int ii=p-1;ii>=0;ii--){
            ans+=d*a[ii];
            d*=10;
        }
        printf("Case #%d: %lld\n",i,ans);
    }
    return 0;
}