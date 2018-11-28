#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<pair<int, int>, int> iii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;

#define I18F 1000000000000000000 // 10^18
#define INF 2139062143
#define MEMSET_INF 127 // about 2B
#define MEMSET_HALF_INF 63 // about 1B

int T;

int main(){
  scanf("%d", &T);
  for(int _t = 1; _t <= T; ++_t){
    printf("Case #%d: ", _t);

    ll N;
    vi digits;
    scanf("%lld", &N);
    while(N > 0){
      digits.push_back((int) (N % 10));
      N = N / 10;
    }

    reverse(digits.begin(), digits.end());

    for(int k = 0; k < digits.size(); ++k){
      bool flag = false;
      for(int i = 0; i < digits.size(); ++i){
        if(flag){
          digits[i] = 9; continue;
        }
        if(i != digits.size() - 1 && digits[i] > digits[i+1]){
          digits[i]-=1;
          flag = true;
        }
      }
    }
    for(int i = 0; i < digits.size(); ++i){
      if(i == 0 && digits[i] == 0) continue;
      printf("%d", digits[i]); 
    }

    printf("\n");
  }

}
