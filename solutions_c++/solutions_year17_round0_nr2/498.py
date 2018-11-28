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

bool is_tidy(int64_t v){
  auto s = to_string(v);
  for (int i = 1; i < s.length(); ++i){
    if (s[i] < s[i - 1])
      return false;
  }
  return true;
}

void update(string& s, int idx){
  if (s[idx] > '1' && (idx == 0 || s[idx] - 1 >= s[idx - 1])){
    s[idx]--;
    return;
  }
  if (idx > 0){
    s[idx] = '9';
    if (idx + 1 < s.length())
      s[idx] = s[idx + 1];
    update(s, idx - 1);
    return;
  }
  s[idx] = '0';
}

int64_t prev_tidy(int64_t v){  
  auto s = to_string(v);
  auto n = s.length();
  for (int i = 1; i < n; ++i){
    if (s[i] < s[i - 1]){
      for (int j = i; j < n; ++j){
        s[j] = '9';
      }
      update(s, i - 1);
      break;
    }
  }
  return strtoll(s.c_str(), nullptr, 10);
}

int main()
{
  freopen("inputs\\QF_1\\b-large.in", "r", stdin);
  freopen("inputs\\QF_1\\b-large.out", "w", stdout);

  int tests = ni();
  for (int cs = 1; cs <= tests; ++cs){
    printf("Case #%i: ", cs);
    auto n = nll();
    if (!is_tidy(n))
      n = prev_tidy(n);
    printf("%lld\n", n);
  }
  
  return 0;
}