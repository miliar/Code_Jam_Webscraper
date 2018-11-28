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
#define MAX 110
#define INF 100000000
#define MAXEDGE 50010
using namespace std;
//freopen("", "r", stdin);
//freopen("", "w", stdout);
//printf("Case #%d: ", ii);
int n, c, m;
int cnt[1010][2];
priority_queue<pair<int, int> > que;

int main(){
	freopen("B-small-attempt5.in", "r", stdin);
	freopen("B-small-attempt5.out", "w", stdout);
	int T;
	int p, b;
	scanf("%d", &T);
	for (int ii = 1; ii <= T; ii++){
		scanf("%d%d%d", &n, &c, &m);
		mem(cnt, 0);
		for (int i = 0; i < m; i++){
			scanf("%d%d", &p, &b);
			b--;
			cnt[p][b] ++;
		}
		int sum, pro;
		sum = pro = 0;
		pair<int, int> temp;
		for (int i = 1; i <= n; i++){
			if (cnt[i][0]){
				for (int j = i + 1; j <= n; j++){
					if (cnt[j][0] && cnt[j][1]){
						if (cnt[i][0] > cnt[j][1]){
							sum += cnt[j][1];
							cnt[i][0] -= cnt[j][1];
							cnt[j][1] = 0;
						}
						else{
							sum += cnt[i][0];
							cnt[j][1] -= cnt[i][0];
							cnt[i][0] = 0;
						}
					}
				}
				if (cnt[i][0]){
					for (int j = i + 1; j <= n; j++){
						if (cnt[i][0] > cnt[j][1]){
							sum += cnt[j][1];
							cnt[i][0] -= cnt[j][1];
							cnt[j][1] = 0;
						}
						else{
							sum += cnt[i][0];
							cnt[j][1] -= cnt[i][0];
							cnt[i][0] = 0;
						}
					}
				}
			}
			if (cnt[i][1]){
				for (int j = i + 1; j <= n; j++){
					if (cnt[j][0] && cnt[j][1]){
						if (cnt[i][1] > cnt[j][0]){
							sum += cnt[j][0];
							cnt[i][1] -= cnt[j][0];
							cnt[j][0] = 0;
						}
						else{
							sum += cnt[i][1];
							cnt[j][0] -= cnt[i][1];
							cnt[i][1] = 0;
						}
					}
				}
				if (cnt[i][1]){
					for (int j = i + 1; j <= n; j++){
						if (cnt[i][1] > cnt[j][0]){
							sum += cnt[j][0];
							cnt[i][1] -= cnt[j][0];
							cnt[j][0] = 0;
						}
						else{
							sum += cnt[i][1];
							cnt[j][0] -= cnt[i][1];
							cnt[i][1] = 0;
						}
					}
				}
			}
			if (cnt[i][0] && !cnt[i][1]){
				sum += cnt[i][0];
				cnt[i][0] = 0;
			}
			else if (cnt[i][1] && !cnt[i][0]){
				sum += cnt[i][1];
				cnt[i][1] = 0;
			}
			else if (cnt[i][0] && cnt[i][1]){
				if (i == 1){
					sum += (cnt[i][0] + cnt[i][1]);
				}
				else{
					sum += max(cnt[i][0], cnt[i][1]);
					pro += min(cnt[i][0], cnt[i][1]);
				}
				break;
			}
		}
		printf("Case #%d: %d %d\n", ii,sum, pro);
	}
	return 0;
}