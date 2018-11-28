
#include<bits/stdc++.h>

using namespace std;

#define all(c) (c).begin(), (c).end()
#define MP make_pair
#define PB push_back
#define sz(v) (int((v).size()))
int ni() { int val; scanf("%i", &val); return val; }
pair<int, int> npi() { pair<int, int> val; scanf("%i %i", &val.first, &val.second); return val; }
int64_t nll() { int64_t val; scanf("%I64d", &val); return val; }
vector<int> nvi(int n, int corr = 0) { vector<int> a(n); for (int i = 0; i < n; ++i) a[i] = ni() + corr; return move(a); }
char nc() { char val; do { val = getchar(); } while (val == ' ' || val == '\r' || val == '\n'); return val; }
char ncs() { char val; do { val = getchar(); } while (false); return val; }
string ns() { static char buff[1024 * 4000]; scanf("%s", buff); return string{ buff }; }
int64_t gcd(int64_t a, int64_t b) { while (b) { auto tmp = a % b; a = b; b = tmp; } return a; }
int64_t tr2(int xv1, int yv1, int xv2, int yv2, int x3, int y3) { return 1LL * (xv2 - xv1) * (y3 - yv1) - 1LL * (yv2 - yv1) * (x3 - xv1); }

typedef long double lfloat;
const lfloat eps = 1e-12;
bool eq(lfloat a, lfloat b) { return abs(a - b) <= eps; }

int8_t bits_cnt[256];
const string input_dir = "inputs\\";
string input_file = input_dir + "input.txt";
string output_file = input_dir + "output.txt";
void init_streams() {
#ifdef _LOCAL_TEST
  freopen(input_file.c_str(), "r", stdin);
  freopen(output_file.c_str(), "w", stdout);
#endif // _LOCAL_TEST  
}
void init_data() {
  bits_cnt[0] = 0;
  for (int i = 1; i <= 255; ++i) for (int j = 0; j < 8; ++j) if ((1 << j) & i)
    ++bits_cnt[i];
}
int get_bit_count(int v) {
  return bits_cnt[v & 0xFF] + bits_cnt[(v >> 8) & 0xFF] + bits_cnt[(v >> 16) & 0xFF] + bits_cnt[(v >> 24) & 0xFF];
}

const int maxt = 1440 + 4;
const int inf = 1000 * 1000;
int dp[maxt][2][2][maxt];

int main()
{
  init_streams();
  init_data();

  int test_cnt = ni();
  for (int tn = 1; tn <= test_cnt; ++tn)
  {
    printf("Case #%i: ", tn);

    auto C = ni(), J = ni();
    
    vector<int> act(maxt);
    for (int i = 0; i < C; ++i) {
      auto from = ni(), to = ni();
      for (int j = from; j < to; ++j)
        act[j] = 1;
    }
    for (int i = 0; i < J; ++i) {
      auto from = ni(), to = ni();
      for (int j = from; j < to; ++j)
        act[j] = 2;
    }

    for (int i = 0; i < maxt; ++i) for (int who = 0; who < 2; ++who) for (int strt = 0; strt < 2; ++strt) for (int j = 0; j < maxt; ++j)
      dp[i][who][strt][j] = inf;

    dp[0][0][0][0] = 0;
    dp[0][1][1][0] = 0;

    for (int tick = 0; tick <= 1440; ++tick) {
      for (int w = 0; w < 2; ++w) for (int st = 0; st < 2; ++st) {
        for (int tm = 0; tm <= tick; ++tm) if (dp[tick][w][st][tm] < inf) {
          if (act[tick + 1] != w + 1) {
            dp[tick + 1][w][st][tm + 1] = min(dp[tick + 1][w][st][tm + 1], dp[tick][w][st][tm]);
          }
          auto other = 1 - w;
          if (act[tick + 1] != other + 1) {
            auto other_tm = tick - tm;
            dp[tick + 1][other][st][other_tm + 1] = min(dp[tick + 1][other][st][other_tm + 1], dp[tick][w][st][tm] + 1);
          }
        }
      }
    }

    int ans = min(dp[1440][0][0][720], dp[1440][1][1][720]);
    ans = min(ans, dp[1440][0][1][720] + 1);
    ans = min(ans, dp[1440][1][0][720] + 1);
    printf("%i\n", ans);
  }

  return 0;
}