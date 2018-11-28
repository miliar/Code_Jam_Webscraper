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

ll T, N, C, M, a, b, c1, c2;

int main(){
  cin >> T;
  rep(t, 0, T){
    cout << "Case #" << t+1 << ": ";
    cin >> N >> C >> M;
    if (C == 2){
      ll pos1[N], pos2[N]; c1 = c2 = 0;
      rep(i, 0, N){ pos1[i] = 0; pos2[i] = 0; }
      rep(i, 0, M){
        cin >> a >> b;
        if (b == 1) { pos1[a-1]++; c1++; }
        else { pos2[a-1]++; c2++; }
      }
      if (pos1[0]+pos2[0] <= max(c1, c2)){
        cout << max(c1, c2) << " ";
        rep(i, 0, N){
          if (pos1[i]+pos2[i] > max(c1, c2)){
            cout << pos1[i]+pos2[i]-max(c1, c2) << endl;
            break;
          }
          if (i == N-1) cout << 0 << endl;
        }
      } else {
        cout << pos1[0]+pos2[0] << " 0" << endl;
      }
    }
  }
}
