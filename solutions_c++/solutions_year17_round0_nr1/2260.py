#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include <limits>
#include <string>
#include <cstring>
#include <cassert>
#include <climits>
using namespace std;

typedef long long ll;

template<typename TH>
void debug_vars(const char* data, TH head){
	cerr << data << "=" << head << "\n";
}

template<typename TH, typename... TA>
void debug_vars(const char* data, TH head, TA... tail){
	while(*data != ',') cerr << *data++;
	cerr << "=" << head << ",";
	debug_vars(data+1, tail...);
}

#ifdef LOCAL
#define debug(...) debug_vars(#__VA_ARGS__, __VA_ARGS__)
#else
#define debug(...) {}
#endif

/////////////////////////////////////////////////////////

int main()
{
	string s;
	int t,k;
	cin>>t;
	for (int T = 1; T <= t; ++T) {
		cin>>s>>k;
		int ans = 0;
		for (int i = 0; i < s.size(); ++i) {
			if (s[i]=='-') {
				ans++;
				if (i+k-1>=s.size()) {
					ans = -1;
					break;
				}
				for (int j = 1; j < k; ++j) {
					s[i+j]=(s[i+j]=='+')?'-':'+';
				}
			}
		}
		if (ans==-1) 
			printf("Case #%d: IMPOSSIBLE\n", T);
		else 
			printf("Case #%d: %d\n", T, ans);
	}
}
