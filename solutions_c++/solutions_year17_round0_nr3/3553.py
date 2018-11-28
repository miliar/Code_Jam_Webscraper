///Fahim Ahmed :: Dhaka Residential Model College
#pragma comment(linker, "/STACK:16777216") ///Increases Stack size
#include <bits/stdc++.h>
using namespace std;
#define li long long int
///I/O functions begin
#define rfile(a) freopen(a, "r", stdin)
#define wfile(a) freopen(a, "w", stdout)
#define rd(a) scanf("%lf", &a)
#define lb printf("\n")
#define mp make_pair
#define pb push_back
#define ru(n) scanf("%llu",&n)
#define ruuu(m,n,o) scanf("%llu %llu %llu", &m, &n, &o)
#define ui unsigned long long int
#define rl(n) scanf("%lld", &n)
#define rll(m,n) scanf("%lld %lld", &m, &n)
#define rlll(m,n,o) scanf("%lld %lld %lld", &m, &n, &o)
#define ri(n) scanf("%d", &n)
#define rc(c) scanf("%c", &c)

bool rs(string *s) //for line input
{
    char buf[200001];
    again:
    if(gets(buf))
    {
        if(buf[0]=='\n' || buf[0] == 0)goto again;
        *s=string(buf);
        return true;
    }
    else return false;
}
bool rtok(string *s) //for input of strings without space
{
    char buf[200001];
    again:
    if(scanf("%s", buf) != EOF)
    {
        if(buf[0]=='\n' || buf[0] == 0 || buf[0]==' ')goto again;
        *s=string(buf);
        return true;
    }
    else return false;
}
///for double,float use scanf
///for printing decimal use wl
///for printing string use puts
///for printing double use printf
///for newline, just type lb;
///I/O functions END
#define pi acos(-1.00)
#define Pr printf
#define For(i,a,b) for(int i = a; i < b; i++)
#define MOD 1000003
#define eps 1e-9

template <typename t1> t1 gcd(t1 a, t1 b) {while(b != 0 ){a=a%b;a = a^b;b = b^a;a = a^b;}return a;}
template <typename t1> t1 lcm(t1 a, t1 b) { return a * (b / gcd(a, b)); }
template <typename t1> bool check (t1 i, t1 k){return i&((t1)1<<k);}
template <typename t1> t1 On(t1 i, t1 k) { return i|((t1)1 << k);}
template <typename t1> t1 Off(t1 i, t1 k) {return (i-((check(i,k))<<k) );}


struct slot{
    li first,second, d;
    slot(){}
    slot(li aa, li bb)
    {
        first=aa,second=bb;
        d=second-first;
    }
    bool operator < (const slot& p) const
    {
        if(d < p.d)return true;
        else if(d > p.d)return false;
        else if(d==p.d)
        {
            return first>p.first;
        }
    }
    void print()
    {
        cout<<first<<" "<<second<<endl;
    }

};

li used[61];
li boundary[61];
priority_queue<slot> Q;
int main()
{
    rfile("ingcg.txt");
    wfile("outgcg.txt");
//    boundary[0]=1;
//    li mul=1;
//    for(int i=1; i <=60; i++)
//    {
//        mul*=2;
//        boundary[i]=boundary[i-1]+mul;
////        cout<<i<<" "<<boundary[i]<<endl;
//    }
    int t;
    ri(t);
    for(int tc=1; tc <= t; tc++)
    {
        li n,k;
        rll(n,k);
        while(Q.empty()==false)
        {
            Q.pop();
        }
        Q.push(slot(1,n));
        for(li i = 1; i <= k; i++)
        {
            slot p = Q.top();
            Q.pop();
            li mid=(p.first+p.second)/2;
            li ls,rs;
            if(mid==p.first)
            {
                ls=0;
            }
            else{
                ls = mid-p.first;
            }

            if(mid==p.second)
            {
                rs=0;
            }
            else{
                rs=p.second-mid;
            }
            li mini=min((ls), (rs));
            li maxi=max((ls), (rs));

            if(mid != p.first)Q.push(slot(p.first,mid-1));
            if(mid != p.second)Q.push(slot(mid+1,p.second));
//            cout<<maxi<<" "<<mini<<" "<<mid<<endl;
            if(i==k)
            {
                printf("Case #%d: %lld %lld\n",tc, maxi, mini);
            }
        }
    }

}
