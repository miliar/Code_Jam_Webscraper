#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

int main(){
  const int t = getInt();

  REP(cc,t){
    const int n = getInt();
    const int c = getInt();
    const int m = getInt();

    vector<vector<int> > v(n);

    REP(i,m){
      const int p = getInt() - 1;
      const int b = getInt() - 1;
      v[p].push_back(b);
    }

    int ans = 0;
    vector<int> cnts(c);
    int tot = 0;
    REP(i,n){
      tot += v[i].size();

      REP(j,v[i].size()){
	cnts[v[i][j]]++;
	ans = max(ans, cnts[v[i][j]]);
      }

      const int k = i + 1;
      ans = max(ans, (tot + k - 1) / k);
    }

    int pro = 0;
    REP(i,n) pro += max(0, (int)v[i].size() - ans);

    printf("Case #%d: %d %d\n", cc + 1, ans, pro);
  }

  return 0;
}
