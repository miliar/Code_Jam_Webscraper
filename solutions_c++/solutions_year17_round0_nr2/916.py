#include<algorithm>
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<sstream>
using namespace std;

typedef long long LL;
typedef long double LD;

#define dprintf(...) fprintf(stderr, __VA_ARGS__)

int cond = 1;
#define DB(X) {if(cond){cerr<<"Line:"<<__LINE__<<", "<<#X<<" = "<<X<<endl;}}

LL solve(LL tmp) {
	LL n;
	vector<int> d;
	n = tmp;
	if (n < 10) { return n; }
	while (n > 0) {
		d.push_back(n % 10);
		n /= 10;
	}	
	int l = d.size();
	int prev = 0;
	int i = l - 1;
	for(; i >= 0; --i) {
		if (d[i] >= prev) {
			prev = d[i];	
		}
		else {
			break;
		}
	}
	if (i < 0) {
		return tmp;
	}
	for(int j = i+1; j < l; ++j) {
		if (d[j] > 0) {
			d[j]--;
		}
		if (j < l - 1 && d[j+1] <= d[j]) {
			break;
		}
		if (j < l - 1) {
			i++;
		}
	}
	for(int j = 0; j <= i; ++j) {
		d[j] = 9;
	}
	long long r = 0;
	for(int i = l - 1; i >= 0; --i) {
		r *= 10;
		r += d[i];
	}
	return r;
}

LL solveBrut(LL n) {
	LL tmp = n;
	bool ok = true;
	while (ok) {
		vector<int> d;
		LL t = tmp--;
		while (t > 0) {
			d.push_back(t % 10);
			t /= 10;
		}
		ok = false;
		for (int i = d.size() - 2; i >= 0; --i) {
			if (d[i+1] > d[i]) {
				ok = true;
				break;
			}
		}
	}
	return tmp + 1;
}

int main() {
	int t; cin >> t;
	for(int x = 1; x <= t; ++x){
		LL n; cin >> n;
		cout << "Case #" << x << ": " << solve(n) << endl;//result 
	 }
	return 0;
}
