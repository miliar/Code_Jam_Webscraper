
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
pair<long long, long long> solve(long long N, long long k)
{
  if (N == k) {
    return make_pair(0LL, 0LL);
  }
  if (k == 1) {
    return make_pair(N / 2, (N - 1) / 2);
  }
  if (N % 2 == 1 && k % 2 == 1) {
    return solve((N - 1) / 2, (k - 1) / 2);
  } else if (N % 2 == 1 && k % 2 == 0) {
    return solve((N - 1) / 2, (k - 1) / 2 + 1);
  } else if (N % 2 == 0 && k % 2 == 0) {
    return solve((N) / 2, (k) / 2);
  } else if (N % 2 == 0 && k % 2 == 1) {
    return solve((N - 1) / 2, (k - 1) / 2);
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
    cout<<"Case #"<<i<<": ";
    long long N, k;
    cin>>N>>k;
    pair<long long, long long> pr = solve(N, k);
    cout<<pr.first<<' '<<pr.second<<endl;

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
