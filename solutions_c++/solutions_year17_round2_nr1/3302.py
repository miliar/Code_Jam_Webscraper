#include <bits/stdc++.h>

#define pb push_back
#define all(a) a.begin(),a.end()
#define allr(a) a.rbegin(),a.rend()
#define fr first
#define se second
#define mp make_pair
#define sz(a) ll((a).size())
#define memo(a,b) memset(a,b,sizeof(a))
#define MAX 100001
#define INF 1e18+1
#define EPS 0.000000001

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pll;
typedef vector<ll> vll;
typedef vector<pll> vpll;

double k[1001],s[1001],ans,d;
int t,n;

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(0);cout.tie(0);
  cout.precision(10);
  
  cin >> t;

  for(int id = 1;id <= t;++id){

    cin >> d >> n;

    for(int i = 0;i < n;++i)
      cin >> k[i] >> s[i];

    ans = 0.0;
    
    for(int i = 0;i < n;++i)
      ans = max(ans,(d-k[i])/s[i]);

    ans = d/ans;

    cout << "Case #" << id << ": " << fixed << ans << endl;

  }
  
  return 0;
}
