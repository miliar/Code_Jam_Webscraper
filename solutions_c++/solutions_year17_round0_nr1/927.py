#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int st[1050];

string a;
int K;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("answer.txt", "w", stdout);
  int T;
  cin>>T;
  for (int _ = 1; _ <= T; _++)
  {
    cin>>a;
    cin>>K;
    for (int i = 0; i < a.length(); i++)
      st[i] = (a[i]=='-'?0:1);
    int cnt = 0;
    for (int i = 0; i + K <= a.length(); i++) {
      if (st[i] == 0) {
        cnt++;
        for (int j = 0; j < K; j++)
          st[i+j] = (st[i+j]==0?1:0);
      }
    }
    bool flag = true;
    for (int i = 0 ; i < a.length(); i++) {
      if (st[i] == 0)
        flag = false;
    }
    if (!flag)
      printf("Case #%d: IMPOSSIBLE\n", _);
    else
      printf("Case #%d: %d\n", _, cnt);
  }
}
