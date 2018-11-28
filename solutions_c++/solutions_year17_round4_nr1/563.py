
#include<bits/stdc++.h>
#define all(x) x.begin(), x.end()
#define pb(x) push_back(x)
#define cout2(x, y) cout << x << " " << y << endl
#define N 100005

using namespace std;

int frec[5], p;
char memo[101][101][101];

int DP(int c1, int c2, int c3, int r){
	
	if(c1 == 0 && c2 == 0 && c3 == 0)return 0;
	
	char &ret = memo[c1][c2][c3];
	if(ret != -1)return ret;
	
	int ans = 0;
	if(r == 0){
		
		if(c1 > 0)ans = max(ans, DP(c1 - 1, c2, c3, (p - (1 - r)%p)%p));
		if(c2 > 0)ans = max(ans, DP(c1, c2 - 1, c3, (p - (2 - r)%p)%p));
		if(c3 > 0)ans = max(ans, DP(c1, c2, c3 - 1, (p - (3 - r)%p)%p));
		ans++;
	}
	else{
			
		if(c1 > 0)ans = max(ans, DP(c1 - 1, c2, c3, (p - (1 - r)%p)%p));
		if(c2 > 0)ans = max(ans, DP(c1, c2 - 1, c3, (p - (2 - r)%p)%p));
		if(c3 > 0)ans = max(ans, DP(c1, c2, c3 - 1, (p - (3 - r)%p)%p));
	}
	
	return ret = ans;
}


int main(){

	int tc = 0, caso = 1;
	scanf("%d", &tc);
	
	while(tc--){
		
		int n, x;
		scanf("%d%d", &n, &p);
		
		memset(frec, 0, sizeof frec);
		for(int i = 0 ; i < n; i++)scanf("%d", &x), frec[x%p]++;
		
		int ans = frec[0];
		memset(memo, -1, sizeof memo);
		
		ans += DP(frec[1], frec[2], frec[3], 0);
		
		printf("Case #%d: %d\n", caso++, ans);
	}


}

