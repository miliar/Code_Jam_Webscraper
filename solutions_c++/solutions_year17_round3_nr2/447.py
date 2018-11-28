#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main() {
  int t, tt, ac, aj, tc, tj, i, ex;
  pair<int, char> st[200], ed[200];
  vector<int> gc, gj;
  cin >> t;
  for (tt = 1; tt <= t; tt++) {
    cin >> ac >> aj;
    tc = tj = 720;
    for (i = 0; i < ac; i++) {
      cin >> st[i].first >> ed[i].first;
      st[i].second = ed[i].second = 'c';
      tj -= ed[i].first - st[i].first;
    }
    for (; i < ac + aj; i++) {
      cin >> st[i].first >> ed[i].first;
      st[i].second = ed[i].second = 'j';
      tc -= ed[i].first - st[i].first;
    }
    sort(st, st + ac + aj);
    sort(ed, ed + ac + aj);
    ex = 0;
    gc.clear();
    gj.clear();
    for (i = 0; i < ac + aj - 1; i++) {
      if (st[i].second != st[i + 1].second) ex++;
      else if (st[i].second == 'j') {
        gc.push_back(st[i + 1].first - ed[i].first);
      } else {
        gj.push_back(st[i + 1].first - ed[i].first);
      }
    }
    if (st[i].second != st[0].second) ex++;
    else if (st[i].second == 'j') {
      gc.push_back(st[0].first + 1440 - ed[i].first);
    } else {
      gj.push_back(st[0].first + 1440 - ed[i].first);
    }
    sort(gc.begin(), gc.end());
    sort(gj.begin(), gj.end());
    for (i = 0; i < gc.size(); i++) {
      if (tc < gc[i]) ex += 2;
      else tc -= gc[i];
    }
    for (i = 0; i < gj.size(); i++) {
      if (tj < gj[i]) ex += 2;
      else tj -= gj[i];
    }
    cout << "Case #" << tt << ": " << ex << endl;
  }
  return 0;
}
