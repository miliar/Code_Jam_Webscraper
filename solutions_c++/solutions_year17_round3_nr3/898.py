#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

bool op(double a, double b) {
  return a > b;
}

double cal_p(vector<double> tab, int n) {
  double ret = tab[0];
  for (int i = 1; i < n; i++) ret *= tab[i];
  return ret;  
}

int main(){
  int t; cin >> t;
  for (int i = 1; i <= t; i++) {
    int n, k; cin >> n >> k;
    double u; cin >> u;
    vector<double> tab;
    for (int j = 0; j < n; j++) {
      double q; cin >>  q;
      tab.push_back(q);
    }
    sort(tab.begin(), tab.end(), op);
//    for (int j = 0; j < n; j++) cout << p[j] << endl;
    while (u > 0) {
      int count = 0; double val = tab[k-1];
      int idx = k-1;
      while (idx >= 0 && tab[idx] == tab[k-1]) {
        count ++;
        idx --;
      }
      if (idx == -1) {
        double dif = u / k;
        for (int i = idx+1; i < k; i++) {
          tab[i] += dif;
          u -= dif;
        }
      } else {
        double next = tab[idx];
        double dif = next - tab[k-1];
        if (dif * count > u) dif = u/count;
        for (int i = idx+1; i < k; i++) {
          tab[i] += dif;
          u -= dif;
        }
      }
    }
    for (int j = 0; j < n; j++) {
      //printf("Case #%d %d core: %f\n", i, j, tab[j] );
    }
    if (k == n) {
      printf("Case #%d: %f\n", i, cal_p(tab, n));
    } else {
      printf("Case #%d: TODO\n", i);
    }
  }
}
