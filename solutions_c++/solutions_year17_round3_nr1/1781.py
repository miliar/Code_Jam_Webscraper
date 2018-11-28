/*
 
I don't know when to give up
-Naruto uzumaki
 
*/

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <vector>
#include <string>

#define set(p) memset(p,-1,sizeof(p))
#define clr(p) memset(p,0,sizeof(p))
#define ll long long int
#define llu unsigned long long int
#define si(n)                   scanf("%d",&n)
#define sf(n)                   scanf("%lf",&n)
#define ss(n)                                   scanf("%s",n)
#define rep(i,a,n) for(i=(a);i<(n);i++)
#define pii pair<int,int>
#define pb(x) push_back(x)
#define v(x) vector<x>
using namespace std;

int gcd(int a,int b)
{
 int r, i;
  while(b!=0){
    r = a % b;
    a = b;
    b = r;
  }
  return a;
}


long long int power(long long int x,long long int y)
{
    long long int temp,ty,my;
    long long int mod;
    mod=1000000007;
    if( y == 0)
        return 1;
    temp = power(x, y/2);
    ty=(temp%mod)*(temp%mod);
    if (y%2 == 0)
        {

                return ty%mod;
        }
    else
        {
                my=(x%mod)*(ty%mod);
                return my%mod;
        }
}



long long int mini(long long int a,long long int b)
{
        return a<b?a:b;
}



struct node
{
       ll r;
       ll h;
};

struct node abhi[100010];

bool cmp(struct node x,struct node y)
{
    if(x.r==y.r){
        return x.h>y.h;
    } else{
        return x.r>y.r;
    }
}

char ss[100010];
ll ra[100100];
ll he[100100];
ll to[100100];
//int b[100000];
// vector< pair<int,int> > abhi;
int strr[1020];

double pie = 3.14159265358979323846264338328;

int main()
{
        freopen("/Users/abhishek.gupt/Documents/CP/GCJ2017/ab.in","r",stdin);
        freopen("/Users/abhishek.gupt/Documents/CP/GCJ2017/out_1.txt","w",stdout);
        ll t,m,i,n,c,w,j,k=0,p,kk=0;
        scanf("%lld",&t);
        while(t--)
        {

            //cin>>n>>k;
            scanf("%lld",&n);
            scanf("%lld",&k);

            vector<ll> vec;

            ll maxr=-1,max_ri=-1;
            ll maxh=-1,max_hi=-1;
            rep(i,0,n){
                //cin>>ra[i]>>he[i];

                scanf("%lld",&ra[i]);

                scanf("%lld",&he[i]);

                abhi[i].r=ra[i];
                abhi[i].h=he[i];
            }

             double sum=0.0;

             double ans = 0.0;

             sort(abhi,abhi+n,cmp);
             rep(i,0,n-k+1){

                // cout<<abhi[i].r<<" "<<abhi[i].h<<"\n";
                sum = 0.0;
                sum = sum + pie*abhi[i].r*abhi[i].r;
                sum = sum + 2.0*pie*abhi[i].r*abhi[i].h;
                ll ind = 0;

            
                rep(j,i+1,n){

                    to[ind++] = abhi[j].r*abhi[j].h;

                }

                sort(to,to+ind);
                ll inp=0;
                for(inp=ind-1;inp>ind-k;inp--){
                    sum = sum + 2.0*pie*(to[inp]);
                }

            

                ans = max(ans,sum);

                //printf("Case2 %0.6lf\n",ans);
             }

             

             // rep(i,0,k-1){

             //        sum = sum + 2.0*pie*(brr[i].pos)*(h[i].val);
             // }

             kk++;
            
            printf("Case #%lld: %0.6lf\n",kk,ans);

                //cout<<"Case #"<<kk<<": IMPOSSIBLE\n";
        }

        return 0;

}

