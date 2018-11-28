
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
int64_t tr2(int x1, int y1, int x2, int y2, int x3, int y3) { return 1LL * (x2 - x1) * (y3 - y1) - 1LL * (y2 - y1) * (x3 - x1); }

const string input_dir = "inputs\\";
string input_file = input_dir + "a-large.in";
string output_file = input_dir + "a-large.out";
void init_streams() {
  freopen(input_file.c_str(), "r", stdin);
  freopen(output_file.c_str(), "w", stdout);
}

int main()
{
  init_streams();
  auto t = ni(), cs = 0;
  while (cs < t) {
    printf("Case #%i: ", ++cs);
    
    auto to = ni();
    auto n = ni();
    vector<int64_t> ph(n);
    vector<int64_t> vh(n);
    for (int i = 0; i < n; ++i) {
      ph[i] = ni();
      vh[i] = ni();
    }

    double max_tm = 0.0;
    for (int i = 0; i < n; ++i) {
      double inv_speed = 1.0 / vh[i];
      max_tm = max(max_tm, inv_speed * (to - ph[i]));
    }

    auto res = to / max_tm;
    printf("%.12lf\n", res);
  }

  return 0;
}
