#include <algorithm>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
#include <cstring>

#define SIZE(s) ((int)((s).size()))
#define FOREACH(it,vec) for(typeof((vec).begin())it=(vec).begin();it!=(vec).end();++it)
#define REP(i,n) for(int i=0;i<(int)(n);++i)

using namespace std;

map<char, int> F;
map<int, char> G;

int T, N;

int main(void) {
  F['R'] = 0; F['O'] = 1; F['Y'] = 2; F['G'] = 3; F['B'] = 4; F['V'] = 5;
  G[0] = 'R'; G[1] = 'O'; G[2] = 'Y'; G[3] = 'G'; G[4] = 'B'; G[5] = 'V';
  cin >> T;
  REP(t, T) {
    vector<int> C(6);
    cin >> N;
    int s = 0;
    REP(i, 6) { cin >> C[i]; s += C[i]; }
    if (s == 1) {
      cout << "Case #" << (t+1) << ": ";
      REP(i, 6) if (C[i] > 0) cout << G[i] << endl;
      continue;
    }
    if (C[F['R']] == C[F['G']] && s == C[F['R']] + C[F['G']]) {
      cout << "Case #" << (t+1) << ": ";
      REP(i, C[F['R']]) cout << "RG"; cout << endl;
      continue;
    }
    if (C[F['Y']] == C[F['V']] && s == C[F['Y']] + C[F['V']]) {
      cout << "Case #" << (t+1) << ": ";
      REP(i, C[F['Y']]) cout << "YV"; cout << endl;
      continue;
    }
    if (C[F['B']] == C[F['O']] && s == C[F['B']] + C[F['O']]) {
      cout << "Case #" << (t+1) << ": ";
      REP(i, C[F['B']]) cout << "BO"; cout << endl;
      continue;
    }
    if ( (C[F['R']] <= C[F['G']] && C[F['G']] > 0) ||
         (C[F['Y']] <= C[F['V']] && C[F['V']] > 0) ||
         (C[F['B']] <= C[F['O']] && C[F['O']] > 0) ) {
      cout << "Case #" << (t+1) << ": " << "IMPOSSIBLE" << endl;
      continue;
    }
    C[F['R']] -= C[F['G']];
    C[F['Y']] -= C[F['V']];
    C[F['B']] -= C[F['O']];

    vector<pair<int, char> > S;
    S.push_back(make_pair(C[F['R']], 'R'));
    S.push_back(make_pair(C[F['Y']], 'Y'));
    S.push_back(make_pair(C[F['B']], 'B'));
    sort(S.begin(), S.end());
    reverse(S.begin(), S.end());

    if (S[0].first > S[1].first + S[2].first) {
      cout << "Case #" << (t+1) << ": " << "IMPOSSIBLE" << endl;
      continue;
    }
    
    vector<char> out(3*N, '.');
    REP(j, S[0].first) out[3*j] = S[0].second;
    REP(j, S[1].first) out[3*j+1] = S[1].second;
    REP(j, S[2].first) out[ 3*(S[0].first-S[2].first) + 3*j+2 ] = S[2].second;

    cout << "Case #" << (t+1) << ": ";
    REP(i, SIZE(out)) {
      if (out[i] == '.') continue;
      if (out[i] == 'R') while(C[F['G']] > 0) { cout << "RG"; --C[F['G']]; }
      if (out[i] == 'Y') while(C[F['V']] > 0) { cout << "YV"; --C[F['V']]; }
      if (out[i] == 'B') while(C[F['O']] > 0) { cout << "BO"; --C[F['O']]; }
      cout << out[i];
    }
    cout << endl;
  }
  return 0;
}
