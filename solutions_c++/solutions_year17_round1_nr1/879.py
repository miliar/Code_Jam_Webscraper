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
#define N 1002
#define M 400100
#define MP make_pair
#define Pi acos(-1.0)
//#pragma comment(linker,"/STACK:1024000000,1024000000")
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
#define ui unsigned long long
LL powmod(LL a,LL b) {LL res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
#define F(x) ((x)/3+((x)%3 == 1 ? 0 : tb))
#define G(x) ((x)<tb ? (x)*3+1 : ((x) - tb)*3+2)
#define lowbit(x) ((x)&(-x))
#define fi first
#define se second
#define pii pair<int,int>
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

ui read()
{
    ui x=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}

int n,m;
char s[N][N];
bool mark[N];

bool check(){
    for(int i = 1;i <= n; i++){
        if(!mark[i]) return 0;
    }
    return 1;
}

void solve()
{
    for(int i = 1;i <= n; i++){
        char full = 0;
        for(int j = 1;j <= m; j++){
            if(s[i][j] != '?') {
                full = s[i][j];
                break;
            }
        }
        if(full != 0){
            mark[i] = 1;
            for(int j = 1;j <= m; j++){
                if(s[i][j] == '?'){
                    s[i][j] = full;
                }else{
                    full = s[i][j];
                }
            }
        }
    }
    
    while(!check()){
        for(int i = 1;i < n; i++){
            if(mark[i] ^ mark[i+1])
            {
                if(mark[i])
                {
                    for(int j = 1;j <= m; j++){
                        s[i+1][j] = s[i][j];
                    }
                    mark[i+1] = 1;
                }else{
                    for(int j = 1;j <= m; j++)
                    {
                        s[i][j] = s[i+1][j];
                    }
                    mark[i] = 1;
                }
            }
        }
    }
}

int main(){
    
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, casi = 0;
    cin >> T;
    while(T--){
        
        cin >> n >> m;
        
        for(int i = 1;i <= n; i++)
        {
            for(int j = 1;j <= m; j++)
            {
                scanf(" %c",&s[i][j]);
            }
        }
        memset(mark, 0, sizeof mark );
        solve();
        
        printf("Case #%d:\n", ++casi);
        for(int i = 1;i<= n; i++)
        {
            for(int j = 1;j <= m; j++)
            {
                putchar(s[i][j]);
            }
            puts("");
        }
    }
    
    return 0;
}
