#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

const int MAXD = 30;

vector<string> result;

bool valid(char* str){
  int s = strlen(str);
  for(int i=0; i<s-1; ++i) if(str[i] > str[i + 1]) return false;
  return true;
}

void solve(char* str){
  if(valid(str)){ result.push_back((string)str); return; }
  int N = strlen(str);
  for(int i=0; i<N-1; ++i){
    if(str[i] > str[i + 1]){
      str[i]--;
      for(int j=i+1; j<N; ++j) str[j] = '9';
    }
  }
  if(str[0] == '0') solve(str + 1);
  else solve(str);
}

int main(){
#ifdef DEBUG
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  char str[MAXD];
  int N, T;
  scanf("%d", &T);
  for(int i=0; i<T; ++i){
    scanf("%s", str);
    N = strlen(str);
    if(valid(str)){ result.push_back((string)str); continue; }
    solve(str);
  }
  for(int i=0; i<T; ++i) printf("Case #%d: %s\n", i + 1, result[i].c_str());
  return 0;
}
    