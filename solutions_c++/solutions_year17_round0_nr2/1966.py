
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
long long solve(string &s)
{
  long long res;
  
  while (true) {
    int find = 0;
    for (int i = 0;i < s.size() - 1;++i) {
      if (s[i] > s[i + 1]) {
        find = 1;
        string p1(s.begin(), s.begin() + i + 1);
        string p2(s.begin() + i + 1, s.end());
        long long p = _atoi64(p1.c_str());
        for (int j = 0;j < p2.size();++j) {
          p2[j] = '9';
        }
        p = p - 1;
        if (p == 0) {
          s = p2;
          res = _atoi64(s.c_str());
          return res;
        } else {
          s = toString(p) + p2;
        }
      }
    }
    if (find == 0) {
      res = _atoi64(s.c_str());
      return res;
    }
  }
  return res;
}
long long gt(string &s)
{
  long long N = _atoi64(s.c_str());
  long long res = 1;
  for (int i = 1;i <= N;++i) {
    string t = toString(i);
    int find = 0;
    for (int j = 0;j < t.size() - 1;j++) {
      if (t[j] > t[j + 1]) {
        find = 1;
      }
    }
    if (find == 0) {
      res = i;
    }
  }
  return res;
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
    cout<<"Case #"<<i<<": ";
    string s;
    cin>>s;
    cout<<solve(s)<<endl;

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
