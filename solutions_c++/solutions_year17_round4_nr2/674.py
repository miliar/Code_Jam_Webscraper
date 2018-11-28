#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;
typedef long long Int;
typedef pair<Int, Int> P;

#define INF 1080

int n, c, m;
int p, b;
vector<P> vec;
int bcnt[1080];
int placecnt[1080];
int t;
int ok(int x){
  int res = 0;
  int sum = 0;
  for(int i = 1;i <= n;i++){
    if(placecnt[i] > x){
      sum += placecnt[i] - x;
      res += placecnt[i] - x;
    }
    if(sum > (i-1) * x)return INF;
    sum += min(x, placecnt[i]);
  }
  if(sum > n * x)return INF;
  return res;
}

void solve(){
  vec.clear();
  cin >> n >> c >> m;
  for(int i = 0;i < 1080;i++)placecnt[i] = bcnt[i] = 0;
  for(int i = 0;i < m;i++){
    cin >> p >> b;
    placecnt[p]++;
    bcnt[b]++;
  }
  
  int bottom = 0, top = m;
  for(int i = 1;i <= c;i++)bottom = max(bottom, bcnt[i] - 1);
  while(top - bottom > 1){
    int mid = (top + bottom) / 2;
    if(ok(mid)<INF)top = mid;
    else bottom = mid;
  }
  cout << top << " " << ok(top) << endl;
  return;
}

int main(){
  cin >> t;
  for(int i = 1;i <= t;i++){
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
