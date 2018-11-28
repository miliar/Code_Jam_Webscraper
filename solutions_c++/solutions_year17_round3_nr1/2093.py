#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <map>

using namespace std;
int n, k;

struct pancake {
  unsigned long long r, h, s;
};

bool comparator(const pancake& left, const pancake& right) {
  return left.s > right.s;
}

pancake p[1000];
double ans;

int main() {
  int cases_count, imaxr;
  unsigned long long a, maxr, sum,b;
  cin >> cases_count;
  for (int _case = 1; _case <= cases_count; _case++) {
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
      cin >> p[i].r >> p[i].h;
      p[i].s = 2*p[i].r*p[i].h;
    }
    sort(p, p+n, comparator);
    imaxr = 0;

    for (int i = 0; i < n; i++) {
      if (p[i].r > p[imaxr].r) {
        imaxr = i;
      }
    }
    sum = 0;
    maxr = 0;
    for (int i = 0; i < k-1; i++) {
      sum += p[i].s;
      if (p[i].r > maxr) {
        maxr = p[i].r;
      }
    }

    if (imaxr < k) {
      sum += p[k-1].s;
      maxr = p[imaxr].r;
    } else {
      a = (p[imaxr].r - maxr)*(p[imaxr].r - maxr) + p[imaxr].s;
      b = p[k-1].s;
      if (p[k-1].r > maxr) {
        b+= (p[k-1].r - maxr)*(p[k-1].r - maxr);
      }

      if (a > b) {
        sum += p[imaxr].s;
        maxr = p[imaxr].r;
      } else {
        sum += p[k-1].s;
        maxr = max(maxr, p[k-1].r);
      }
    }
    cout << "Case #" << _case << ": ";
    ans = (double)(maxr * maxr + sum) * 3.14159265359;
    printf("%.8f\n", ans);
  }
  return 0;
}
