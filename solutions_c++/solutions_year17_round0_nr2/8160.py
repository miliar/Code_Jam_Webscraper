#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <limits>
#include <iostream>
#include <utility>

using namespace std;

#define TRACE(x...) x
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define PRINT(x...) TRACE(printf(x); fflush(stdout))

#define gc getchar  //unlocked linux
#define all(v) (v).begin(), (v).end()
#define FU(i, a, b) for(decltype(b) i = (a); i < (b); ++i)
#define fu(i, n) FU(i, 0, n)
#define FD(i, a, b) for (decltype(b) i = (b)-1; i >= a; --i)
#define fd(i, n) FD(i, 0, n)
#define mod(a, b) ((((a)%(b))+(b))%(b))
#define pb push_back
#define sz(c) int((c).size())
#define mk make_pair

const int INF = 0x3F3F3F3F; const int NEGINF = 0xC0C0C0C0;

const double EPS = 1e-8;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;

int cmp_double(double a, double b, double eps = 1e-9){
  return a + eps > b ? b + eps > a ? 0 : 1 : -1;  //0 = iguais, 1 = a maior
}

inline void scanint(int &x){
  register int c = gc();
  x = 0;
  int neg = 0;
  for(;((c<48 || c>57) && c != '-');c = gc());
  if(c=='-') {neg=1;c=gc();}
  for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
  if(neg) x=-x;
}

bool isHappy(string s){
  for (auto & c : s) if (c == '-') return false;
  return true;
}

void flip(string& s, int p, int K) {
  for (int i = p; i < p + K; i++) {
    if (s[i] == '+') s[i] = '-';
    else s[i] = '+';
  }
}

bool isTidy(ll N) {
  int top = -1;
  while (N != 0) {
    int dig = N% (ll)10;
    if (top == -1) top = dig;
    if (dig > top) return false;
    top = dig;
    N /= (ll)10;
  }
  return true;
}

vector<int> getDigs(ll N) {
  vector<int> ans;
  while(N != 0) {
    int dig = N % (ll)10;
    ans.pb(dig);
    N /= (ll)10;
  }
  reverse(ans.begin(), ans.end());
  return ans;
}

ll makeNumba(vector<int>& digs) {
  ll ans = 0;
  for (auto & d : digs) {
    ans *= (ll)10;
    ans += (ll)d;
  }
  return ans;
}

int main(){
  int T;
  int cases = 1;
  cin >> T;
  while(T--){
    printf("Case #%d: ", cases++);
    ll N; cin >> N;
    if (N < 10) {
      cout << N << endl;
      continue;
    }
    if (isTidy(N)) {
      cout << N << endl;
      continue;
    }
    vector<int> digs = getDigs(N);
    while(!isTidy(makeNumba(digs))) {
      for (int i = 0; i < digs.size()-1; i++) {
        if (digs[i] > digs[i+1]) {
          digs[i]--;
          for (int j = i + 1; j < digs.size(); j++) {
            digs[j] = 9;
          }
          break;
        }
      }
    }
done:
    cout << makeNumba(digs) << endl;
  }
  return 0;
}
