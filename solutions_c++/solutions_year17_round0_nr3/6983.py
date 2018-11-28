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

bool ck[2000];


int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t){
		for (int i = 0; i < 2000; ++i){
			ck[i] = false;
		}
		int n, k;
		cin >> n >> k;
		int ans1 = 0, ans2 = INF;
		vector <pair<int, int> > a;
		a.push_back({ 0, n - 1 });
		for (int i = 0; i < k; ++i){
			int t = 0;
			int x = 0;
			for (int j = 0; j < a.size(); ++j){
				if (ck[j])continue;
				if (a[j].second - a[j].first + 1 > t || (a[j].second - a[j].first + 1 == t && a[j].first < a[x].first)){
					x = j;
					t = a[j].second - a[j].first + 1;
				}
			}
			ck[x] = true;
			if (i == k - 1){
				ans1 = a[x].second - ((a[x].first + a[x].second) / 2 + 1) + 1;
				ans2 = (a[x].first + a[x].second) / 2 - 1 - a[x].first + 1;
			}
			else{
				a.push_back({ a[x].first, (a[x].first + a[x].second) / 2 - 1 });
				a.push_back({ (a[x].first + a[x].second) / 2 + 1, a[x].second });
			}
		}
		cout << "Case #" << t + 1 << ": " << ans1 << " " << ans2 << "\n";
	}
	return 0;
}