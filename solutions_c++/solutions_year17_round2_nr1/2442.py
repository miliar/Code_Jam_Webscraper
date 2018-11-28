#include <bits/stdc++.h>
//file stream
#include <stdio.h>
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<string>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<sstream>
#include <set>

using namespace std;
#define output freopen("output.txt","w",stdout)
#define input freopen("input.txt","r",stdin)
#define inputfile(x) freopen(x,"r",stdin)
//functions
#define pb(x)  push_back(x)
#define pf  printf
#define sc scanf
#define maxe max_element
#define mine min_element


#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
// pair
#define xx first
#define yy second
#define mp(x,y) make_pair(x,y)
//inputs 1 var
#define si1(n) sc("%d",&n)
#define su1(n) sc("%u",&n)
#define sl1(n) sc("%lld",&n)
#define slu1(n) sc("%llu",&n)
#define sd1(n) sc("%lf",&n)
#define ss1(n) sc("%s",n)
//inputs 2 var
#define si2(n,m) sc("%d %d",&n,&m)
#define su2(n,m) sc("%u %u",&n,&m)
#define sl2(n,m) sc("%lld %lld",&n,&m)
#define slu2(n,m) sc("%llu %llu",&n,&m)
#define sd2(n,m) sc("%lf %lf",&n,&m)
//inputs 3 var
#define si3(n,m,l) sc("%d %d %d",&n,&m,&l)
#define su3(n,m,l) sc("%u %u %u",&n,&m,&l)
#define sl3(n,m,l) sc("%lld %lld %lld",&n,&m,&l)
#define slu3(n,m,l) sc("%llu %llu %llu",&n,&m,&l)
#define sd3(n,m,l) sc("%lf %lf %lf",&n,&m,&l)

//output 1 var
#define pi1(n) pf("%d",n)
#define pu1(n) pf("%u",n)
#define pl1(n) pf("%lld",n)
#define plu1(n) pf("%llu",n)
#define pd1(n,pre) pf("%.*f",pre,n)
#define ps1(n) pf("%s",n)
//output 2 var
#define pi2(n,m) pf("%d %d",n,m)
#define pu2(n,m) pf("%u %u",n,m)
#define pl2(n,m) pf("%lld %lld",n,m)
#define plu2(n,m) pf("%llu %llu",n,m)
#define pd2(n,m,pre) pf("%.*f %.*f",pre,n,pre,m)
//inputs 3 var less important
#define pi3(n,m,l) pf("%d %d %d",n,m,l)
#define pu3(n,m,l) pf("%u %u %u",n,m,l)
#define pl3(n,m,l) pf("%lld %lld %lld",n,m,l)
#define plu3(n,m,l) pf("%llu %llu %llu",n,m,l)
//output misc
#define nline() putchar(10)
#define space() putchar(' ')
#define pch(c) putchar(c)
#define tcase(i) pf("Case #%d:",i)
#define dbg()   pf("-----------")
//loop
#define fr0(i,n) for(i=0;i<n;i++)
#define fr1(i,n) for(i=1;i<=n;i++)
#define fri(i,ini,limit,inc) for(i=ini;i<=limit;i+=inc)
#define frd(i,ini,limit,dec) for(i=ini;i>=limit;i-=dec)
//to compile in codeblocks , c++11 flag must be off
//additional, only work if compiled with gcc compiler
#define frf(c, it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define frr(c, it) for(typeof((c).rbegin()) it = (c).rbegin(); it != (c).rend(); it++)
//memory reset
#define set0(x) memset(x,0,sizeof x)
#define setn1(x) memset(x,-1,sizeof x)
#define setinf(x) memset(x,125,sizeof x)
//misc
#define SZ(v)   ((int) (v).size())
#define all(v)  (v).begin(), (v).end()
//bit operation single variable
#define On(x,i)  (x|=(1<<(i)))
#define Off(x,i) (x&= ~(1<<(i)))
#define isOn(x,i) (x&(1<<(i)))
#define Toggle(x,i) (x^=(1<<(i)))
#define tmod(x,i)  (x&(~(-1<<i)))
//bit operation array
//data type
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<double,double> pdd;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;

//constant
const double EPS = 1e-9;

int i,j,m,n,a,b,c,tc,o,d;
double k[2000],s[2000],tt;
main()
{
    input;
    output;

    si1(tc);
    while(tc--)
    {
        si2(d,n);
        fr0(i,n)sd2(k[i],s[i]);

        tt=-1.0;
        fr0(i,n)
        {
            tt=max(tt,(d-k[i])/s[i]);
        }
        tcase(++o);space();
        pd1(d/tt,7);nline();
    }

    return 0;
}
