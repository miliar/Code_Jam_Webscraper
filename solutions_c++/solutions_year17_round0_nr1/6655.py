
#include<bits/stdc++.h>

using namespace std;

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(a) (int)(a.size())
#define ALL(a) a.begin(),a.end()
#define SET(a,b) memset(a,b,sizeof(a))

#define SI(n) scanf("%d",&n)
#define PI(n) printf("%d\n",n)
#define SL(n) scanf("%lld",&n)
#define PL(n) printf("%lld\n",n)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)

#define TRACE

#ifdef TRACE
#define TR(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
    cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
    const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define TR(...)
#endif

//FILE *fin = freopen("in","r",stdin);
//FILE *fout = freopen("out","w",stdout);
typedef long long int 	LL;
typedef long double 	LD;
typedef pair<int,int>   II;
typedef vector<int>     VI;
const int MOD = 1e9 + 7;
const int N = 1011;
char a[N];

int main() {
    int t; SI(t);
    int cas = 0;
    while(t--) {
        int k;
        scanf("%s %d",a, &k);
        int n = strlen(a);
        int operations = 0;
        for(int i = 0;i <= n - k; ++i) {
            if(a[i] == '+') continue;
            else {
                operations++;
                for(int j = i;j < i + k; ++j) {
                    if(a[j] == '+') a[j] = '-';
                    else a[j] = '+';
                }
            }
        }
        bool ok = 1;
        for(int i = 0;i < n; ++i) if(a[i] == '-') ok = 0;
        if(ok)
            printf("Case #%d: %d\n",cas + 1, operations);
        else 
            printf("Case #%d: IMPOSSIBLE\n",cas + 1);
        cas++;
    }

    return 0;
}
