#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long lglg;


bool checkfree(char row[], int c) {
  for (int j = 0; j < c; ++j) {
    if(row[j] != '?') {
      return false;
    }
  }
  return true;
}

void fillrow(char row[], int c) {
  int lastletter = 0;
  int j = 0;
  for (; j < c; ++j) {
    if(row[j] != '?') {
      break;
    }
  }
  for (int i = 0; i < j; ++i) {
    row[i] = row[j];
  }
  for(int i = j; i < c; ++i) {
    if(row[i] != '?') {
      lastletter = row[i];
    } else {
      row[i] = lastletter;
    }
  }
}

int main()
{
  int T;
  scanf("%d", &T);

  for(int t = 0; t < T; ++t) {
    printf("Case #%d:\n", t+1);

    int r, c;
    char row[30];
    string lastrow;

    scanf("%d %d\n", &r, &c);

    int i = 0;
    for(; i < r; ++i) {
      scanf("%s\n", row);
      bool free = checkfree(row, c);
      if(!free) {
        fillrow(row, c);
        for (int j = 0; j <= i; ++j) {
          printf("%s\n", row);
        }
        lastrow = row;
        break;
      }
    }
    ++i;

    for(; i < r; ++i) {
      scanf("%s\n", row);
      bool free = checkfree(row, c);
      if(free) {
        printf("%s\n", lastrow.c_str());
      } else {
        fillrow(row, c);
        printf("%s\n", row);
        lastrow = row;
      }
    }
  }

  return 0;
}

