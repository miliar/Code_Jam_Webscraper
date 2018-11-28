#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <map>
#include <set>
#include <stdlib.h>
#include <string>
#include <queue>
#include <unordered_map>
using namespace std;

int main() {

  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  int testN; cin >> testN;

  for (int t = 1; t <= testN; t++) {
    cout << "Case #" << t << ": ";
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    set <pair <int, pair <int, char> > > st;
    st.insert(make_pair(-r, make_pair(0, 'R')));
    st.insert(make_pair(-y, make_pair(0, 'Y')));
    st.insert(make_pair(-b, make_pair(0, 'B')));
    string result = "";
    while (true) {
      auto it = st.begin();
      pair <int, pair <int, char> > fir = *it;
      if (fir.first == 0) break;
      it++;
      pair <int, pair <int, char> > sec = *it;
      if (result.length() == 0 || (result[result.length() - 1] != fir.second.second)) {
        result += fir.second.second;
        st.erase(fir);
        fir.first++;
        fir.second.first--;
        st.insert(fir);
      } else {
        if (sec.first == 0) {
          result = "IMPOSSIBLE";
          break;
        } else {
          result += sec.second.second;
          st.erase(sec);
          sec.first++;
          sec.second.first--;
          st.insert(sec);
        }
      }
    }

    for (int i = 0; i < result.length(); i++) {
      if (result[i] == result[(i + 1) % n]) {
        result = "IMPOSSIBLE";
        break;
      }
    }
    cout << result << "\n";
  }

  return 0;
}
