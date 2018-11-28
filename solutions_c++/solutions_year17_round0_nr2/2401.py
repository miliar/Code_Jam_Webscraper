/*
 * Google Code Jam 2017
 * Qualification Round - Problem B - Tidy Numbers
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
  #define INPUT_FILE    "B-large.in"
  #define OUTPUT_FILE   "B-large.out"
#else
  #define INPUT_FILE    "input.txt"
  #define OUTPUT_FILE   "output.txt"
#endif

unsigned long long N;
vector<int> V;

void PreGen()
{
  // stuff which executes only once, before reading the input
}

void NumberToVector(unsigned long long n, vector<int>& v)
{
  v.clear();
  while (n > 0)
  {
    v.push_back(n % 10);
    n /= 10;
  }
}

bool check(unsigned long long n)
{
  vector<int> v;

  NumberToVector(n, v);

  for (int i = 0; i < v.size() - 1; ++i)
    if (v[i] < v[i + 1])
    {
      return false;
    }
  return true;
}

void Brute(unsigned long long n)
{
  while (!check(n)) --n;

  printf("%llu\n", n);
}

int Solve()
{
  // stuff which is executed for each input
  // expects the output to be printed out

  scanf("%llu", &N);

  //Brute(N);

  NumberToVector(N, V);

  for (int i = 0; i < V.size() - 1; ++i)
  {
    if (V[i] < V[i + 1])
    {
      --V[i + 1]; // decrease current digit

      // make all previous 9s
      // TODO: is this really correct? should we go to the previous group only?
      for (int j = 0; j <= i; ++j)
      {
        V[j] = 9;
      }
    }
  }
  while (V.size() > 0 && V[V.size() - 1] == 0)
  {
    V.pop_back();
  }

  for (int i = V.size() - 1; i >= 0; --i)
  {
    printf("%d", V[i]);
  }

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