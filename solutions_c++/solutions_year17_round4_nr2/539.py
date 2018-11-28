
#include<bits/stdc++.h>
#define all(x) x.begin(), x.end()
#define pb(x) push_back(x)
#define cout2(x, y) cout << x << " " << y << endl
#define N 1005

using namespace std;

int n, m,c;
int frec[N];
vector<int>L[N];

bool puedo(int rides){
	
	int acum = 0;
	for(int i = 1; i <= n; i++){
		
		acum += L[i].size();
		if(acum > rides * i)return false;

	}
	
	return true;
}

int main(){

	int tc = 0, caso = 1;
	scanf("%d", &tc);
	
	while(tc--){
		
		memset(frec, 0, sizeof frec);
		for(int i = 0; i <= n; i++)L[i].clear();
		
		int p, b, maxi = 0;
		scanf("%d%d%d", &n, &c, &m);
		
		for(int i = 0; i < m; i++){
			
			scanf("%d%d", &p, &b);
			L[p].pb(b);
			
			frec[b]++;
			maxi = max(maxi, frec[b]);
		}
		
		int lo = maxi, hi = m, me;
		
		while(lo < hi){
			
			me = lo + (hi - lo)/2;
			if(puedo(me))hi = me;
			else lo = me + 1;
		}
		
		int moves = 0, len;
		for(int i = 1; i <= n; i++){
			
			len = L[i].size();
			if(len > lo)moves += len - lo;
		}
		
		printf("Case #%d: %d %d\n", caso++, lo, moves);
		
	}


}

