#include <bits/stdc++.h>

#define INF (1e9)
#define INF_LL (1e17)
#define YJ 1145141919810
#define mod 1000000007

using LL = long long;
using ULL = unsigned long long;

using namespace std;

int TestCase;
LL N;

void input()
{
  cin >> N;
}

string dfs(string &ans)
{
  if(N == 0){
    return ans;
  }
  else if(N < 10){
    string a; a = N + '0';
    ans = a + ans;
    return ans;
  }
  else{
    LL tmpN = N;
    deque<int> list;

    while(tmpN > 0){
      list.push_front(tmpN % 10);
      tmpN /= 10;
    }

    bool flag = true;
    for (int i = 0; i < list.size()-1 && flag; i++) {
      if(list[i] > list[i+1]){
        flag = false;
      }
    }

    if(flag){
      string a;
      while(N > 0){
        string b; b = (N%10) + '0';
        a = b + a;
        N /= 10;
      }
      return a + ans;
    }
    else{
      ans = '9' + ans;
      N /= 10;
      N--;
      return dfs(ans);
    }

  }
}

string solve()
{
  string ans;
  return dfs(ans);
}

int main()
{
  cin >> TestCase;
  for (int i = 1; i <= TestCase; i++) {
    input();

    string ans = solve();

    printf("Case #%d: %s\n", i, ans.c_str());
  }

  return 0;
}
