#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

#ifdef DEBUG
  #define DEB(x) cerr << x << '\n'
#else
  #define DEB(x)
#endif

typedef long long int ll;
typedef unsigned long long int ull;

#define MP make_pair
#define PB push_back

#define F first
#define S second

struct Pancake{
  ll r = 0;
  ll h = 0;
  //long double m = 0;
};

bool comp(Pancake &a, Pancake &b) {
  return a.r*a.h > b.r*b.h;
}

int main () {

  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int T;
  cin >> T;

  for(int i = 1; i <= T; i++) {
    ll N,K;
    cin >> N >> K;
    vector<Pancake> Ps(N);
    for(ll j = 0; j < N; j++) {
      cin >> Ps[j].r >> Ps[j].h;
    }

    sort(Ps.begin(), Ps.end(), comp);

    ll maxR = 0;

    ll m = 0;

    for(ll j = 0; j < K-1; j++) {
      maxR = max(maxR, Ps[j].r);
      m += Ps[j].r * Ps[j].h;
    }

    ll maxP = 0;
    // ll maxRR = 0;


    for(ll j = K-1; j < N; j++) {
      if(max(0ll, Ps[j].r*Ps[j].r-maxR*maxR)+2*Ps[j].r*Ps[j].h > maxP) {
        maxP = max(0ll, Ps[j].r*Ps[j].r-maxR*maxR)+2*Ps[j].r*Ps[j].h;
      }
    }

    // cout << m << " " << maxP << " " << maxR << endl;

    long double sum = 2*m+maxP+maxR*maxR;

    printf("Case #%i: %.8Lf\n", i, M_PI*sum);

    // cout << "Case #" << i << ": " << M_PI * sum << "\n";

  }



  return 0;
}
