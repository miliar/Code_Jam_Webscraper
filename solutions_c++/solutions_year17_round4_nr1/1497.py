#include <bits/stdc++.h>

using namespace std;

#define DEBUG

#ifdef DEBUG
#define trace(x) cerr << #x <<": "<<x<<endl;
#else
#define trace(x)
#endif


int a[5];

int dp3[105][105][3];
int dp4[105][105][105];

int solve2(int x) {
  if(x < 0) return 0;
  return x/2;
}

map<int,int> memo3[105][105];
int solve3(int x,int y,int mm = 0) {
  if(memo3[x][y].count(mm))
    return memo3[x][y][mm];
  if(y < 0 || x < 0) return 0;
  int ans = 0;
  if(x) ans = max(ans,solve3(x - 1,y,(mm + 1) % 3) + ((mm + 1) == 3));
  if(y) ans = max(ans,solve3(x,y - 1,(mm + 2) % 3) + ((mm + 2) == 3));
  return memo3[x][y][mm] = ans;
}

map<int,int> memo4[105][105][105];
int solve4(int x,int y,int z,int mm = 0) {
  if(x < 0 || y < 0 || z < 0) return 0;
  if(memo4[x][y][z].count(mm))
    return memo4[x][y][z][mm];
  int ans = 0;
  if(x) ans = max(ans,solve4(x - 1,y,z,(mm + 1) % 4) + ((mm + 1) == 4));
  if(y) ans = max(ans,solve4(x,y - 1,z,(mm + 2) % 4) + ((mm + 2) == 4));
  if(z) ans = max(ans,solve4(x,y,z - 1,(mm + 3) % 4) + ((mm + 3) == 4));
  return memo4[x][y][z][mm] = ans;
  return 0;
}

void solve() {
  int n,p; cin>>n>>p;
  cerr<<n<<endl;
  for(int j = 0;j < p;j++)
    a[j] = 0;
  for(int i = 1;i <= n;i++) {
    int t; scanf("%d",&t);
    a[p - t % p]++;
    if(t % p == 0) a[0]++;
  }
  if(p == 2) {
    int ans = a[0] + solve2(a[1] - 1) + (a[1] > 0);
    cout<<ans<<endl;
  }
  else if(p == 3) {
    int ans = max(solve3(a[1] - 1,a[2]),solve3(a[1],a[2] - 1)) + a[0] + (a[1] > 0 || a[2] > 0);
    cout<<ans<<endl;
  }
  else {
    int ans = max({solve4(a[1] - 1,a[2],a[3]),solve4(a[1],a[2] - 1,a[3]),solve4(a[1],a[2],a[3] - 1)}) + a[0] + ((a[1] + a[2] + a[3]) > 0);
    cout<<ans<<endl;
  }
}

int main() {
  assert(freopen("input.txt","r",stdin));
  assert(freopen("output.txt","w",stdout));
  int t; cin>>t;
  int a[2];
  for(int i = 1;i <= t;i++) {
    cerr<<"Executing Case #"<<i<<endl;
    cout<<"Case #"<<i<<": ";
    solve();
  }

}
