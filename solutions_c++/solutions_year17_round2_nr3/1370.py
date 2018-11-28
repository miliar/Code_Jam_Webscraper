#include <string.h>
#include <stdint.h>
#include <cstdio>
#include <cstdlib>
#include <ctype.h>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#include <fstream>
using namespace std;
typedef long long ll;
typedef pair<uint64_t,uint64_t> pii;
#define SZ(x) (int)(x.size())

#define for0n(i,n) for(i=0;i<n;i++)
#define for1n(i,n) for(i=1;i<=n;i++)
#define forn(i,j,n) for(i=j;i<n;i++)
#define ZERO(arr) for(int CNT=0;CNT<sizeof(arr);CNT++){arr[CNT]=0;}

const int MAX = 1000000;
const int inf = 2100000000;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

int moveDir[4][2] = { {0, -1} , {1, 0} , {0, 1} , {-1, 0} }; // N, E, S, W
char dirName[4] = { 'N', 'E', 'S', 'W' };

//ofstream debug("debug.txt", fstream::trunc);

//
// Add variables here.
//
int nCases;
int c, i, j, k, l;
double ans;

uint32_t my32;
uint64_t modArr[3][3];

// First is distance, second is speed
pii h[100];
uint64_t D[100][100];
pii trip[100];
uint64_t DT[100];
double bt[100];

int N, Q;

int main (int argc, char **argv)
{
  if (argc < 2) {
    printf("Specify input file\n");
    return -1;
  }

  ifstream inFile(argv[1]);
  ofstream outFile("output.txt", fstream::trunc);

  inFile >> nCases;
  cerr << nCases << " cases." << endl;
  for0n(c,nCases) {

    inFile >> N >> Q;
    for0n(i, N) {
      inFile >> h[i].first >> h[i].second;
    }
    for0n(i, N) {
      for0n(j, N) {
        inFile >> D[i][j];
      }
    }
    for0n(i, Q) {
      inFile >> trip[i].first >> trip[i].second;
    }
    DT[0] = 0;
    for(i = 1; i < N; i++) {
      DT[i] = DT[i-1] + D[i-1][i];
      // cout << i << ": " << DT[i] << endl;
    }

#if 0
    for (i = N-1; i > 0; i--) {
      double best = inf;
      // Find all viable horses
      for0n(j, i) {
        if (h[j].first >= DT[i] - DT[j]) {
          cout << j << " can get to " << i << endl;
        }
      }
    }
#endif
    bt[0] = 0;
    for(i = 1; i < N; i++) {
      double best = -1.0;
      // Find all viable horses
      for0n(j, i) {
        uint64_t dist = DT[i] - DT[j];
        if (h[j].first >= dist) {
          double tm = bt[j] + (double(dist) / double(h[j].second));
          if (best < 0) best = tm;
          if (tm < best) best = tm;
           //cout << j << " can get to " << i << endl;
           //cout << "dist: " << dist << " hs: " << h[j].second << " time: " << tm << endl;
           //cout << "bt[j] = " << bt[j] << endl;
        }
      }
      bt[i] = best;
    }
    ans = bt[N-1];

    cout.precision(6);
    cout.setf(ios::fixed, ios::floatfield);
    cout << "Case #" << c + 1 << ": " << ans << endl;
  }

  outFile.close();
  return 0;
}
