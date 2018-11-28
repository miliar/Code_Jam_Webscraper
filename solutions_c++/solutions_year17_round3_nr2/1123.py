#define _CRT_SECURE_NO_WARNINGS

#include <algorithm>
#include <fstream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <iomanip>
#include <array>
#include <cmath>
#include <limits>
#include <cassert>
#include <math.h>
#include <memory.h>

//#pragma comment(linker, "/STACK:134217728")

using namespace std;
using namespace tr1;

#define all(c) (c).begin(), (c).end()
#define CLEAR(x) memset(x,0,sizeof x)

typedef long long ll;
typedef unsigned long long ull;

void solve(int test)
{
   printf("Case #%d: ", test + 1);
   int c_cnt;
   int j_cnt;

   cin >> c_cnt;
   cin >> j_cnt;
   
   vector<pair<int, int>> cameron;
  

   vector <pair<int, int>> jamie;
   int start, finish;
   for (int i = 0; i < c_cnt; ++i) {

      cin >> start;
      cin >> finish;
      cameron.push_back(make_pair(start, finish));
   }

   
   for (int i = 0; i < j_cnt; ++i) {
      cin >> start;
      cin >> finish;
      jamie.push_back(make_pair(start, finish));
   }

   sort(cameron.begin(), cameron.end());
   sort(jamie.begin(), jamie.end());

   int result;

   if (c_cnt == 2) {
      if (cameron[1].second - cameron[0].first <= 720) result = 2;
      else if (cameron[0].second + 1440 - cameron[1].first <= 720) result = 2;
      else result = 4;
   }
   else if (j_cnt == 2) {
      if (jamie[1].second - jamie[0].first <= 720) result = 2;
      else if (jamie[0].second + 1440 - jamie[1].first <= 720) result = 2;
      else result = 4;
   }
   else {
      result = 2;
   }


   printf("%d\n", result);
}

int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);

   int tests;
   scanf("%d", &tests);

   for (int test = 0; test < tests; ++test)
   {
      fprintf(stderr, "Solving %d/%d\n", test + 1, tests);
      solve(test);
   }

   return 0;
}
