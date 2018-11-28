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

int main()
{
  int T;
  scanf("%d", &T);

  for(int t = 0; t < T; ++t) {
    printf("Case #%d: ", t+1);

    char number[30];
    char out[30];

    scanf("%s\n", number);

    int lastdigit = 0;


    int numlen = strlen(number);

    int lastup = 0;

    for (int i = 0; i < numlen; ++i) {
      int digit = number[i] - '0';
//      printf("\ndigit is %d", digit);
      out[i] = number[i];
      if(digit > lastdigit) {
        lastup = i;
        lastdigit = digit;
      } else if (digit < lastdigit) {
        --out[lastup];
        for(int j = lastup+1; j < numlen; ++j) {
          out[j] = '9';
        }
        break;
      }
    }
    out[numlen] = 0;

    int i = 0;
    while(out[i] == '0') ++i;

    printf("%s\n", out + i);
  }

  return 0;
}
