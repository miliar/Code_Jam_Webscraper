#include <bits/stdc++.h>

using namespace std;

vector<pair<double, double> > v;

int main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    int N, k, s;
    double D;
    cin >> D >> N;

    double ti = 0;
    for (int n=0; n<N; ++n) {
      cin >> k >> s;
      if ((D-k) / s > ti) {
        ti = (D-k) / s;
      }

      v.push_back(make_pair(k, s));
    }

    printf("Case #%d: %f\n", t+1, D/ti);
    continue;

    sort(v.begin(), v.end());

    if (N == 2 && v[0].second <= v[1].second) {
      N = 1;
    }

    if (N == 1) {
      printf("Case #%d: %f\n", t+1, (D * v[0].second) / (D - v[0].first));
      v.clear();
      continue;
    } else if (N == 2) {
      printf("Case #%d: %f\n", t+1, (D * v[1].second) / (D - v[1].first));

      v.clear();
      continue;
    }

    vector<pair<int, int> > a, b;

    vector<pair<int, int> > *current = &a, *last = &b, *tmp;

    for (auto it = v.rbegin(); it != v.rend(); it++) {
      current->push_back(*it);

      double Ceil = D;
      for (auto jt: *last) {
        if (it->second < jt.second) {
          continue;
        }

        double step = (it->first - jt.first) / (jt.second - it->second);

        if (it->first + it->second * step < Ceil) {
          Ceil = it->first + it->second * step;

          current->push_back(make_pair(
            it->first + it->second * step,
            jt.second
          ));
        }
      }

      tmp = current;
      current = last;
      last = tmp;

      current->clear();
    }

    double time = 0;
    for (int i=0; i<last->size(); ++i) {
      if (i + 1 < last->size()) {
        cout << ((*last)[i+1].first - (*last)[i].first) << "/" << (*last)[i].second << endl;
        time += ((*last)[i+1].first - (*last)[i].first) / (*last)[i].second;
      } else {
        cout << (D - (*last)[i].first) << "/" << (*last)[i].second << endl;
        time += (D - (*last)[i].first) / (*last)[i].second;
      }
    }

    cout << D << ' ' << time << endl;
    cout << "Case #" << t+1 << ": ";
    printf("%f\n", D/time);
    v.clear();
  }
}
