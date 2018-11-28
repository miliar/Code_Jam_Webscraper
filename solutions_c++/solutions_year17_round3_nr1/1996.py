/**
 * Problem: A
 */
#include <algorithm>
#include <assert.h>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <math.h>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>
#include <stdexcept>
#include <typeinfo>

#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
#define TR(x) cout << #x << " = " << x << endl
#define _ << " _ " <<
#define PI 3.1415926535897932384626433832795

using namespace std;

typedef pair <double, double > dd;

int R[1005];
int H[1005];
vector<pair <double, double> > P;
int N, K;

double areaD(double r) {
  return PI * r * r;
}

double areaH(double r, double h) {
  return 2 * PI * r * h;
}

double calc(int j, vector<dd> v) {
  if (SZ(v) == K) {
    double total = 0;
    double maxR = 0;
    F0(i, SZ(v)) {
      if (maxR < v[i].first) maxR = v[i].first;
      total += areaH(v[i].first, v[i].second);
    }
    total += areaD(maxR);
    return total;
  }

  if (j >= N) return 0;

  vector<dd> v1 = v;
  v1.push_back(P[j]);
  double r1 = calc(j+1, v1);
  double r2 = calc(j+1, v);
  return max(r1, r2);
}

int main(int argc, const char **argv) {
  int cases;
  cin >> cases;

  double r, h;

  F1(caseI, cases) {
    P.clear();
    cin >> N >> K;
    F0(i, N) {
      cin >> r >> h;
      P.push_back(make_pair(r, h));
    }
    vector<dd> v;
    double r = calc(0, v);
    cout << "Case #" << caseI << ": ";
    printf("%0.9f\n", r);
  }

  return 0;
}

