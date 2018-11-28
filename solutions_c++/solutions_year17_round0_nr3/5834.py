#include<bits/stdc++.h>

using namespace std;

long long t, n, k, ls, rs, l, r;
long long niz[2000] = {0};

long long trazilijevo(int x){
	x--;
	while(niz[x] == 0) x--;
	return x;
}

long long trazidesno(int x){
	x++;
	while(niz[x] == 0) x++;
	return x;	
}

int main(){
	scanf("%d", &t);
	for (long long c = 1; c <= t; c++) {
		scanf("%d %d", &n, &k);
		memset(niz, 0, n + 5);
		for (long long j = 0; j <= n + 1; j++) niz[j] = 0;
		niz[0] = 1;
		niz[n + 1] = 1;
		for (long long i = 0; i < k; i++){
			long long best = -1;
			ls = -1; 
			rs = -1;
			long long bestpos = -1;
			for (long long j = 1; j <= n; j++){
				if (niz[j] == 0) {
					l = j - trazilijevo(j) - 1;
					r = trazidesno(j) - j - 1;
					//cout << "Probana pozicija " << j << " L: " << l << " R: " << r << endl;
					if (best < min(l, r) || best == min(l, r) && (max(l, r) > max(ls, rs) ) ) {
						ls = l;
						rs = r;
						best = min(l, r);
						bestpos = j;
						//cout << "Popravak pos:" << bestpos << " Ls: " << ls << " Rs: " << rs << ' ' << best << endl;
					}
				}
			}
			//cout << "Sjeo na " << best << " Ls: " << ls << " Rs: " << rs <<endl;
			niz[bestpos] = 1;
		/*	for (long long j = 0; j <= n + 1; j++) cout << niz[j] << ' ';
			cout << endl;*/
		}
		printf("Case #%d: %d %d\n", c, max(ls, rs), min(ls, rs));
	}	
	return 0;
}
