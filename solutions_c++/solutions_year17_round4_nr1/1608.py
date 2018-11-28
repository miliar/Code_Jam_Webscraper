
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
typedef pair<int,int> pint;
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

int calc(vector<int>& groups, int p) {
  int left = 0, res = 0;
  for (auto gr : groups) {
    if (left == 0)
      ++res;
    int n = (gr - left + p - 1) / p;
    left = n * p - gr + left;
  }
  return res;
}

int main()
{
  init_streams();
  init_data();

  int test_cnt = ni();
  for (int tn = 1; tn <= test_cnt; ++tn)
  {
    printf("Case #%i: ", tn);
    auto n = ni(), p = ni();
    vector<int> groups = nvi(n);

    vector<int> order;
    for (int i = 0, found = 1; found && i < n; ++i) {
      found = false;
      for(int j = 0; !found && j < n; ++j) if (groups[j] >= 0 && groups[j] % p == 0){
        order.push_back(groups[j]);
        groups[j] = -1;
        found = true;
      }
    }

    groups.erase(remove(all(groups), -1), groups.end());
    while (!groups.empty()) {
      auto rem = groups.front() % p;
      for (int i = 1; i < groups.size(); ++i) if ((groups[i] % p) + rem == p) {
        order.push_back(groups[i]);
        groups.erase(next(groups.begin(), i));
        break;
      }
      order.push_back(groups.front());
      groups.erase(groups.begin());
    }

    cout << calc(order, p) << endl;
  }

  return 0;
}