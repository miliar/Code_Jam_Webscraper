#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#define LL long long
#define eps 1e-8
#define mem(a,b) memset(a,b,sizeof(a))
#define zero(x) ((x > +eps) - (x < -eps))
#define MAX 100010
#define INF 100000000
#define MAXEDGE 50010
#define MAX 2100
using namespace std;
//freopen("", "r", stdin);
//freopen("", "w", stdout);
//printf("Case #%d: ", ii);

int color[6];
char str[1010], ans[1010];
map<int, char> mp;
priority_queue<pair<int, char> > q;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	int d, n;
	pair<int, char> temp, newd, sp;
	scanf("%d", &T);
	for (int ii = 1; ii <= T; ii++){
		scanf("%d", &n);
		int all = 0;
		for (int i = 0; i < 6; i++){
			scanf("%d", &color[i]);
			all += color[i];
		}
		while (!q.empty()){
			q.pop();
		}
		if (color[1] > color[4] + 1 || color[3] > color[0] + 1 || color[5] > color[2] + 1){
			printf("Case #%d: IMPOSSIBLE\n", ii);
			continue;
		}
		if (color[0] != 0 && color[0] == color[3]){
			if (all - color[0] - color[3] != 0){
				printf("Case #%d: IMPOSSIBLE\n", ii);
				continue;
			}
			for (int i = 0; i < color[0]; i++){
				ans[2 * i] = 'R';
				ans[2 * i + 1] = 'G';
			}
			ans[2 * color[0]] = '\0';
			printf("Case #%d: %s\n", ii, ans);
			continue;
		}
		if (color[2] != 0 && color[2] == color[5]){
			if (all - color[2] - color[5] != 0){
				printf("Case #%d: IMPOSSIBLE\n", ii);
				continue;
			}
			for (int i = 0; i < color[2]; i++){
				ans[2 * i] = 'Y';
				ans[2 * i + 1] = 'V';
			}
			ans[2 * color[2]] = '\0';
			printf("Case #%d: %s\n", ii, ans);
			continue;
		}
		if (color[4] != 0 && color[4] == color[1]){
			if (all - color[1] - color[4] != 0){
				printf("Case #%d: IMPOSSIBLE\n", ii);
				continue;
			}
			for (int i = 0; i < color[1]; i++){
				ans[2 * i] = 'B';
				ans[2 * i + 1] = 'O';
			}
			ans[2 * color[1]] = '\0';
			printf("Case #%d: %s\n", ii, ans);
			continue;
		}
		int sum = 0;
		temp.first = color[0] - color[3];
		temp.second = 'R';
		sum += temp.first;
		q.push(temp);
		temp.first = color[2] - color[5];
		temp.second = 'Y';
		sum += temp.first;
		q.push(temp);
		temp.first = color[4] - color[1];
		temp.second = 'B';
		sum += temp.first;
		q.push(temp);
		temp = q.top();
		q.pop();
		newd = q.top();
		q.pop();
		if (temp.first > newd.first + q.top().first){
			printf("Case #%d: IMPOSSIBLE\n", ii);
			continue;
		}
		mp[3] = temp.second;
		temp.second = 3;
		mp[2] = newd.second;
		newd.second = 2;
		sp = q.top();
		q.pop();
		mp[1] = sp.second;
		sp.second = 1;
		q.push(temp);
		q.push(newd);
		q.push(sp);
		for (int i = 0; i < sum; i++){
			temp = q.top();
			q.pop();
			if (i > 0 && str[i - 1] == mp[temp.second]){
				if (!q.empty()){
					newd = q.top();
					q.pop();
					q.push(temp);
					temp = newd;
				}
				else{
					printf("error\n");
				}
			}
			str[i] = mp[temp.second];
			temp.first--;
			if (temp.first > 0){
				q.push(temp);
			}
		}
		if (str[sum - 1] == str[0]){
			swap(str[sum - 2], str[sum - 1]);
			if (str[sum - 2] == str[sum - 3] || str[sum - 1] == str[0]){
				printf("error.\n");
			}
		}
		for (int i = 1; i < sum; i++){
			if (str[i] == str[i - 1]){
				printf("error.\n");
			}
		}
		if (str[0] == str[sum - 1]){
			printf("error.\n");
		}
		str[sum] = '\0';
		int cnt = 0, idx = 0;
		for (; idx < sum; idx++){
			if (str[idx] == 'B'){
				for (int i = 0; i < color[1]; i++){
					ans[cnt++] = 'B';
					ans[cnt++] = 'O';
				}
				ans[cnt++] = 'B';
				idx++;
				break;
			}
			ans[cnt++] = str[idx];
		}
		for (; idx < sum; idx++){
			ans[cnt++] = str[idx];
		}
		strcpy(str, ans);
		sum = cnt;
		idx = 0;
		cnt = 0;
		for (; idx < sum; idx++){
			if (str[idx] == 'R'){
				for (int i = 0; i < color[3]; i++){
					ans[cnt++] = 'R';
					ans[cnt++] = 'G';
				}
				ans[cnt++] = 'R';
				idx++;
				break;
			}
			ans[cnt++] = str[idx];
		}
		for (; idx < sum; idx++){
			ans[cnt++] = str[idx];
		}
		strcpy(str, ans);
		sum = cnt;
		idx = 0;
		cnt = 0;
		for (; idx < sum; idx++){
			if (str[idx] == 'Y'){
				for (int i = 0; i < color[5]; i++){
					ans[cnt++] = 'Y';
					ans[cnt++] = 'V';
				}
				ans[cnt++] = 'Y';
				idx++;
				break;
			}
			ans[cnt++] = str[idx];
		}
		for (; idx < sum; idx++){
			ans[cnt++] = str[idx];
		}
		ans[cnt] = '\0';
		for (int i = 1; i < cnt; i++){
			if (ans[i] == ans[i - 1]){
				printf("error.\n");
			}
		}
		if (ans[0] == ans[cnt - 1]){
			printf("error.\n");
		}
		printf("Case #%d: %s\n", ii, ans);
	}
	return 0;
}