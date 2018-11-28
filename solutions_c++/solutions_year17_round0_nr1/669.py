#include <bits/stdc++.h>

#define INF (1e9)
#define INF_LL (1e17)
#define YJ 1145141919810
#define mod 1000000007

using LL = long long;
using ULL = unsigned long long;

using namespace std;

int TestCase;
string str;
int K;

void input()
{
  cin >> str >> K;
}

int solve()
{
  int ret = 0;
  for (int i = 0; i+K <= str.length(); i++) {
    if(str[i] == '-'){
      ret++;
      for (int j = i; j < i+K; j++) {
        if(str[j] == '-'){
          str[j] = '+';
        }
        else{
          str[j] = '-';
        }
      }
    }
  }

  for (int i = 0; i < str.length(); i++) {
    if(str[i] == '-'){
      return -1;
    }
  }

  return ret;
}

int main()
{
  cin >> TestCase;
  for (int i = 1; i <= TestCase; i++) {
    input();

    int ans = solve();
    if(ans == -1){
      printf("Case #%d: IMPOSSIBLE\n", i);
    }
    else{
      printf("Case #%d: %d\n", i, ans);
    }
  }

  return 0;
}
