#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
#include <map>
#include <sstream>
#include <string>
// www.boost.org
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/utility/binary.hpp>
using namespace std;
using namespace boost::multiprecision;

typedef pair<long double, int> EdgeArea;

bool compareEdgeArea(EdgeArea i, EdgeArea j) {
  return i.first > j.first;
}

long double maxExposed(long r[], long h[], int n, int k) {
  vector<EdgeArea> edgeAreas;
  for (int i = 0; i < n; i++) {
    EdgeArea currentArea(M_PI * r[i] * 2 * h[i], i);
    edgeAreas.push_back(currentArea);
  }
  sort(edgeAreas.begin(), edgeAreas.end(), compareEdgeArea);

  long double bestArea = 0;
  for (int i = 0; i < n; i++) {
    long double currentArea = M_PI * r[i] * r[i] + 2 * M_PI * r[i] * h[i];

    int numChosen = 1;
    for (int j = 0; j < n && numChosen < k; j++) {
      long double area = edgeAreas[j].first;
      int areaIndex = edgeAreas[j].second;

      if (areaIndex != i && r[i] >= r[areaIndex]) {
        currentArea += area;
        numChosen++;
      }
    }

    if (currentArea > bestArea) {
      bestArea = currentArea;
    }
  }

  return bestArea;
}

int main() {
  int t;
  scanf("%d\n", &t);

  for (int tc = 1; tc <= t; tc++) {
    int n, k;
    cin >> n >> k;

    long r[1001];
    long h[1001];
    for (int pci = 0; pci < n; pci++) {
      cin >> r[pci] >> h[pci];
    }

    cout << "Case #" << tc << ": ";
    cout << setprecision(32) << maxExposed(r, h, n, k) << endl;
    //printf("%.20Lf\n", maxExposed(r, h, n, k));
  }
}
