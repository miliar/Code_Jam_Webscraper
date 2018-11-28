//
//  main.cpp
//  ac
//
//  Created by 胡天翼 on 2017/2/21.
//  Copyright © 2017年 胡天翼. All rights reserved.
//
#include <cstring>
#include <iostream>
#include <set>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <cstdio>
#include <bitset>
#define read freopen("in.txt","r",stdin)
#define write freopen("out.txt","w",stdout)
#define maxlongint 2147483647
typedef  long long LL;
typedef  unsigned long long ULL;
#pragma comment(linker, "/STACK:102400000,102400000")
#define fori for(int i=1;i<=n;i++)
#define forj for(int j=1;j<=n;j++)
#define fork for(int k=1;k<=n;k++)
#define FOR(i,n) for(int i=1;i<=n;i++)
#define REP(i,a,b) for(int i=a;i<=b;i++)
#define DREP(i,a,b) for(int i=a;i>=b;i--)
#define DOWN(i,n) for(int i=n;i>=1;i--)
#define enter cout<<endl;
#define in push_back
#define out pop_back
#define sqr(x) ((x)*(x))
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define offcin ios::sync_with_stdio(false)
#define s(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n)
#define sd(x,y) scanf("%d%d",&x,&y)
#define sch(s) scanf("%s",s)
#define fillfalse(v) memset(v,false,sizeof(v))
#define filltrue(v) memset(v,true,sizeof(v))
#define f0(a)    memset(a,0,sizeof(a))
#define Fillplus(a)    memset(a,-1,sizeof(a))
#define lowbit(x) x&(-x)
using namespace std;
const int maxn = 5e3+5;
const int mod=1e9+7;
LL x,y,xx,yy,z,n,m,k,ans1,ans2;
const double eps=1e-8;
int gcd(int a,int b) {if(a==0){return b;}else{return gcd(b%a,a);}}
string s;
int a[1000];
int l[1000];
int r[1000];
int main()
{
  read;
  write;
    int T,_;
    _=0;
    cin>>T;
    while(T--)
    {
        cin>>n>>m;
        f0(a);
        a[0]=1;
        a[n+1]=1;
        FOR(i,m)
        {
            ans2=0;
            ans1=0;
            int le=0;
            fori if(!a[i]) l[i]=i-le-1; else le=i;
            int re=n+1;
            for(int i=n;i>=1;i--) if(!a[i]) r[i]=re-i-1; else re=i;
            fori if(!a[i]&&((min(l[i],r[i])>ans2)||(min(l[i],r[i])==ans2&&max(l[i],r[i])>ans1)))
            {
                ans1=max(l[i],r[i]);
                ans2=min(l[i],r[i]);
                k=i;
            }
            a[k]=1;
        }
        printf("Case #%d: %lld %lld\n",++_,ans1,ans2);
    }
    
}
