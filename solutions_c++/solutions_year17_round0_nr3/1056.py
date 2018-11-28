#include <bits/stdc++.h>

using namespace std;


typedef long long ll;
enum {VAL, CNT};
enum {EVN, ODD};

void printM(ll M[2][2][2]) {
  for (int i = 0; i < 2; ++i) {
    for (int j = 0; j < 2; ++j) {
      for (int k = 0; k < 2; ++k) {
        cout << M[i][j][k] << " ";
      }
      cout << endl;
    }
    cout << endl;
  }
}

pair<ll, ll> solve(ll N, ll K) {
  // prethodni-sljedeci, parni-neparni, vrijednost-broj
  ll M[2][2][2] = {{{N%2==0 ? N : N+1, N%2==0}, {N%2 ? N : N+1, N%2}}};
  pair<ll, ll> ret;
  ll cnt=0, cur=0, nxt=1, i=N%2, j=1;
  //cout << "N = " << N << " | K = " << K << endl;
  while(cnt<K) {
    cnt += M[cur][i][CNT];
    //cout << "cnt = " << cnt << endl;
    // x je manji od dva broja na sljedecoj razini
    ll x = (min(M[cur][EVN][VAL], M[cur][ODD][VAL])-1)/2;
    M[nxt][EVN][VAL] = x + x%2;
    M[nxt][ODD][VAL] = x + (x%2==0);
    // odd2evn oznacava da li se neparni dijeli na dva neparna ili na dva parna
    int odd2evn = (M[cur][ODD][VAL]+1)%4!=0;
    M[nxt][EVN][CNT] = odd2evn*2*M[cur][ODD][CNT] + M[cur][EVN][CNT];
    M[nxt][ODD][CNT] = (!odd2evn)*2*M[cur][ODD][CNT] + M[cur][EVN][CNT];
    //printM(M);
    if (i) {  // Ako dijelimo neparne
      if (odd2evn) {  // na dva parna
        ret = make_pair(M[nxt][EVN][VAL], M[nxt][EVN][VAL]);
      } else {  // na dva neparna
        ret = make_pair(M[nxt][ODD][VAL], M[nxt][ODD][VAL]);
      }
    } else {  // Ako dijelimo parne na jedan parni i jedan neparni
      ret = make_pair(max(M[nxt][EVN][VAL], M[nxt][ODD][VAL]), min(M[nxt][EVN][VAL], M[nxt][ODD][VAL]));
    }
    j++;
    // Svaka dva koraka nova razina
    if (j%2==0) {
      // odaberi veci
      i = M[nxt][ODD][VAL] > M[nxt][EVN][VAL];
      nxt = cur;
      cur = !cur;
    } else {
      i = !i;
    }
  }
  return ret;
}

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    ll N, K;
    cin >> N >> K;
    pair<ll, ll> ans = solve(N, K);
    cout << "Case #" << i << ": " << ans.first << " " << ans.second << endl;
  }
  return 0;
}
