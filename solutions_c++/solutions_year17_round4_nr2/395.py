#include<bits/stdc++.h>
using namespace std;
const int N = 100000;
int p[100000], b[100000], num[100000], flag[100000];
int main(){
	freopen("bb.in","r", stdin);
	freopen("bbb.out","w",  stdout);
	int T,n,c,m;
	cin>>T;
	for(int ii = 1; ii <= T; ii++){
		cin>>n>>c>>m;
		for(int i = 0; i <= c; i++)
			num[i] = 0;
		for(int i = 0; i <= n; i++)
			flag[i] = 0;
		for(int i = 1; i <= m; i++){
			scanf("%d%d", &p[i], &b[i]);
			num[b[i]]++;
			flag[p[i]]++;
		}
		int ans = 0;
		for(int i = 1; i <= c; i++)
			ans = max(ans, num[i]);
		for(int i = 1; i <= n; i++){
			int sum = 0;
			for(int j = 1; j <= m; j++)
				if(p[j] <= i) sum++;
			ans = max(ans, (sum + i - 1) / i);
		}
		int sum = 0;
		for(int i = 1; i <= n; i++)
			if(flag[i] > ans) sum += flag[i] - ans;
		printf("Case #%d: %d %d\n",ii,ans, sum);
	}
}