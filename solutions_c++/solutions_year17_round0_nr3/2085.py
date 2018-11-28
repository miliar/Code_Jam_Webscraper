#include <iostream>
#include <map>
#include <algorithm>
using namespace std;
typedef long long ll;
int main()
{
  ios::sync_with_stdio(false);
  int T;
  ll K, N;
  cin >> T;
  for( int testcase = 1; testcase <= T; testcase++ ){
    cin >> N >> K;
    map<ll,ll> m;
    m[N]++;
    ll LS, RS;
    for( map<ll,ll>::reverse_iterator it = m.rbegin(); it != m.rend(); ++it ){
      ll d = it->first - 1;
      LS = d / 2;
      RS = d / 2 + d % 2;
      K -= it->second;
      if( K <= 0 ) break;
      m[LS] += it->second;
      m[RS] += it->second;
    }
    cout << "Case #" << testcase << ": " << max( LS, RS ) << ' ' << min( LS, RS ) << endl;
  }
}
