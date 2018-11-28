
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
const int N = 100011;
vector<int> num;

int main() {
    int cs = 0; SI(cs);
    for(int i = 0;i < cs; ++i) {
        LL n; scanf("%lld",&n);
        num.clear();
        while(n) {
            num.PB(n%10);
            n /= 10;
        }
        reverse(ALL(num));
        bool ok = 0;
        int prev = 0;
        for(int i = 1;i < SZ(num); ++i) {
            if(num[i - 1] > num[i]) {
                num[prev]--;
                for(int j = prev + 1;j < SZ(num); ++j) num[j] = 9;
                break;
            }
            if(num[i - 1] < num[i]) prev = i;
        }
        printf("Case #%d: ",i + 1);
        for(int i = 0;i < SZ(num); ++i) {
            if(!ok and num[i] == 0) continue;
            ok = 1;
            printf("%d",num[i]);
        }
        printf("\n");
    }
    return 0;
}
