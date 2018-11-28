#pragma comment(linker, "/stack:640000000")
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <list>
#include <map>
//#include <unordered_map>
/// unordered map only when c++ 11 is ticked :p
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const double EPS = 1e-9;
const double PI=acos(-1.0);

#define    READ(f) 	     freopen(f, "r", stdin)
#define    WRITE(f)      freopen(f, "w", stdout)

#define    INF           999999999999999
#define    pii 	         pair<int, int>
#define    pdd 	         pair<double, double>
#define    pll 	         pair<long long int, long long int>
#define    ii	         long long int
#define    uii 	         unsigned long long int
#define    ui            unsigned int
#define    bitCheck(a,k) ((bool)(a&(1<<(k))))
#define    bitOff(a,k)   (a&(~(1<<(k))))
#define    bitOn(a,k)    (a|(1<<(k)))
#define    bitFlip(a,k)  (a^(1<<(k)))
#define    iseq(a,b)     (fabs(a-b)<EPS)

template< class T > inline T _abs(T n) { return ((n) < 0 ? -(n) : (n)); }
template< class T > inline T _max(T a, T b) { return (!((a)<(b))?(a):(b)); }
template< class T > inline T _min(T a, T b) { return (((a)<(b))?(a):(b)); }
template< class T > inline T _swap(T &a, T &b) { a=a^b;b=a^b;a=a^b;}
template< class T > inline T gcd(T a, T b) { return (b) == 0 ? (a) : gcd((b), ((a) % (b))); }
template< class T > inline T lcm(T a, T b) { return ((a) / gcd((a), (b)) * (b)); }


///******************DELETE****************

#ifdef rafiul41
     #define debug(args...) {cerr<<"Debug: "; dbg,args; cerr<<endl;}
#else
    #define debug(args...)  // Just strip off all debug tokens
#endif

struct debugger{
    template<typename T> debugger& operator , (const T& v){
        cerr<<v<<" ";
        return *this;
    }
}dbg;

int strToint(string x)
{
    stringstream ss(x);
    int i;
    ss>>i;
    return i; /// this int does not have any leading zeros !!!
}

///**************************************************

int n,m;

char grid[26][26];

bool check(char x,int r,int c1,int c2)
{
    if(r<0||r>=n) return 0;
    for(int i=c1;i<=c2;i++)
    {
        if(!(grid[r][i]=='?'||grid[r][i]==x)) return 0;
    }
    return 1;
}

bool check1(char x,int c,int r1,int r2)
{
    if(c<0||c>=m) return 0;
    for(int i=r1;i<=r2;i++)
    {
        if(!(grid[i][c]=='?'||grid[i][c]==x)) return 0;
    }
    return 1;
}

pii starts[26],endd[26];

bool ques_check()
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(grid[i][j]=='?')
                return 1;
        }
    }
    return 0;
}

int main()
{
#ifdef rafiul41

    READ("A-large.in");
    WRITE("out.txt");

#endif // rafiul41
    //ios_base::sync_with_stdio(false);cin.tie(NULL);
    int test;
    scanf("%d",&test);
    int cas=1;
    while(test--)
    {
        for(int i=0;i<26;i++)
        {
            starts[i].first=-1;starts[i].second=-1;
            endd[i].first=-1;endd[i].second=-1;
        }
        scanf("%d %d",&n,&m);
        for(int i=0;i<n;i++)
        {
            scanf("%s",grid[i]);
            for(int j=0;j<m;j++)
            {
                char now=grid[i][j];
                if(now=='?')
                {
                    continue;
                }
                starts[now-'A'].first=i;
                starts[now-'A'].second=j;
                endd[now-'A'].first=i;
                endd[now-'A'].second=j;
            }
        }
        while(ques_check())
        {
            for(int i=0;i<26;i++)
            {
                if(starts[i].first==-1) continue;
                /// upore
                int strt_row=starts[i].first-1;
                int l1=starts[i].second,l2=endd[i].second;
                while(check(i+'A',strt_row,l1,l2))
                {
                    for(int j=l1;j<=l2;j++)
                    {
                        grid[strt_row][j]=i+'A';
                    }
                    strt_row--;
                }
                starts[i].first=strt_row+1;
            }
            for(int i=0;i<26;i++)
            {
                if(starts[i].first==-1) continue;
                /// niche
                int strt_row=endd[i].first+1;
                int l1=starts[i].second,l2=endd[i].second;
                while(check(i+'A',strt_row,l1,l2))
                {
                    for(int j=l1;j<=l2;j++)
                    {
                        grid[strt_row][j]=i+'A';
                    }
                    strt_row++;
                }
                endd[i].first=strt_row-1;
            }
            for(int i=0;i<26;i++)
            {
                if(starts[i].first==-1) continue;
                /// dan e
                int start_col=endd[i].second+1;
                int l1=starts[i].first,l2=endd[i].first;
                while(check1(i+'A',start_col,l1,l2))
                {
                    for(int j=l1;j<=l2;j++)
                    {
                        grid[j][start_col]=i+'A';
                    }
                    start_col++;
                }
                endd[i].second=start_col-1;
            }
            for(int i=0;i<26;i++)
            {
                if(starts[i].first==-1) continue;
                /// left e
                int start_col=starts[i].second-1;
                int l1=starts[i].first,l2=endd[i].first;
                while(check1(i+'A',start_col,l1,l2))
                {
                    for(int j=l1;j<=l2;j++)
                    {
                        grid[j][start_col]=i+'A';
                    }
                    start_col--;
                }
                starts[i].second=start_col+1;
            }
            //debug(ques_check());
        }
        printf("Case #%d:\n",cas++);
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                printf("%c",grid[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
