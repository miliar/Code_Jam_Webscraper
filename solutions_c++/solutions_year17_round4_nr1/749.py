#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

char str[108][108];
int r, c;
int t;

int n, g[108], p;
int solve(){
  cin >> n >> p;
  int cnt[] = {0,0,0,0};
  for(int i = 0;i < n;i++){
    cin >> g[i];
    cnt[g[i]%p]++;
  }
  if(p == 2){
    return cnt[0] + (cnt[1] / 2) + (cnt[1] % 2);
  }
  if(p == 3){
    int onetwo = min(cnt[1], cnt[2]);
    cnt[1] -= onetwo;
    cnt[2] -= onetwo;
    return cnt[0] + onetwo + (cnt[1] / 3) + (cnt[1] % 3 != 0) + (cnt[2] / 3) + (cnt[2] % 3 != 0);
  }
  if(p == 4){
    int onethree = min(cnt[1], cnt[3]);
    int twotwo = cnt[2] / 2;
    cnt[1] -= onethree;
    cnt[3] -= onethree;
    cnt[2] -= twotwo * 2;
    if(cnt[2] && cnt[1])cnt[1] += 2;
    else if(cnt[2] && cnt[3])cnt[3] += 2;
    return cnt[0] + onethree + twotwo + (cnt[1] / 4) + (cnt[1] % 4 != 0) + (cnt[3] / 4) + (cnt[3] % 4 != 0);
  }
}

int main(){
  cin >> t;
  for(int i = 1;i <= t;i++){
    cout << "Case #" << i << ": " << solve() << endl;
  }
  return 0;
}
