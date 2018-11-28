#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
long long int city_e[101];
long long int city_s[101];
long long int q_u[101];
long long int q_v[101];

long long int d[101][101];
int n, q;

long double rec(int speed, int i, long long int r, double dd) {
  if (i == n) {
    return dd;
  }

  int j = i+1;
  //cout << "!!! " << r - d[i][j] << " " << city_e[j] - d[i][j] << endl;
  //cout << i << " " << j << " " << city_e[j]  <<  " " <<  d[i][j] << endl;
  if (city_e[i] < d[i][j]) {
//    cout << "!!! " << r << " " << d[i][j] << endl;
    if (r >= d[i][j]) {
      return rec(speed, j, r-d[i][j], dd + (long double)d[i][j]/speed);
    } else {
      return -1;
    }
  } else {
    long double p1 = rec(city_s[i], j, city_e[i]-d[i][j], dd + (long double)d[i][j]/city_s[i]);
    if (r >= d[i][j]) {
      long double p2 = rec(speed, j, r-d[i][j], dd + (long double)d[i][j]/speed);
      if (p2 > 0.0) {
        if (p1 > 0.0) {
          return min(p2, p1);
        } else {
          return p2;
        }
      } else {
        return p1;
      }
    } else {
      return p1;
    }
  }
  /*
  if (d[i][j] <= r && (city_s[j] < speed || city_e[j] < d[i][j])) {
    return rec(speed, j, r-d[i][j], dd + (long double)d[i][j]/speed);
  } else {
    if (city_e[j]<d[i][j]) {
      cout << "ERROR";
      exit(1);
    }
    return
  }*/
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t;
  cin >> t;
  for (int _case = 1; _case <= t; _case++) {
    cin >> n >> q;
 //   cout << n << endl;
    for (int i = 1; i <= n; i++) {
      cin >> city_e[i] >> city_s[i];
    }
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        cin >> d[i][j];
      }
    }

    for (int i = 1; i <= q; i++) {
      cin >> q_u[i] >> q_v[i];
    }


    cout << "Case #" << _case << ": ";
    printf("%Lf\n", rec(city_s[1], 2, city_e[1]-d[1][2], (double)d[1][2]/city_s[1]));
  }
  return 0;
}
