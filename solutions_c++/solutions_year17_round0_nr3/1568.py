#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <utility>
#include <sstream>
#include <queue>
#include <unordered_set>
#include <unordered_map>
#include <bitset>
#include <cstdint>
using namespace std;


int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++){
		int64_t num;
		int64_t k;
		cin >> num >> k;
		cerr << num << endl;
		unordered_map <int64_t, int64_t> mp;
		queue <int64_t> qu;
		qu.push(num);
		mp[num] = 1;
		int64_t ans1 = -1;
		int64_t ans2 = -1;
		while (k > 0 && !qu.empty()){
			int64_t cur, h1, h2;
			cur = qu.front(); qu.pop();
			
			k -= mp[cur];	
			h1 = h2 = (cur-1) / 2;
			if ((cur - 1) % 2) h1++;
			ans1 = h1; ans2 = h2;
			
			if (h1 != 0){
				if (mp.find(h1) == mp.end()){
					mp[h1] = mp[cur];
					qu.push(h1);
				}
				else mp[h1] += mp[cur];
			}

			if (h2 != 0){
				if (mp.find(h2) == mp.end()){
					mp[h2] = mp[cur];
					qu.push(h2);
				}
				else mp[h2] += mp[cur];
			}

			mp.erase(cur);
		}
		cout << "Case #" << z << ": " << max(ans1, ans2) << " " << min(ans1, ans2) << endl;
	}
	
	return 0;
}