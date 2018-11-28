#include <bits/stdc++.h>

using namespace std;

struct event {
  char qui;
  int x;
  bool fi;
};

int main() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    int a, b;
    cin >> a >> b;
    int n = a + b;
    vector<event> ev(2 * n);
    for (int i = 0; i < a; ++i) {
      cin >> ev[2 * i].x;
      ev[2 * i].qui = 'a';
      ev[2 * i].fi = false;
      cin >> ev[2 * i + 1].x;
      ev[2 * i + 1].qui = 'a';
      ev[2 * i + 1].fi = true;
    }
    for (int i = 0; i < b; ++i) {
      cin >> ev[2 * a + 2 * i].x;
      ev[2 * a + 2 * i].qui = 'b';
      ev[2 * a + 2 * i].fi = false;
      cin >> ev[2 * a + 2 * i + 1].x;
      ev[2 * a + 2 * i + 1].qui = 'b';
      ev[2 * a + 2 * i + 1].fi = true;
    }
    sort(ev.begin(), ev.end(), [](event u, event v) {
        if (u.x != v.x) return u.x < v.x;
        return u.fi > v.fi;
        });
    int sa = 0, sb = 0, lliure = 0;
    int cota = 0;
    vector<int> ea, eb;
    for (int i = 0; i < 2 * n; ++i) {
      int ant = (i + 2 * n - 1) % (2 * n);
      int incr = ev[i].x - ev[ant].x;
      if (incr < 0) incr += 1440;
      if (ev[i].qui == ev[ant].qui) {
        if (ev[i].fi) {
          ((ev[i].qui == 'a') ? sa : sb) += incr;
        } else {
          ((ev[i].qui == 'a') ? ea : eb).push_back(incr);
          ((ev[i].qui == 'a') ? sa : sb) += incr;
        }
      } else {
        lliure += incr;
        ++cota;
      }
    }
    sort(ea.begin(), ea.end());
    sort(eb.begin(), eb.end());
    while ((720 - sa > lliure) or (720 - sb > lliure)) {
      if (720 - sa > lliure) {
        lliure += eb.back();
        sb -= eb.back();
        eb.pop_back();
        cota += 2;
      } else {
        lliure += ea.back();
        sa -= ea.back();
        ea.pop_back();
        cota += 2;
      }
    }
    cout << "Case #" << t << ": " << cota << endl;
  }
}
