#include "bits/stdc++.h"
#define INF 1000000000;

using namespace std;

int k;
string line;

string flip(string &l, int start) {
  for (int i = start; i < start + k; ++i) {
    if(l[i] == '+') l[i] = '-';
    else l[i] = '+';
  }
  return l;
}

bool areHappy(string &l){
  for(int i = 0; i < l.size(); ++i){
    if(l[i] == '-') return false;
  }
  return true;
}

int solve(string l) {
  int cont = 0;
  int i = 0;
  while(!areHappy(l) && i < l.size()) {
    if(l[i] == '-' && i + k <= l.size()) {
      flip(l,i);
      ++cont;
      i = 0;
    } else ++i;
  }
  if(!areHappy(l)) return -1;
  return cont;

}
int main(int argc, char const *argv[]) {
  int TC;
  int c = 1;
  scanf("%d",&TC);
  while(TC--) {
    cin >> line >> k;
    int ans = solve(line);
    if (ans == -1) printf("Case #%d: IMPOSSIBLE\n",c++);
    else printf("Case #%d: %d\n",c++,solve(line));
  }
  return 0;
}
