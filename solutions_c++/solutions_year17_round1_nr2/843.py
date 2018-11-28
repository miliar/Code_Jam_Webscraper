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
#define mp(x,y) std::make_pair(x,y)
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
int N,P;

uint32_t my32;
uint64_t modArr[3][3];

list<pii> ingredientRanges[50];
int recipe[50];

bool anyEmpty()
{
  int tmp;
  for0n(tmp, N) {
    if (ingredientRanges[tmp].empty()) {
      return true;
    }
  }
  return false;
}

pii combRange(pii f, pii s)
{
  pii tmp = mp(max(f.first, s.first), min(f.second, s.second));
  if (tmp.first > tmp.second) {
    return mp(0,0);
  } else {
    return tmp;
  }
}

pii findRange(int lowamt, int highamt, int rec)
{
  int templ = lowamt / rec;
  int temph = highamt / rec;
  if (lowamt % rec != 0) {
    templ++;
  }

  if (templ > temph) {
    return mp(0,0);
  }

  return mp(templ, temph);
}

int high(int in)
{
  int temp = in * 10;
  int temp2 = temp/9;
  //if (temp % 9 != 0) temp2--;

  return temp2;
}

int low(int in)
{
  int temp = in * 10;
  int temp2 = temp/11;
  if (temp % 11 != 0) temp2++;

  return temp2;
}

int multiple(int q, int r)
{
  int rough = round(float(q)/float(r));
  return rough;
}

int main (int argc, char **argv)
{
  if (argc < 2) {
    printf("Specify input file\n");
    return -1;
  }

#if 0
  cout << multiple(500,300) << endl;
  cout << multiple(450,300) << endl;
  cout << multiple(451,300) << endl;
  cout << multiple(449,300) << endl;
  cout << multiple(1260,70) << endl;
  cout << low(780) << ":" << high(780) << endl;
  cout << low(1000) << ":" << high(1000) << endl;
  cout << low(900) << ":" << high(900) << endl;
#endif

  ifstream inFile(argv[1]);
  ofstream outFile("output.txt", fstream::trunc);

  inFile >> nCases;
  cerr << nCases << " cases." << endl;
  for0n(c,nCases) {
    ans = 0;
    for0n(i,50) {
      ingredientRanges[i].clear();
    }
    inFile >> N >> P;
    for0n(i,N) {
      inFile >> recipe[i];
      // cerr << "Need " << recipe[i] << " for " << i << endl;
    }
    for0n(i,N) {
      vector<int> amts;
      for0n(j,P) {
        int temp;
        inFile >> temp;
        amts.push_back(temp);
      }
      sort(amts.begin(), amts.end());
      for0n(j,P) {
        int temp = amts[j];

        int lowt = low(temp);
        int hight = high(temp);
        pii range = findRange(lowt, hight, recipe[i]);
        if (range.first == 0) { continue; } // Don't remember useless amounts
        // cerr << "Have " << temp << "(" << lowt << ":" << hight << ") for " << i << endl;
        // cerr << "  - Range is " << range.first << ":" << range.second << endl;
        ingredientRanges[i].push_back(range);
      }
    }

    if (N == 1) {
      ans = ingredientRanges[0].size();
    } else {
      while (!anyEmpty()) {
        // See if we can make something with all the heads
        vector<pii> ingHeads;
        for0n(i, N) {
          ingHeads.push_back(ingredientRanges[i].front());
        }
        pii overallRange = combRange(ingredientRanges[0].front(),
                                     ingredientRanges[1].front());
        for (i = 2; i < N; i++) {
           overallRange = combRange(overallRange, ingredientRanges[i].front());
        }

        if (overallRange.first != 0) {
          for0n(i,N) {
            ingredientRanges[i].pop_front();
          }
          ans++;
        } else {
          int small = ingredientRanges[0].front().first;
          int sloc = 0;
          for0n(i,N) {
            int tmp = ingredientRanges[i].front().first;
            if (tmp < small) {
              small = tmp;
              sloc = i;
            }
          }
          ingredientRanges[sloc].pop_front();
        }
      }
    }


    cout << "Case #" << c + 1 << ": " << ans << endl;
  }

  outFile.close();
  return 0;
}
