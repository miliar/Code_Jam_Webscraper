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
typedef pair<int,int> pii;
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
int ans;
int R,C;

uint32_t my32;
uint64_t modArr[3][3];

char cake[25][25];
bool done[26];

void printCake ()
{
    for0n(i, R) {
      for0n(j,C) {
        cout << cake[i][j];
      }
      cout << endl;
    }
}

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

    for0n(i, 26) done[i] = false;
    inFile >> R >> C;
    for0n(i, R) {
      for0n(j,C) {
        inFile >> cake[i][j];
      }
    }

    for0n(i, R) {
      for0n(j,C) {
        int ml,mr,mu,md;
        ml = mr = j;
        mu = md = i;
        if (cake[i][j] == '?') continue;
        char exp = cake[i][j];
        if (done[exp-'A']) continue;

        // cerr << "Found " << exp << " at " << j << ":" << i << endl;

        // Expand the letter left.
        for (k = j - 1; k >= 0; k--) {
          if (cake[i][k] != '?') {
            break;
          } else {
            ml = k;
          }
        }
        // Expand the letter right.
        for (k = j + 1; k < C; k++) {
          if (cake[i][k] != '?') {
            break;
          } else {
            mr = k;
          }
        }

        // cerr << "Stop at " << ml << ":" << mr << endl;

        // Fill up
        for (k = i - 1; k >= 0; k--) {
          bool valid = true;
          for (l = ml; l <= mr; l++) {
            if (cake[k][l] != '?') {
              valid = false;
              break;
            }
          }
          if (valid) {
            mu = k;
          } else {
            break;
          }
        }

        // Fill down
        for (k = i + 1; k < R; k++) {
          bool valid = true;
          for (l = ml; l <= mr; l++) {
            if (cake[k][l] != '?') {
              valid = false;
              break;
            }
          }
          if (valid) {
            md = k;
          } else {
            break;
          }
        }


        // Fill in
        for (l = mu; l <= md; l++) {
          for (k = ml; k <= mr; k++) {
            cake[l][k] = exp;
          }
        }
        done[exp-'A'] = true;
      }
    }

    cout << "Case #" << c + 1 << ":" << endl;
    printCake();
  }

  outFile.close();
  return 0;
}
