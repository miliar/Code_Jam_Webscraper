#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;
int T, n, p;
int r[55];
int q[55][55];
int cmp(const int & a,const int & b){
	return a > b;
}
int rem[55], tmp[55];
int main(){
	//		freopen("in.txt", "r", stdin);
	//		freopen("out.txt", "w", stdout);
	scanf("%d",&T);
	for (int tt = 1; tt <= T; tt++){
		scanf("%d %d\n", &n, &p);
		for (int i = 1; i <= n; i++)
			scanf("%d", &r[i]);
		//		if (tt == 25) fprintf(stderr, "%d\n", r[1]);

		for (int i = 1; i <= n; i++){
			for (int j = 1; j <= p; j++)
				scanf("%d", &q[i][j]);
			sort(q[i] + 1, q[i] + p + 1, cmp);
		}
		for (int i = 1; i <= n; i++)
			rem[i] = 1;
		int ans = 0;
		for (int i = 1000000; i >= 1; i--){
			int flag = 1;
			for (int j = 1; j <= n; j++){
				double least = 0.9 * i * r[j];
				double most = 1.1 * i * r[j];
				tmp[j] = rem[j];
				if (tmp[j] > p) {flag = 0; break;}
				//if (tt == 25) fprintf(stderr, "!!%d %d %f\n", tmp[j], q[j][tmp[j]], most);
				while (q[j][tmp[j]] > most && tmp[j] <= p) tmp[j]++;
				//if (tt == 25) fprintf(stderr, "%d %d\n", tmp[j], q[j][tmp[j]]);
				if (q[j][tmp[j]] < least || tmp[j] > p){
					flag = 0;break;
				}
			}
			if (flag){
				//if (tt == 25) fprintf(stderr, "\n%d",i);
				ans++;
				for (int j = 1; j <= n; j++)
					rem[j] = tmp[j] + 1;
				i++;
			}
		}
		printf("Case #%d: ",tt);
		printf("%d\n",ans);

	}
	return 0;
}
