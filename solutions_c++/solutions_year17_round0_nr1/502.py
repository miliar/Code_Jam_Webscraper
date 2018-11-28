#include<bits\stdc++.h>
using namespace std;

#define all(c) (c).begin(), (c).end()
int ni() { int val; scanf("%i", &val); return val; }
pair<int, int> npi() { pair<int, int> val; scanf("%i %i", &val.first, &val.second); return val; }
int64_t nll() { int64_t val; scanf("%I64d", &val); return val; }
vector<int> nvi(int n, int corr = 0){ vector<int> a(n); for (int i = 0; i < n; ++i) a[i] = ni() + corr; return move(a); }
char nc() { char val; do { val = getchar(); } while (val == ' ' || val == '\r' || val == '\n'); return val; }
char ncs() { char val; do { val = getchar(); } while (false); return val; }
string ns() { static char buff[1024 * 4000]; scanf("%s", buff); return string{ buff }; }
string nsl() { static char buff[1024 * 4000]; gets(buff); return string{ buff }; }
int64_t gcd(int64_t a, int64_t b) { while (b) { auto tmp = a % b; a = b; b = tmp; } return a; }

char flip_char(char c){
  return c == '+' ? '-' : '+';
}

void flip(string& s, int offset, int k){
  for (int i = offset; i < offset + k; ++i)
    s[i] = flip_char(s[i]);
}

int solve_bf(string s, int k){

  const int n = s.length();
  const int target = (1 << n) - 1;

  map<int, int> d;
  int cur_st = 0;
  for (int i = n - 1; i >= 0; --i) if (s[i] == '+'){
    cur_st |= 1 << (n - i - 1);
  }

  queue<int> que; que.push(cur_st);
  d[cur_st] = 0;

  while (d.find(target) == d.end() && !que.empty()){
    auto state = que.front(); que.pop();
    auto dcur = d[state];    
    for (int i = 0; i + k <= n; ++i){
      int next_st = state;
      for (int j = 0; j < k; ++j){
        next_st ^= (1 << (i + j));
      }
      if (d.find(next_st) == d.end()){
        d[next_st] = dcur + 1;
        que.push(next_st);
      }
    }
  }

  if (d.count(target))
    return d[target];
  return -1;
}

int solve(string s, int k){

  const int n = s.length();

  auto target = s;
  for (auto& ch : target){
    if (ch == '-')
      ch = flip_char(ch);
  }

  set<string> was;
  was.insert(s);

  int step = 0;
  for (int lp = 0, rp = n-1; lp < rp && s != target ; ){
    if (step & 1){
      while (rp >= 0 && s[rp] == '+')
        --rp;
      if (rp - k + 1 >= lp){
        flip(s, rp - k + 1, k);
        ++step;
      }
    }
    else{
      while (lp < n && s[lp] == '+')
        ++lp;
      if (lp + k - 1 <= rp){
        flip(s, lp, k);
        ++step;
      }
    }
    if (was.count(s))
      return -1;
    was.insert(s);
  }
  return step;
}

int main()
{
  int tests = ni();
  for (int cs = 1; cs <= tests; ++cs){
    printf("Case #%i: ", cs);   

    auto cakes = ns();
    auto k = ni();
    //int ans2 = solve_bf(cakes, k);
    //printf("ans2 = %i ", ans2);

    int ans = solve(cakes, k);
    if (ans == -1){
      printf("IMPOSSIBLE\n");
    }
    else{
      printf("%i\n", ans);
    }    
  }
  
  return 0;
}