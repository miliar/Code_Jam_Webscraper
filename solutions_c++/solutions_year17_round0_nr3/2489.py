										/* in the name of Allah */
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

#define uint unsigned int
#define int64 long long
#define P pair<int, int>
#define Pss pair<string, string>
#define PLL pair<int64, int64>
#define Inf 1000000
#define Mod 1000000007LL

int64 n, k;
priority_queue <int64> q;
map <int64, int64> mp;

int main(){
	std::ios::sync_with_stdio(false);
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int T, test = 0;
	for(cin >> T; T--; ){
		cin >> n >> k;
		mp.clear();
		while(!q.empty())
			q.pop();

		mp[n] = 1;
		q.push(n);
		while(k > mp[q.top()]){
			int64 value = q.top();
			q.pop();

			int64 cnt = mp[value];
			k -= cnt;
			
			for(int i = 0; i <= 1; i++){
				int64 tmp = (value - i) / 2;
				if(mp[tmp] == 0)
					q.push(tmp);
				mp[tmp] += cnt;
			}
		}

		int64 ans = q.top();
		cout << "Case #" << ++test << ": " << ans / 2 << ' ' << (ans - 1) / 2 << endl;
	}
	return 0;
}
