#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>
#include <fstream>

using namespace std;


#define LL long long
#define N 5000002
#define M 400100
#define MP make_pair
#define Pi acos(-1.0)
#pragma comment(linker,"/STACK:1024000000,1024000000")
#define ls (rt << 1)
#define rs (ls | 1)
#define md ((ll+rr)/2)
#define lson ll, md, ls
#define rson md+1, rr, rs
#define mod 1000000007
#define inf 0x3f3f3f3f
#define sqr(x) ((x)*(x))
#define eps 1e-6
#define uLL unsigned long long
#define ui unsigned int
LL powmod(LL a,LL b) {LL res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
#define F(x) ((x)/3+((x)%3 == 1 ? 0 : tb))
#define G(x) ((x)<tb ? (x)*3+1 : ((x) - tb)*3+2)
#define lowbit(x) ((x)&(-x))
#define fi first
#define se second
#define Pii pair<int,int>
#define pli pair<LL,int>
#define pb push_back
#define MP make_pair
LL gcd(LL x,LL y){
    while(y){
        LL t = x % y;
        x = y;
        y = t;
    }
    return x;
}

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }

int read()
{
    int x=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}

char s[1010];

int main()
{
    freopen("A-large.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    int casi = 0;
    T = read();
    while(T--)
    {
        scanf("%s",s);
        int n = read();
        int len = strlen(s);
        int ans = 0;
        for(int i = 0; i < len; i++)
        {
            if(s[i] == '-')
            {
                if(i + n > len)
                {
                    ans = -1;
                    break;
                }
                for(int j = i; j < i + n; j++)
                    if(s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                ans++;
            }
        }
        printf("Case #%d: ",++casi);
        if(ans == -1) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
    return 0;
}
