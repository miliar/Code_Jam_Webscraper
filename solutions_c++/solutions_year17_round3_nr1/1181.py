
#include <assert.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <stdlib.h>  
#include <stdio.h>  
#include <errno.h> 

using namespace std;

template<class T> std::string toString(T n) { std::ostringstream ost; ost<<n; ost.flush(    ); return ost.str(); }


vector<vector<double> > ans;
vector<pair<double, double> > vpr;

double dfs(int p, int k)
{
  if (ans[p][k] > 0) return ans[p][k];
  double pi = acos(-1.0);
  if (k <= 0) return 0;
  double base = pi * vpr[p].first * vpr[p].first + 2 * pi * vpr[p].first * vpr[p].second;
  if (k == 1) {
    ans[p][k] = base;
    return base;
  }
  double maxv = -1;

  for (int s = p + 1;s < vpr.size();++s) {
    int rest = vpr.size() - s;
    if (rest < k - 1) continue;
    double res = base + dfs(s, k - 1) - pi * vpr[s].first * vpr[s].first;
    
    if (res > maxv) maxv = res;
  }
  
  ans[p][k] = maxv;
  return maxv;
}
void solve(int N, int k)
{
  vpr.clear();
  for (int i = 0;i < N;++i) {
    double r, h;
    cin>>r>>h;
    vpr.push_back(make_pair(r, h));
  }
  sort(vpr.begin(), vpr.end(), greater<pair<double, double> >());
  
  ans = vector<vector<double> >(N, vector<double>(k + 1, -1));
  for (int i = 0;i < N;++i) {
    dfs(i, k);
  }
  double maxv = ans[0][k];
  for (int i = 0;i < N;++i) {
    if (ans[i][k] > maxv) maxv = ans[i][k];
  }
  printf("%.16f\n", maxv);
}

int main()
{
  //freopen("data.txt", "r", stdin);
  freopen("/home/zhanyi/Downloads/A-small-attempt0.in", "r", stdin);
	//freopen("A-small-practice.in", "r", stdin);
	//freopen("A-large-practice.in", "r", stdin);
  //freopen("ans.txt", "w", stdout);
  long long t = 1;
  cin>>t;
  for (long long i = 1;i <= t;++i) {
    cout<<"Case #"<<i<<": ";
    int N, k;
    cin>>N>>k;
    solve(N, k);
    
    //cin>>N>>k;
    //pair<long long, long long> pr = solve(N, k);
    //cout<<pr.first<<' '<<pr.second<<endl;

    //cout<<solve(s)<<' '<<gt(s)<<endl;
    //assert(gt(s) == solve(s));
    //if (s.size() == 1) {
    //  cout<<s<<endl;
    //} else {
    //  cout<<solve(s)<<endl;
    //}


		//break;
  }
	return 0;
}
