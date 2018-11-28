#include <bits/stdc++.h>
using namespace std;

#define LL long long
#define ULL unsigned long long
#define INF LLONG_MAX
#define LD long double
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MOD 1000000007LL
#define ABS(x) ((x)<0?-(x):(x))
#define line() printf("\n");
#define spc() printf(" ");
#define f(i, a, b) for(i = a; i < b; ++i)
#define fe(i, a, b) for(i = a; i <= b; ++i)
#define rf(i, a, b) for(i = a; i > b; --i)
#define rfe(i, a, b) for(i = a; i >= b; --i)
#define pb(x) push_back(x)
#define pf(x) push_front(x)
#define make_pair mp
#define DB(x) cout<<"\n"<<#x<<" = "<<(x)<<"\n";
#define CL(a, b) memset(a, b, sizeof(a));
#define F first
#define S second
#define boost ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
typedef pair<LL, LL> pll;
typedef vector<LL> vll;
typedef vector<pll> vpll;
const double PI = 3.14159265358979323846264338327950288419716939937510582097494459230;
ULL gcd(ULL a,ULL b){if(a==0)return b;if(b==0)return a;if(a==1||b==1)return 1;
if(a==b)return a;if(a>b)return gcd(b,a%b);else return gcd(a,b%a);}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out-large.txt", "w", stdout);
    //freopen("log.txt", "w", stderr);
    //boost;
    LL T, t, K, n, i, j, ans;
    string S;
    cin>>T;
    t = 1;
    while(T--){
        ans = 0;
        cin>>S>>K;
        n = S.length();
        fe(i, 0, (n - K))
            if(S[i] == '-'){
                ans++;
                f(j, i, i + K)
                    if(S[j] == '+')
                        S[j] = '-';
                    else
                        S[j] = '+';
            }
        f(i, i, n)
            if(S[i] == '-'){
                ans = -1;
                break;
            }
        cout<<"Case #"<<t++<<": ";
        if(ans != -1)
            cout<<ans<<endl;
        else
            cout<<"IMPOSSIBLE\n";
    }
    return 0;
}
