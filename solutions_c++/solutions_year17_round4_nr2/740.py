#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int T,N,C,M;
vector<int> tickets[1002];
int cnt[1002];

int main () {

  cin >> T;

  for(int tc=1;tc<=T;tc++) {
    cin >> N >> C >> M;
    for(int i=0;i<1002;i++) {
      tickets[i].clear();
      cnt[i] = 0;
    }
    for(int i=0;i<M;i++) {
      int p,b;
      cin >> p >> b;
      tickets[b].push_back(p);
      cnt[p] ++;
    }
    int ret = 0;
    for(int i=1; i<=C;i++) ret = max(ret, (int)tickets[i].size());
    int ee = 0;
    int pr = 0;
    for(int i=1;i<=1000;i++) {
      if(cnt[i] > ret) {
        int lf = cnt[i] - ret;
        if (lf > ee) {
          ret = cnt[i];
          pr = 0;
          i = 0;
        } else {
          pr += lf;
        }
      } else {
        ee += ret - cnt[i];
      }
    }

    printf("Case #%d: ",tc);
    printf("%d %d", ret, pr);
    printf("\n");
  }

  return 0;
}