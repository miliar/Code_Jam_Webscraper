/*
 * Google Code Jam 2017
 * Qualification Round - Problem A - Oversized Pancake Flipper
 */


#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <iostream>
#include <sstream>
#include <functional>
#include <deque>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define MIN(a, b)           ((a) > (b) ? (b) : (a))
#define MAX(a, b)           ((a) > (b) ? (a) : (b))
#define ABS(x)              ((x) > 0 ? (x) : -(x))
#define SGN(x)              (((x) == 0) ? 0 : ((x) > 0 ? 1 : -1))
#define SZ(a)               ((a).size())
#define FORN(_i, _n)        for (int (_i) = 0; (_i) < (_n); ++(_i))
#define FOR_(_i, _a, _b)    for (int (_i) = (_a); (_i) <= (_b); ++(_i))
#define ALL(stl)            (stl).begin(), (stl).end()
#define INF                 1000000000

using namespace std;


#define OFFICIAL 1

#if OFFICIAL
  #define INPUT_FILE    "A-large.in"
  #define OUTPUT_FILE   "A-large.out"
#else
  #define INPUT_FILE    "input.txt"
  #define OUTPUT_FILE   "output.txt"
#endif

string S;
int K, Sol;

void PreGen()
{
  // stuff which executes only once, before reading the input
}

int Solve()
{
  // stuff which is executed for each input
  // expects the output to be printed out
  char sz[1024];

  Sol = 0;
  scanf("%s %d\n", &sz, &K);
  S = sz;

  for (int i = 0; i <= S.size() - K; ++i)
  {
    if (S[i] == '-')
    {
      // flip K from here
      for (int j = 0; j < K; ++j)
      {
        S[i + j] = '+' + '-' - S[i + j]; // flip +/-
      }
      ++Sol;
    }
  }

  // check pancakes for non-happy faces
  for (int i = 0; i < S.size(); ++i)
    if (S[i] == '-')
    {
      printf("IMPOSSIBLE");
      return 0;
    }

  printf("%d", Sol);

  return 0;
}

int main()
{
  freopen(INPUT_FILE, "rt", stdin);

#if OFFICIAL
  freopen(OUTPUT_FILE, "wt", stdout);
#endif

  PreGen();

  int T, nt;

  scanf("%d\n", &T);

  for (nt = 1; nt <= T; ++nt)
  {
    printf("Case #%d: ", nt);

    if (Solve())
    {
    }

    printf("\n");
  }

  return 0;
}