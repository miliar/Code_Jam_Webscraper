#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <utility>
#include <cmath>
using namespace std;

int T, N, P, R[55], Q[55][55], ans, start, stop, countr[55], alive, amt, ingredient, saved[55];

int main() {
  ifstream fin("B-large.in");
  ofstream fout("B-large.out");
  fin >> T;
  for (int t = 1 ; t <= T ; t++) {
    fin >> N >> P;
    ans = 0;
    for (int i = 0 ; i < N ; i++) {
      countr[i] = 0;
      saved[i] = 0;
      fin >> R[i];
    }
    for (int i = 0 ; i < N ; i++) {
      for (int j = 0 ; j < P ; j++) {
        fin >> Q[i][j];
      }
      sort(Q[i], Q[i] + P);
    }
    vector<pair<int, pair<int, int>>> sweep;
    for (int j = 0 ; j < P ; j++) {
      for (int i = 0 ; i < N ; i++) {
        start = ceil(Q[i][j]/1.1/R[i]);
        stop = (int)(Q[i][j]/0.9/R[i]);
        if (start <= stop) {
          sweep.push_back(make_pair(start, make_pair(1, i)));
          sweep.push_back(make_pair(stop + 1, make_pair(-1, i)));
        }
      }
    }
    sort(sweep.begin(), sweep.end());
    alive = 0;
    for (int i = 0 ; i < sweep.size() ; i++) {
      amt = sweep[i].second.first;
      ingredient = sweep[i].second.second;
      if (countr[ingredient] == 0 && amt == 1) {
        alive++;
      } else if (countr[ingredient] == 1 && amt == -1 && !saved[ingredient]) {
        alive--;
      }
      if (saved[ingredient] && amt == -1) {
        saved[ingredient]--;
      } else {
        countr[ingredient] += amt;
      }
      if (alive == N) {
        ans++;
        for (int j = 0 ; j < N ; j++) {
          countr[j]--;
          if (countr[j] == 0) alive--;
          saved[j]++;
        }
      }
    }
    fout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}