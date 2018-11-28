#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <string>
#include  <cstring>
#include <cstdlib>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int test = 1; test<=t; test++) {
		int r, o, y, g, b, v, n;
		//scanf("%d %d %d", &r, &y, &b);
		scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
		int sum = r+y+b;
		if(r > sum/2 || b > sum/2 || y > sum/2) {
			printf("Case #%d: IMPOSSIBLE\n", test);   
		}
		else {
			vector<char> ans;
			char last = '0';
			char first = '0';
			while(sum) {
				pair<int, char> x[] = {{r, 'R'}, {y, 'Y'}, {b, 'B'}};
				sort(x, x+3);
				reverse(x, x+3);
				pair<int, char> chosen;
				if(x[0].second != last) chosen = x[0];
				else chosen = x[1];
				
				if(first != last) {
					int aux;
					if(first == 'R') aux = r;
					else if(first == 'B') aux = b;
					else aux = y;
					if(aux == chosen.first) chosen = {aux, first};
				}
				
				ans.push_back(chosen.second);
				last = chosen.second;
				if(chosen.second == 'R') r--;
				else if(chosen.second == 'B') b--;
				else y--;
				sum--;
				
				if(ans.size() == 1) first = last;
				
			}
			if(ans[ans.size()-1] == ans[0]) {
				for(int i = 1; i<ans.size()-1; i++) {
					if(ans[i] == ans[ans.size()-1]) continue;
					if(ans[i-1] == ans[i+1] && ans[i-1] != ans[ans.size()-1]) {
						swap(ans[ans.size()-1], ans[i]);
						break;
					}
				}
			}
			printf("Case #%d: ", test);
			for(int i = 0; i<ans.size(); i++) {
				printf("%c", ans[i]);
			}
			printf("\n");
		}
	}
	return 0;
}
