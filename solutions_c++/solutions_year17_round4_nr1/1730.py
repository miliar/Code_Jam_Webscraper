#include <bits/stdc++.h>
#define SZ(v) ((int)(v).size())
#define debug(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

int n, p, g[103];

int main(){
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++){
		printf("Case #%d: ", t);
		scanf("%d%d", &n, &p);
		for (int i=0; i<n; i++){
			scanf("%d", &g[i]);
			g[i] %= p;
		}
		if (p == 2){
			int cnt = count(g, g+n, 1);
			if (cnt == 0){
				printf("%d\n", n);
			}
			else {
				printf("%d\n", (n-cnt+1)+(cnt-1)/2);
			}
		}
		else if (p == 3){
			int cnt1 = count(g, g+n, 1);
			int cnt2 = count(g, g+n, 2);
			int cnt = n-cnt1-cnt2;
			if (cnt1 == 0 && cnt2 == 0){
				printf("%d\n", n);
			}
			else if (cnt1 == cnt2){
				printf("%d\n", cnt+cnt1);
			}
			else {
				if (cnt1 > cnt2) swap(cnt1, cnt2);
				printf("%d\n", cnt+cnt1+1+(cnt2-cnt1-1)/3);
			}
		}
	}
	return 0;
}