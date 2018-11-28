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
int x,y,xx,yy,z,n,m,k,l,ans;
const double eps=1e-8;
int gcd(int a,int b) {if(a==0){return b;}else{return gcd(b%a,a);}}
double a[2][maxn][2];
char s[50],ss[50];
bool flag;
void dfs(int x,bool f,int la)
{
 if(x==m+1)
 {
     flag=true;
     return;
 }
    int be;
    if(f) be=9; else be=s[x]-'0';
    if(!f&&s[x]-'0'<la) return;
    for(int i=be;i>=la;i--)
    {
        if (!f&&i!=s[x]-'0') f=true;
        ss[x]=i+'0';
        dfs(x+1,f,i);
        if(flag) return;
    }
    return;
}
int main()
{
    read;
    write;
    int T,_;
    _=0;
    cin>>T;
    while(T--)
    {
      
        scanf("%s",s);
        m=strlen(s)-1;
        flag=false;
        dfs(0,false,1);
        if(flag==false)
        {
            m--;
            REP(i,0,m) ss[i]='9';
        }
        if(strcmp(s,"0")==0) {ss[0]='0'; m=0;}
        ss[++m]='\0';
       
        printf("Case #%d: %s\n",++_,ss);
        
    }
    
}
