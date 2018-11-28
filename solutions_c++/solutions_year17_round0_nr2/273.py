#include <cstdio>
#include <cassert>
#include <vector>
using namespace std;
typedef long long int ll;

bool istidy(ll x) {
  ll lastd=9ll;
  while (x) {
    ll d=x%10ll;
    if (d>lastd) return false;
    lastd=d;
    x/=10ll;
  }
  return true;
}

ll solveBF(ll x) {
  while (!istidy(x)) --x;
  return x;
}

ll dec(const vector<ll>& digits) {
  ll m=1ll,r=0ll;
  for (vector<ll>::const_iterator it=digits.begin();it!=digits.end();++it) {
    r+=(*it)*m;
    m*=10ll;
  }
  assert(istidy(r));
  return r;
}

ll solve(ll x) {
  vector<ll> digits;
  while (x) {
    digits.push_back(x%10ll);
    x/=10ll;
  }
  int i=int(digits.size())-1;
  while (i>0) {
    if (digits[i]>digits[i-1]) break;
    --i;
  }
  if (i==0) return dec(digits);
  for (int j=0;j<i;++j) digits[j]=9;
  --digits[i];
  while (i+1<int(digits.size())) {
    if (digits[i+1]<=digits[i]) break;
    --digits[i+1];
    digits[i]=9;
    ++i;
  }
  return dec(digits);
}

void run() {
  ll N;
  scanf("%lld", &N);
  printf("%lld\n", solve(N));
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=1;t<=T;++t) {
    printf("Case #%d: ",t);
    run();
  }
  return 0;
}
