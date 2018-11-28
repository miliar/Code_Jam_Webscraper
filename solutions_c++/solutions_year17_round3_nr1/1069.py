#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>

#define PI 3.14159265359

using namespace std;

struct pancake {
  long long int r;
  long long int h;
  long long int pow;
  long long int bok;
};

bool op (pancake l, pancake r) {
  return l.bok > r.bok;
}

int main(){
  int t; cin >> t;
  for (int i = 1; i <= t; i++) {
    long long int k, n; cin >> n >> k;
    vector<pancake> tab;
    for (long long int j = 0; j < n; j++) {
      long long int r, h; cin >> r; cin >> h;
      pancake p;
      tab.push_back(p);
      tab[j].r = r; tab[j].h = h;
      tab[j].pow = (r) * (r);
      tab[j].bok = 2 * (r) * h;
    }
    sort(tab.begin(), tab.end(), op);
    for (int j = 0; j < n; j++) {
      //printf("pancake %d: %d %d: %d %d\n", j, tab[j].r, tab[j].h, tab[j].pow, tab[j].bok);
    }

    long long int pow = 0;
    for (long long int j = 0; j < k; j++) {
      pow = max(pow, tab[j].pow);
    }

    for (int j = k; j < n; j++) { // for the rest of K pancakes looking for something better than those K
      long long int diff = tab[j].pow + tab[j].bok - tab[k-1].bok - pow;
      if (diff > 0) {
        pow = tab[j].pow;
        pancake tmp = tab[k-1];
        tab[k-1] = tab[j];
        tab[j] = tmp;
      }
    }

    long long int res = pow;
    for (int j = 0; j < k; j++) {
      res += tab[j].bok;
    }

    printf("Case #%d: %f\n", i, (double) res * PI);

  }

}
