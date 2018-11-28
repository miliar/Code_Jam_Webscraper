#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

using namespace std;
int get_length(unsigned long long x){
  int leng = 0;
  while (x)
  {
    x /= 10;
    leng++;
  }
  return leng;
}
int main(int argc, char *argv[]) {
  unsigned long long T, inNum, outNum;
  int leng;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cin >> inNum;

    unsigned long long calNum = inNum;
    while (calNum) {
      leng = get_length(calNum);
      unsigned long long temp_Num = calNum;
      int last_num, test_num = 9;

      for (int j = 0; j < leng; j++){

        last_num = temp_Num % 10;
        if (last_num == 0) {
          calNum--; break;
        }
        if (test_num < last_num) {
          calNum -= 1; break;
        }
        else {
          test_num = last_num;
        }
        if (j == leng-1) {
          outNum = calNum;
          calNum = 0;
        }
        temp_Num /= 10;
      }
    }

    cout << "Case #" << i << ": " << outNum << endl;
  }
  return 0;
}