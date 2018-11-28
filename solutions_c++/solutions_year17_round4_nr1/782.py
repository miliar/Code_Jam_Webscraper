#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

typedef long long ll;
typedef long double lld;
typedef vector<ll> vi;
typedef pair<ll,ll> ii;
typedef vector<ii> vii;

#define rep(i, from, to) for(int i = from; i < to; i++)
#define inf 1000000000000000000

ll T, N, P, A;

int main(){
  cin >> T;
  rep(t, 0, T){
    cout << "Case #" << t+1 << ": ";
    cin >> N >> P;
    ll C[P];
    rep(i, 0, P) C[i] = 0;
    rep(i, 0, N) { cin >> A; C[A%P]++; }
    if (P == 2) cout << C[0] + (C[1]+1)/2 << endl;
    else if (P == 3) cout << C[0]+(min(C[1], C[2]))+(abs(C[2]-C[1])+2)/3 << endl;
    else {
      if (C[2]%2 == 0){
        cout << C[0]+min(C[1], C[3])+(abs(C[1]-C[3])+3)/4+C[2]/2 << endl;
      } else {
        ll res = C[0];
        res += min(C[1], C[3]);
        res += C[2]/2;
        res += 1;
        ll cur = abs(C[3]-C[1]); cur -= 2;
        if (cur >= 0){
          cout << res + (cur+3)/4 << endl;
        } else {
          cout << res << endl;
        }
      }
    }
  }
}
