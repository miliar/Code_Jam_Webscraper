
#include<bits/stdc++.h>

using namespace std;

#define all(c) (c).begin(), (c).end()
int ni() { int val; scanf("%i", &val); return val; }
pair<int, int> npi() { pair<int, int> val; scanf("%i %i", &val.first, &val.second); return val; }
int64_t nll() { int64_t val; scanf("%I64d", &val); return val; }
vector<int> nvi(int n, int corr = 0) { vector<int> a(n); for (int i = 0; i < n; ++i) a[i] = ni() + corr; return move(a); }
char nc() { char val; do { val = getchar(); } while (val == ' ' || val == '\r' || val == '\n'); return val; }
char ncs() { char val; do { val = getchar(); } while (false); return val; }
string ns() { static char buff[1024 * 4000]; scanf("%s", buff); return string{ buff }; }
int64_t gcd(int64_t a, int64_t b) { while (b) { auto tmp = a % b; a = b; b = tmp; } return a; }

pair<int64_t, int64_t> simulate(int64_t n, int64_t k)
{
  vector<int> stall(n+2, 0);
  stall[0] = stall[n + 1] = 1;
  const int inf = 100000000;  
  pair<int64_t, int64_t> ans;
  for (int step = 0; step < k; ++step) {
    int max_max = 0, max_min = 0;
    int where = 0;
    for (int to = 1; to <= n; ++to) if (0 == stall[to]) {
      int rs = inf, ls = inf;
      for (int j = to + 1; j < stall.size(); ++j) {
        if (stall[j]) {
          rs = j - to;
          break;
        }
      }
      for (int j = to - 1; j >= 0; --j) {
        if (stall[j]) {
          ls = to - j;
          break;
        }
      }
      if (min(rs, ls) > max_min) {
        where = to;
        max_max = max(rs, ls);
        max_min = min(rs, ls);
      }
      else if (min(rs, ls) == max_min)
      {
        if (max(rs, ls) > max_max) {
          where = to;
          max_max = max(rs, ls);
          max_min = min(rs, ls);
        }
      }
    }

    stall[where] = step + 1;
    ans.first = max_max-1;
    ans.second = max_min-1;
  }
  return ans;
}

pair<int64_t, int64_t> get_stall(int64_t n, int64_t k) {  
  map<int64_t, int64_t> wins;
  wins[n] = 1;
  int64_t passed = 0;
  pair<int64_t, int64_t> ans;
  while (passed < k) {
    auto cur = *wins.rbegin();
    auto cur_sz = cur.first;
    auto cur_cnt = cur.second;
    wins.erase(prev(wins.end(), 1));
    int64_t new_sz, new_cnt;
    if (cur_sz & 1LL) {
      new_sz = cur_sz / 2;
      new_cnt = cur_cnt * 2;
      if (new_sz >= 1)
        wins[new_sz] += new_cnt;
    }
    else {
      new_sz = cur_sz / 2;
      new_cnt = cur_cnt;
      if (new_sz >= 1)
        wins[new_sz] += new_cnt;

      new_sz = (cur_sz - 1) / 2;
      if (new_sz >= 1)
        wins[new_sz] += new_cnt;
    }
    passed += cur_cnt;
    ans.first = cur_sz / 2;
    ans.second = (cur_sz - 1) / 2;
  }
  return ans;
}

int main()
{
  //freopen("inputs\\2017_CJ\\QF\\c-large.in", "r", stdin);
  //freopen("inputs\\2017_CJ\\QF\\c-large.out", "w", stdout);

  auto t = ni();
  for (int cs = 1; cs <= t; ++cs){
    printf("Case #%i: ", cs);
    auto n = nll();
    auto k = nll();    
    auto a = get_stall(n, k);
    printf("%lld %lld\n", a.first, a.second);    
  }

  return 0;
}