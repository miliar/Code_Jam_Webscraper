#include <iostream>
#include <cstdio>
#include <cstdlib>

#define LL long long

using namespace std;

int tt;
LL n,k;

void solve(LL n,LL k) {
  if (k==1) {
    cout << n/2 << " " << (n-1)/2 << endl;
    return;
  }
  k--;
  if (k%2==0) solve((n-1)/2,k/2);
  else solve(n/2,k/2+1);
}

int main() {
  freopen("c.in","r",stdin);
  freopen("c.out","w",stdout);

  cin >> tt;

  for (int ii=1;ii<=tt;++ii) {
    cin >> n >> k;
    printf("Case #%d: ",ii);
    solve(n,k);
  }
}