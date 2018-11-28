#include <bits/stdc++.h>
using namespace std;
int falta[4];
int sobra[4];
void solve(int tc) {
	printf("Case #%d: ", tc);
	int n, m, x;
	scanf("%d %d", &n, &m);
	for(int i = 0; i < 4; ++i)falta[i] = sobra[i] = 0;
	int ans = 0;
	int need = 0;
	for(int i = 0; i < n; ++i) {
		scanf("%d", &x);
		if(x%m == 0)++ans;
		else if(x < m){
			sobra[m-x]++;
			++need;
		}else {
			int k = 0;
			while(x%m != 0)--x, ++k;
			falta[k]++;
			++need;
		}
	}
	if(m == 2){
		int mi = min(falta[1], sobra[1]);
		falta[1]-=mi;
		ans+=mi;
		ans+=(falta[1]+1)/2;
		printf("%d\n", ans);
		return;
	}
	for(int i = 0; i < 4; ++i){
		int mi = min(falta[i], sobra[i]);
		ans+=mi;
		falta[i]-=mi;
		sobra[i]-=mi;
		need-=mi*2;
	}
	for(int i = 0; i < 4; ++i){
		if(falta[i] && falta [m-i]){
			int mi = min(falta[i], falta[m-i]);
			falta[i]-=mi;
			falta[m-i]-=mi;
			ans+=mi;
			need-=mi*2;
		}
	}
	ans+=(falta[1]+2)/3;
	ans+=(falta[2]+2)/3;
	ans+=(sobra[1]+2)/3;
	ans+=(sobra[2]+2)/3;
	printf("%d\n", ans);

}	

int main() {
	int tc;
	scanf("%d", &tc);
	for(int i = 1; i <= tc; ++i){
		solve(i);
	}
	return 0;
}