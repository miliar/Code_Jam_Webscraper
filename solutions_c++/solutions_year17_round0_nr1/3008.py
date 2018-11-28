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
    char pancakes[1010];
    int s;
    cin >> pancakes;
    scanf("%d", &s);
    int b[1010];
    for(int i = 0; i < strlen(pancakes); ++i){
      b[i] = (pancakes[i] == '+') ? 1 : 0;
    }
    int ct = 0;
    bool flag = true;
    for(int i = 0; i < strlen(pancakes); ++i){
      if(b[i] == 1) continue;
      if(i > strlen(pancakes) - s){
        flag = false;
        break;
      }
      ct++;
      for(int j = i; j < i+s; ++j) b[j] = 1 - b[j];
    }
    if(flag){
      printf("Case #%d: %d\n", _t, ct);
    }else{
      printf("Case #%d: IMPOSSIBLE\n", _t);
    }
  }

}
