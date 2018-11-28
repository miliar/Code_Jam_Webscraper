#include <bits/stdc++.h>
//#define DEBUG
#define si(n) cin>>n
#define sl(n) cin>>n
#define sf(n) scanf("%f",&n)
#define pn(n) printf("%d\n",n)
#define ps(n) printf("%d ",n)
#define pln(n) cout<<n<<endl
#define pnl() printf("\n")
#define pls(n) cout<<n<<" "
#define pl(n) cout<<n
#define FOR(i,j,n) for(i=j;i<=n;i++)
#define FORR(i,j,n) for(i=j;i>=n;i--)
#define SORT(n) std::sort(n.begin(),n.end())
#define FILL(n,a) std::fill(n.begin(),n.end(),a)
#define ALL(n) n.begin(),n.end()
#define rsz resize
#define pb push_back
#define MAXINT std::numeric_limits<int>::max()
#define MININT std::numeric_limits<int>::min()
#define gc getchar_unlocked
#define pc putchar_unlocked
#define iOS std::ios_base::sync_with_stdio(false)
#define endl "\n"
#define INF 1000000000000000005LL
#define INFI 1009990000
#ifdef DEBUG
    #define debugHello() cout << "Hello" << endl
#else
    #define debugHello()
#endif
#ifdef DEBUG
    #define debug(x) cout << #x << " = " << x << endl
#else
    #define debug(x)
#endif
using namespace std;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<bool> vb;
typedef vector<vector<int> > vvi;
typedef vector<vector<ll> > vvl;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll; const ld eps = 0.0000001L;
/**************** TEMPLATE ENDS HERE *************************/
const int MAXN = 512;
pair< pii, char > arr[MAXN];
vector<int> cg, jg;
int getCnt(int rem, vector<int> l) {
    int ret = 0;
    for(auto it:l) {
        rem -= (it<<1);
        ret+=2;
        if (rem<=0) break;
    }
    return ret;
}
int main() {
    int tt,t,i,aw,Tc,Tj,ac,aj,z,ans,rem;
    si(t);
    FOR(tt,1,t) {
        aw = 0;
        Tc=0;Tj=0;
        cg.clear();
        jg.clear();
        si(ac);si(aj);
        z=0;
        FOR(i,0,ac-1) {
           si(arr[z].first.first); 
           si(arr[z].first.second); 
           arr[z].second = 'J';
           Tj+=arr[z].first.second-arr[z].first.first;
           z++;
        }
        FOR(i,0,aj-1) {
           si(arr[z].first.first); 
           si(arr[z].first.second); 
           arr[z].second = 'C';
           Tc+=arr[z].first.second-arr[z].first.first;
           z++;
        }
        sort(arr, arr+z);
        /*
        FOR(i,0,z-1) {
            cout<<arr[i].second<<":\n";            
            debug(arr[i].first.first);
            debug(arr[i].first.second);
        }
        */
        ans = 0;
        FOR(i,0,z-2) {
            if (arr[i].second != arr[i+1].second) {
                aw+=(arr[i+1].first.first - arr[i].first.second);
                ans++;
            } else if (arr[i].second == 'C') {
                rem = arr[i+1].first.first - arr[i].first.second;
                if (rem > 0) {
                    cg.push_back(rem);
                    Tc+= rem;
                }
            } else {
                rem = arr[i+1].first.first - arr[i].first.second;
                if (rem > 0) {
                    jg.push_back(rem);
                    Tj+=rem;
                }
            }
        }
        if (arr[z-1].second != arr[0].second) {
            aw+=((arr[0].first.first + 1440) - arr[z-1].first.second);
            ans++;
        } else if (arr[z-1].second == 'C') {
            rem = ((arr[0].first.first + 1440) - arr[z-1].first.second);
            if (rem > 0) {
                cg.push_back(rem);
                Tc+= rem;
            }
        } else {
            rem = ((arr[0].first.first +1440)- arr[z-1].first.second);
            if (rem > 0) {
                jg.push_back(rem);
                Tj+= rem;
            }
        }
        /*
        debug(Tc);debug(Tj);debug(aw);
        for(auto it : jg) {
            cout<<it << " " ;
        }
        cout<<endl;
        */
        sort(jg.begin(), jg.end());
        reverse(jg.begin(), jg.end());
        sort(cg.begin(), cg.end());
        reverse(cg.begin(), cg.end());
        if (Tc < Tj) {
            if ((aw + Tc) < Tj) {
                rem = Tj - (aw + Tc);
                ans += getCnt(rem, jg);
                debug(ans);
            }
        } else if (Tj < Tc) {
            if ((aw + Tj) < Tc) {
                rem = Tc - (aw + Tj);
                ans += getCnt(rem, cg);
            }
        }
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
    return 0;
}
