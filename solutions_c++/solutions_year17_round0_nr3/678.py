#include <bits/stdc++.h>

#define INF (1e9)
#define INF_LL (1e17)
#define YJ 1145141919810
#define mod 1000000007

using LL = long long;
using ULL = unsigned long long;

using namespace std;

int TestCase;
LL N, K;

void input()
{
  cin >> N >> K;
}

pair<LL, LL> solve()
{
  pair<LL, LL> ans;

  set<LL> Set;
  map<LL, LL> Map;
  priority_queue<LL> que;

  Set.insert(N);
  que.push(N);
  Map[N]++;

  while(K > 0){

    LL tmpN = que.top();
    que.pop();
    Set.erase(tmpN);

    LL base = Map[tmpN];

    tmpN--;
    LL a = tmpN/2 + tmpN%2;
    LL b = tmpN/2;
    ans.first = a; ans.second = b;

    K -= base;
    Map[a] += base; Map[b] += base;
    if(Set.insert(a).second){
      que.push(a);
    }
    if(Set.insert(b).second){
      que.push(b);
    }

  }

  return ans;
}

int main()
{
  cin >> TestCase;
  for (int i = 1; i <= TestCase; i++) {
    input();

    pair<LL, LL> ans = solve();

    printf("Case #%d: %lld %lld\n", i, ans.first, ans.second);
  }

  return 0;
}
