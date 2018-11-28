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

int n;
char f[128][128];
int best = 0;
char fres[128][128];

bool get_next_p(int& r, int& c){
  if (r == n && c == n)
    return false;
  if (c == n)
    r += 1, c = 1;
  else
    c += 1;
  return true;
}

int get_fash_value(){
  int ans = 0;
  for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j){
    if (f[i][j]){
      ++ans;
      if (f[i][j] == 'o')
        ++ans;
    }
  }
  return ans;
}

bool is_valid_field(){
  // check rows and cols
  for (int i = 1; i <= n; ++i){
    int others_hor = 0, others_ver = 0;
    for (int j = 1; j <= n && others_hor <= 1 && others_ver <= 1; ++j){
      if (f[i][j] && f[i][j] != '+')
        ++others_hor;
      if (f[j][i] && f[j][i] != '+')
        ++others_ver;
    }
    if (others_hor > 1 || others_ver > 1)
      return false;
  }

  for (int i = 1; i <= n; ++i){
    int others = 0;
    for (int j = 1; j + i - 1 <= n && others <= 1; ++j){
      if (f[i + j - 1][j] && f[i + j - 1][j] != 'x')
        ++others;
    }
    if (others > 1) return false;
    others = 0;
    for (int j = 1; j + i - 1 <= n && others <= 1; ++j){
      if (f[j][i + j - 1] && f[j][i + j - 1] != 'x')
        ++others;
    }
    if (others > 1) return false;
    others = 0;
    for (int j = 1; j + i - 1 <= n && others <= 1; ++j){
      if (f[i + j - 1][n - j + 1] && f[i + j - 1][n - j + 1] != 'x')
        ++others;
    }
    if (others > 1) return false;
    others = 0;
    for (int j = 1; j + i - 1 <= n && others <= 1; ++j){
      if (f[j][n - i - j + 2] && f[j][n - i - j + 2] != 'x')
        ++others;
    }
    if (others > 1) return false;
  }
  return true;
}

void update_best(int bv){
  if (bv > best){
    best = bv;
    memcpy(fres, f, sizeof(f));
  }
}

void go(int ans, int r, int c){
  if (f[r][c]){
    if (f[r][c] == 'o'){
      ans += 2;
      if (!get_next_p(r, c))
        update_best(ans);
      else
        go(ans, r, c);
    }
    else{
      ans += 1;
      update_best(ans);
      int nr = r, nc = c;
      auto has_next = get_next_p(nr, nc);
      // leave as is
      if (has_next)
        go(ans, nr, nc);
      // upgrade
      auto pr = f[r][c];
      f[r][c] = 'o';
      if (is_valid_field()){
        ans += 1;
        update_best(ans);
        if (has_next)
          go(ans, nr, nc);
      }
      f[r][c] = pr;
    }
  }
  else
  {
    static const array<char, 4> vars = { '+', 'x', 'o', '\0' };
    static const array<char, 4> cost = { 1, 1,2, 0 };
    for (int i = 0; i < vars.size(); ++i){
      f[r][c] = vars[i];
      if (is_valid_field()){
        auto cst = ans + cost[i];
        update_best(cst);
        int nr = r, nc = c;
        if (!get_next_p(nr, nc))
          return;
        else
          go(cst, nr, nc);
      }
    }
    f[r][c] = 0;
  }
}

struct Update{
  int r, c;
  char chr;
};

vector<Update> updates;
void push_update(int r, int c, char ch){
  f[r][c] = ch;
  updates.emplace_back(Update{r,c,ch});
}

int main()
{
  //freopen("inputs\\QF_1\\d-small.in", "r", stdin);
  //freopen("inputs\\QF_1\\d-small.out", "w", stdout);

  int tests = ni();
  for (int cs = 1; cs <= tests; ++cs)
  {
    printf("Case #%i: ", cs);
    memset(f, 0, sizeof(f));
    
    n = ni();
    auto m = ni();
    int os = 0, op = 0, tp = 0;
    for (int i = 0; i < m; ++i){
      auto type = nc();
      auto r = ni();
      auto c = ni();
      f[r][c] = type;
      if (type == 'o' || type == 'x')
        ++os, op = c, tp = type;
    }

    updates.clear();
    if (!os){
      op = 1;
      push_update(1, 1, 'o');
    }
    else if (tp == 'x'){
      push_update(1, op, 'o');
    }
    for (int i = 1; i <= n; ++i){
      if (!f[1][i])
        push_update(1, i, '+');
    }

    if (op < n)
    {
      for (int j = op + 1; j <= n; ++j)
        push_update(j, j, 'x');
      for (int j = 2; j < n; ++j)
        push_update(n, j, '+');
      for (int j = 1; j + 1 <= n && j < op; ++j)
        push_update(j+1, j, 'x');
    }
    else if (n > 1){
      if (n == 2){
        push_update(2, 1, 'x');
      }
      else
      {
        for (int j = 2; j + 1 < n; ++j)
          push_update(n, j, '+');
        push_update(n, n - 1, 'o');
        for (int j = 1; j + 1 < n && j < op; ++j)
          push_update(j + 1, j, 'x');
      }
    }

    auto res = get_fash_value();
    printf("%i %i\n", res, updates.size());
    for (int i = 0; i < updates.size(); ++i){
      printf("%c %i %i\n", updates[i].chr, updates[i].r, updates[i].c);
    }
  }
  
  return 0;
}