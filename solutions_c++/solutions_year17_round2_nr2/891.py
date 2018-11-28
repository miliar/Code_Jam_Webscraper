#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
#include <iomanip>
#include <map>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    int N;
    cin >> N;

    map<char, int> ks;
    map<char, int> zs;
    {
      int R, O, Y, G, B, V;
      cin >> R >> O >> Y >> G >> B >> V;
      ks['R'] = R - G;
      ks['Y'] = Y - V;
      ks['B'] = B - O;
      zs['O'] = O;
      zs['G'] = G;
      zs['V'] = V;
    }

    if (ks['R'] < 0 || ks['Y'] < 0 || ks['B'] < 0) {
      cout << "Case #" << (t + 1) << ": " << "IMPOSSIBLE" << endl;
      continue;
    }

    if (
      !ks['R'] && zs['G'] && (N - 2 * zs['G'])
      || !ks['Y'] && zs['V'] && (N - 2 * zs['V'])
      || !ks['B'] && zs['O'] && (N - 2 * zs['O'])
    ) {
      cout << "Case #" << (t + 1) << ": " << "IMPOSSIBLE" << endl;
      continue;
    }

    vector<pair<int, char> > wmap2;
    for (auto p : ks) {
      wmap2.push_back(make_pair(-p.second, p.first));
    }
    sort(wmap2.begin(), wmap2.end());

    vector<char> wmap;
    vector<int> ws;
    for (auto p : wmap2) {
      wmap.push_back(p.second);
      ws.push_back(-p.first);
    }

    int det = ws[1] + ws[2] - ws[0];
    if (det < 0) {
      cout << "Case #" << (t + 1) << ": " << "IMPOSSIBLE" << endl;
      continue;
    }

    vector<char> ds;
    for (int i = 0; i < det; i++) {
      ds.push_back(wmap[0]);
      ds.push_back(wmap[1]);
      ds.push_back(wmap[2]);
    }
    ws[0] -= det;
    ws[1] -= det;
    ws[2] -= det;

    for (int i = 0; i < ws[1]; i++) {
      ds.push_back(wmap[0]);
      ds.push_back(wmap[1]);
    }
    for (int i = 0; i < ws[2]; i++) {
      ds.push_back(wmap[0]);
      ds.push_back(wmap[2]);
    }

    {
      auto it = find(ds.begin(), ds.end(), 'R');
      vector<char> es;
      for (int i = 0; i < zs['G']; i++) {
        es.push_back('R');
        es.push_back('G');
      }
      ds.insert(it, es.begin(), es.end());
    }

    {
      auto it = find(ds.begin(), ds.end(), 'Y');
      vector<char> es;
      for (int i = 0; i < zs['V']; i++) {
        es.push_back('Y');
        es.push_back('V');
      }
      ds.insert(it, es.begin(), es.end());
    }

    {
      auto it = find(ds.begin(), ds.end(), 'B');
      vector<char> es;
      for (int i = 0; i < zs['O']; i++) {
        es.push_back('B');
        es.push_back('O');
      }
      ds.insert(it, es.begin(), es.end());
    }

    if (ds[0] == ds[ds.size() - 1]) {
      cout << "Case #" << (t + 1) << ": " << "IMPOSSIBLE" << endl;
      continue;
    }

    cout << "Case #" << (t + 1) << ": ";
    for (char d : ds) {
      cout << d;
    }
    cout << endl;
  }

  return 0;
}
