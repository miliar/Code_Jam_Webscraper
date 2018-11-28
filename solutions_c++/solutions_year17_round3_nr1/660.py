#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

#define rep(i, from, to) for (int i = from; i < to; i++)

typedef long long ll;
typedef vector<ll> vi;
typedef pair<ll,ll> ii;
typedef vector<ii> vii;
typedef long double lld;

const lld pi = acos(-1);

ll T, N, K, r, h, counter;
lld A, ma;
vi R, H;
vector<int> ind;

bool mySort(int i, int j) { return pi*lld(R[i])*lld(H[i]) > pi*lld(R[j])*lld(H[j]); }

int main(){
  cin >> T;
  rep(t, 1, T+1){
    cout << "Case #" << t << ": ";
    cin >> N >> K;
    R.clear(); H.clear(); ind.clear();
    rep(i, 0, N){
      cin >> r >> h;
      R.push_back(r); H.push_back(h);
      ind.push_back(i);
    }
    sort(ind.begin(), ind.end(), mySort);
    ma = 0.0;
    rep(i, 0, N){
      A = pi*lld(R[i])*lld(R[i]) + 2.0*pi*lld(R[i])*lld(H[i]);
      counter = 0;
      rep(j, 0, N){
        if (counter == K-1) break;
        if (ind[j] == i) continue;
        if (R[ind[j]] <= R[i]) { A += 2.0*pi*lld(R[ind[j]])*lld(H[ind[j]]); counter++; }
      }
      ma = max(ma, A);
    }
    cout << setprecision(10) << fixed << ma << endl;
  }

}
