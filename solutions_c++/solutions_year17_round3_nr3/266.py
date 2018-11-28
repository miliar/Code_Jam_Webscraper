#include <bits/stdc++.h>
using namespace std;

int get_int(char *s) {
	int len = strlen(s);
	int ret = 0;
	int i;
	for (i = 0; i < len; i++) {
		if (s[i] != '.')
			ret = 10*ret + s[i] - '0';	
	}	
	return ret;
}

int main() {
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T, kase = 0;
	scanf("%d",&T);
	while (T--) {
		int n, k;
		scanf("%d%d",&n,&k);
		char s[10];
		scanf("%s",s);
		int tot = get_int(s);
		priority_queue<int,vector<int>,greater<int> > pq;
		for (int i = 1; i <= n; i++) {
			scanf("%s",s);
			int v = get_int(s);
			if (v < 10000) {
				pq.push(v);	
			}
		}
		while (tot) {
			int v = pq.top();
			if (v >= 10000) break;
			pq.pop();
			tot--;
			v++;
			pq.push(v);
		}
		double p = 1.0;
		while (!pq.empty()) {
			p = p * 0.0001 * pq.top();
			pq.pop();
		}
		printf("Case #%d: %.6f\n",++kase,p);
	}
	return 0;
}
