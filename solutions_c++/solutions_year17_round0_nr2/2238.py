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
	string n;
	int t;
	cin>>t;
	for (int T = 1; T <= t; ++T) {
		cin>>n;
		int i;
		for (i = 0; i < n.size()-1; ++i) {
			if (n[i]>n[i+1]) {
				break;
			}
		}
		cout<<"Case #"<<T<<": ";
		if (i==n.size()-1) {
			cout<<n;
		} else {
			if (n[i]=='1') {
				for (int j = 0; j < i; ++j) {
					cout<<9;
				}
			} else {
				while(n[i]==n[i-1]) i--;
				for (int j = 0; j < i; ++j) {
					cout<<(n[j]-'0');
				}
				cout<<(n[i]-'0'-1);
			}
			for (int j = i+1; j < n.size(); ++j) {
				cout<<9;
			}
		}
		cout<<"\n";
	}
}
