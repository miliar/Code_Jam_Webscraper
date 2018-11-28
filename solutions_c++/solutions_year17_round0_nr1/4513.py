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

#define    READ(f)       freopen(f, "r", stdin)
#define    WRITE(f)      freopen(f, "w", stdout)

#define    INF           999999999999999
#define    pii           pair<int, int>
#define    pdd           pair<double, double>
#define    pll           pair<long long int, long long int>
#define    ii            long long int
#define    uii           unsigned long long int
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

int main()
{
#ifdef rafiul41
//
    READ("in.txt");
    WRITE("out.txt");

#endif // rafiul41

    int test;
    scanf("%d",&test);
    int cas=1;
    while(test--)
    {
        string s;
        cin>>s;
        int k;
        scanf("%d",&k);
        int cnt=0;
        int f=1;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='-')
            {
                cnt++;
                //debug(i,i+k)
                if(i+k>s.length())
                {
                    f=0;
                    break;
                }
                for(int j=i;j<i+k;j++)
                {
                    if(s[j]=='-') s[j]='+';
                    else s[j]='-';
                }
               // cout<<s<<endl;
            }
        }
        printf("Case #%d: ",cas++);
        if(f==0)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",cnt);
    }
    return 0;
}
