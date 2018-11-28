#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <climits>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <set>
#include <unordered_set>
#include <cmath>
#include <map>
#include <functional>
#include <iomanip>
#define ull unsigned long long
using namespace std;
// clang++ -std=c++11 -stdlib=libc++ general.cpp
// ./a.out

char values[] = {'R', 'Y', 'B'};
int colors[3], original[3];
bool valid(string s){
  return s[0] != s[s.size()-1];
}
bool generate(char first, int N, int i){
  // printf("first: %c | (%d, %d, %d)\n", first, colors[0], colors[1], colors[2]);
  string ans="";
  ans += first;
  for(int j=1; j<N; j++){
    int most=-1;
    for(int k=0; k<3; k++)
      if(ans[ans.size()-1] != values[k] && colors[k] && (most==-1 || colors[k]>colors[most]))
        most = k;
    if(most==-1) return 0;
    ans += values[most];
    colors[most]--;
  }
  if(valid(ans)){
    printf("Case #%d: ", i);
    cout << ans << endl;
    return 1;
  }
  return 0;
}
int main(){
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  
  int T;
  scanf("%d", &T);

  for(int i=1; i<=T; i++){
    int N, O, G, V;
    scanf("%d %d %d %d %d %d %d", &N, &colors[0], &O, &colors[1], &G, &colors[2], &V);

    original[0] = colors[0]; original[1] = colors[1]; original[2] = colors[2];
    int j;
    for(j=0; j<3; j++){
      colors[0] = original[0]; colors[1] = original[1]; colors[2] = original[2];
      if(colors[j]){
        colors[j]--;
        if(generate(values[j], N, i)) break;
      }
    }
    if(j==3)
      printf("Case #%d: IMPOSSIBLE\n", i);
  }
}