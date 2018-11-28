#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <deque> 
#include <set>
#include <sstream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <ctime>
using namespace std;
#define INF 2000010000

int e = 0;

long long to_i(vector <int> &x){
	long long ans = 0, t = 1;
	int s = 0;
	while (x[s] != -1)++s;
	--s;
	for (int i = 0; i <= s; ++i){
		ans += (long long)x[i] * t;
		t *= 10ll;
	}
	return ans;
}

void rec(int n, int t, vector <int> &x, vector <long long> &ans){
	if (n == 0){
		ans.push_back(to_i(x));
		return;
	}
	for (int i = t; i < 10; ++i){
		x[n - 1] = i;
		rec(n - 1, i, x, ans);
	}
}


int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	vector <int> x;
	vector <long long> ans;
	for (int i = 0; i < 20; ++i)x.push_back(-1);
	rec(18, 0, x, ans);
	sort(ans.begin(), ans.end());
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i){
		long long n;
		cin >> n;
		int l = 0, r = ans.size();
		while (r - l > 1){
			int q = (r + l) / 2;
			if (ans[q] > n){
				r = q;
			}
			else{
				l = q;
			}
		}
		int o = l;
		if (ans[r] <= n)o = r;
		cout << "Case #" << i + 1 << ": " << ans[o] << "\n";
	}
	return 0;
}