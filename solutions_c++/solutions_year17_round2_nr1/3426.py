#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

typedef long long ll;
typedef long double ld;
#define S(a) scanf("%d",&a)
#define LS(a) scanf("%lld",&a)
#define D(a) scanf("%lf",&a)
#define LD(a) scanf("%lf",&a)
#define FOR(i,a,b) for(int i = a, i <= b;++i)
#define DOW(i,b,a) for(int i = b; i >= a;--i)
#define eb emplace_back

const ll INF = 1e17;
const ll MOD = 1e9 + 7;
ll power(ll base,ll expo,ll MOD)
{
    ll res = 1;
    while(expo > 0)
    {
        if(expo & 1) res = (res * base) % MOD;
        base = (base * base ) % MOD;
        expo>>= 1;

    }

    return res;




}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
  //  cout << t << "\n";
    for(int tc = 1; tc <= t; ++tc)
    {
      int N;
      double d;
      cin >> d >> N;
      double K ,s;
      double maxt = 0.0;
    //  cout << d << "\n";
      for(int i = 0 ; i < N;++i)
      {
          cin >> K >> s;

           maxt = max((d - K)/s,maxt);
          // cout << s << "\n";
      }

      printf("Case #%d: %.16lf\n",tc,d/maxt);


    }

    return 0;
}

