
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

long long _atoi64(const string &s)
{
  long long res;
   std::istringstream ss(s);
   ss>>res;
   return res;
}
void solve(int a, int b)
{
  vector<string> ss;
  for (int i = 0;i < a;++i) {
    string s;
    cin>>s;
    ss.push_back(s);
  }
  for (int i = 0;i < ss.size();++i) {
    for (int j = 1;j < ss[i].size();++j) {
      if (ss[i][j] == '?') ss[i][j] = ss[i][j - 1];
    }
    for (int j = ss[i].size() - 2;j >= 0;--j) {
      if (ss[i][j] == '?') ss[i][j] = ss[i][j + 1];
    }
  }
  for (int i = 0;i < ss[0].size();++i) {
    for (int j = 1;j < ss.size();++j) {
      if (ss[j][i] == '?') ss[j][i] = ss[j - 1][i];
    }
    for (int j = ss.size() - 2;j >= 0;--j) {
      if (ss[j][i] == '?') ss[j][i] = ss[j + 1][i];
    }
    
  }
  
  for (int i = 0;i < ss.size();++i) {
    for (int j = 0;j < ss[i].size();++j) {
      cout<<ss[i][j];
    }
    cout<<endl;
  }
  
}

int main()
{
  //freopen("data.txt", "r", stdin);
  freopen("/home/zhanyi/Downloads/A-small-attempt0.in", "r", stdin);
	//freopen("A-small-practice.in", "r", stdin);
	//freopen("A-large-practice.in", "r", stdin);
  //freopen("ans.txt", "w", stdout);
  int t = 1;
  cin>>t;
  for (int i = 1;i <= t;++i) {
    cout<<"Case #"<<i<<":"<<endl;
    int a, b;
    cin>>a>>b;
    solve(a, b);
    
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
