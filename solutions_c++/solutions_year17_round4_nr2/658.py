#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int n, m, c;

int roller, promote;

int pos_num[1010];
int ticket_num[1010];

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, a, b;
	cin >> T;
	for(int t = 1; t <= T; ++t){
		memset(pos_num, 0, sizeof(pos_num));
		memset(ticket_num, 0, sizeof(ticket_num));
		roller = 0; promote = 0;
		scanf("%d%d%d", &n, &c, &m);
		for(int i = 1; i <= m; ++i){
			scanf("%d %d", &a, &b);
			ticket_num[b]++;
			pos_num[a]++;
		}
		for(int i = 1; i <= c; ++i){
			roller = max(roller, ticket_num[i]);
		}
		int sum = 0, tmp;
		for(int i = 1; i <= n; ++i){
			sum += pos_num[i];
			tmp = (sum % i == 0) ? sum / i : sum / i + 1;
			roller = max(roller, tmp);
		}
		for(int i = 1; i <= n; ++i){
			promote += max(0, pos_num[i] - roller);
		}
		printf("Case #%d: %d %d\n", t, roller, promote);
	}
	return 0;
}
