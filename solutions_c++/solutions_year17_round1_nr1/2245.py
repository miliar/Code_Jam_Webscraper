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
int main()
{
    rfile("ingcg.txt");
    wfile("outgcg.txt");
    int t;
    ri(t);
    for(int tc = 1; tc <= t; tc++)
    {
        bool ck[50][50];
        int r,c;
        ri(r), ri(c);
        set<char> dict;
        string arr[r+1];
//        printf("INPUT FOR CASE %d:\n", tc);
        for(int i = 0; i < r; i++)
        {
            rs(&arr[i]);
//            puts(arr[i].c_str());
        }
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(arr[i][j]=='?')
                {
                    ck[i][j]=1;
                }
                else{
                    ck[i][j]=0;
                }
            }
        }
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(arr[i][j] != '?' and ck[i][j] != 1)
                {
                    char cur=arr[i][j];
                    arr[i][j]='?';
                    int rh=i;
                    for(int r2=i+1; r2 < r; r2++)
                    {
                        if(arr[r2][j]=='?')rh++;
                        else {
                            break;
                        }
                    }
                    int rl=i;
                    for(int r2=i-1; r2 >= 0; r2--)
                    {
                        if(arr[r2][j]=='?')rl--;
                        else {
                            break;
                        }
                    }
                    int mini=28;
                    for(int r2=rl; r2 <= rh; r2++)
                    {
                        int ctrr=0;
                        for(int c2=j; c2< c; c2++)
                        {
                            if(arr[r2][c2]=='?')ctrr++;
                            else break;
                        }
                        mini=min(mini,ctrr);
                    }
                    for(int r2=rl; r2<=rh;r2++)
                    {
                        for(int c2=j,ctrr=1; ctrr<=mini; ctrr++,c2++)
                        {
                            arr[r2][c2]=cur;
                        }
                    }
                }

            }
        }
        for(int i=0;i<r;i++)
        {
            for(int j=c-1;j>=0;j--)
            {
                if(arr[i][j] != '?' and ck[i][j] != 1)
                {
                    char cur=arr[i][j];
                    arr[i][j]='?';
                    int rh=i;
                    for(int r2=i+1; r2 < r; r2++)
                    {
                        if(arr[r2][j]=='?')rh++;
                        else {
                            break;
                        }
                    }
                    int rl=i;
                    for(int r2=i-1; r2 >= 0; r2--)
                    {
                        if(arr[r2][j]=='?')rl--;
                        else {
                            break;
                        }
                    }
                    int mini=28;
                    for(int r2=rl; r2 <= rh; r2++)
                    {
                        int ctrr=0;
                        for(int c2=j; c2>=0; c2--)
                        {
                            if(arr[r2][c2]=='?')ctrr++;
                            else break;
                        }
                        mini=min(mini,ctrr);
                    }
                    for(int r2=rl; r2<=rh;r2++)
                    {
                        for(int c2=j,ctrr=1; ctrr<=mini; ctrr++,c2--)
                        {
                            arr[r2][c2]=cur;
                        }
                    }
                }

            }
        }
        for(int i=0;i<r;i++)
        {
            for(int j=c-1;j>=0;j--)
            {
                if(arr[i][j] != '?')
                {
                    for(int c2=j-1; c2 >=0; c2--)
                    {
                        if(arr[i][c2] == '?')
                        {
                            arr[i][c2]=arr[i][j];
                        }
                        else break;
                    }
                }

            }
        }

        printf("Case #%d:\n", tc);
        for(int i=0;i<r;i++)
        {
         puts(arr[i].c_str());
        }
    }

}
