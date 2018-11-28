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

int a[1006],s[1006];
int flips(int M, int k)
{
    for(int i=0;i<M;i++)s[i]=0;
    int sum=0,ans=0;

    for(int i=0;i<M;i++)
    {
        s[i] = ((a[i]+sum)%2) != 1;
        sum+= s[i];
        if(i >= k-1)
        {
            sum-=s[i-k+1]; ///the leftmost of this K subsequence
        }
        ans+=s[i];
        if(i > M-k && s[i] == 1)
        {
            return -1;
        }
    }
    return ans;
}
int main()
{
    rfile("ingcg.txt");
    wfile("outgcg.txt");
    int t;
    ri(t);
    for(int tc=1;tc<=t;tc++)
    {
        string s;
        int k;
        rtok(&s);
        ri(k);
        int ln=s.length();
        for(int i=0; i < ln;i++)
        {
          if(s[i]=='+')a[i]=1;
          else a[i]=0;
        }
        int res=flips(ln,k);
        if(res >= 0)
        {
            printf("Case #%d: %d\n",tc,res);
        }
        else{
            printf("Case #%d: IMPOSSIBLE\n",tc);
        }
    }
}
