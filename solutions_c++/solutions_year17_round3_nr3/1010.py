
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


vector<double> pp;
vector<vector<double> > ans;

double dfs(int p, int k)
{
  if (p >= pp.size()) return 0;
  if (ans[p][k] >= 0) return ans[p][k];
  if (k == 0) {
    double res = 1;
    for (int i = p;i < pp.size();++i) res *= (1 - pp[i]);
    ans[p][k] = res;
    return res;
  }
  //if (k == 1) {
  //  double res = 1;
  //  for (int i = p;i < pp.size();++i) res *= (1 - pp[i]);
  //  ans[p][k] = 1 - res;
  //  return ans[p][k];
  //}
  int rest = pp.size() - p;
  if (rest == k) {
    double res = 1;
    for (int i = p;i < pp.size();++i) res *= pp[i];
    ans[p][k] = res;
    return res;
  } else if (rest < k) {
    ans[p][k] = 0;
    return 0;
  }
  double res = pp[p] * (dfs(p + 1, k - 1)) + (1 - pp[p]) * dfs(p + 1, k);
  ans[p][k] = res;
  return res;
}
void solve(int N, int k)
{
  double U;
  cin>>U;
  pp = vector<double> (N, 0);
  for (int i = 0;i < N;++i) {
    cin>>pp[i];
  }
  sort(pp.begin(), pp.end(), less<double>());

#if 0
  for (int i = N - 1;i >= N - k;i--) {
    double inc = min(U, 1 - pp[i]);
    pp[i] += inc;
    U -= inc;
  }
  for (int i = 0;i < N - k;++i) {
    if (i == N - 1) {
      for (int j = 0;j < N;++j) {
        pp[j] += U / N;
      }
    } else {
      double delta = pp[i + 1] - pp[i];
      double inc = min(U / (i + 1), delta);
      for (int j = 0;j <= i;++j) {
        pp[j] += inc;
      }
      U -= inc * (i + 1);
    }
  }
#else
  for (int i = N - 1;i >= k;i--) {
    double inc = min(U, 1 - pp[i]);
    pp[i] += inc;
    U -= inc;
  }
  for (int i = 0;i < k;++i) {
    if (i == N - 1) {
      for (int j = 0;j < N;++j) {
        pp[j] += U / N;
      }
    } else {
      double delta = pp[i + 1] - pp[i];
      double inc = min(U / (i + 1), delta);
      for (int j = 0;j <= i;++j) {
        pp[j] += inc;
      }
      U -= inc * (i + 1);
    }
  }
#endif
  ans = vector<vector<double> > (N, vector<double>(N + 1, -1));
  for (int j = 1;j <= N;++j) {
    for (int i = N - 1;i >= 0;--i) {
      double res = dfs(i, j);
      //cout<<i<<','<<j<<' '<<res<<endl;
    }
  }
  double res = 0;
  for (int i = k;i <= N;++i) {
    if (ans[0][i] > 0) {
    res += ans[0][i];
    }
  }
  
  
  printf("%.16f\n", res);
}

int main()
{
// freopen("data.txt", "r", stdin);
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
  }
	return 0;
}
