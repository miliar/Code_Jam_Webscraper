#include <bits/stdc++.h>
using namespace std;
int tcs, n, p, g[55], q[55][55], idx[55], ans;
vector<int> svs;
int main(){
	scanf("%i", &tcs);
	for(int tc=1;tc<=tcs;tc++){
		svs.clear();
		memset(idx, 0, sizeof idx);
		scanf("%i%i", &n, &p);
		for(int i=0;i<n;i++){
			scanf("%i", &g[i]);
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<p;j++){
				scanf("%i", &q[i][j]);
			}
			sort(q[i], q[i] + p);
		}
		ans = 0;
		for(int k=0;k<p;k++){ //for the k-th 0 item, we search 0.9 but less than 1.1
			bool ok = false;
			//check if we can even make servings from this
			int svl = round(((double)q[0][k] / 1.1f) / g[0]), svu = round(((double)q[0][k] / 0.9f) / g[0]), sva = round(((double)q[0][k]) / g[0]);
			//printf("%i - %i\n", svl, svu);
			ok = (q[0][k] >= sva * (g[0]) * 0.9f && q[0][k] <= sva * g[0] * 1.1f);
			if(!ok) continue;
			ok = false;
			//printf("trying to make %i-%i\n", svl, svu);
			for(int i=1;i<n;i++){
				for(int j=0;j<p;j++){
					for(int sv=svl;sv<=svu;sv++){
						//printf("%i pack - expecting %lf - %lf, got %i\n", sv, (double)sv * (g[i]) * 0.9f, (double)sv * g[i] * 1.1f, q[i][j]);
						if(q[i][j] >= (double)sv * (g[i]) * 0.9f && q[i][j] <= (double)sv * g[i] * 1.1f) {
							ok = true; //found match
							q[i][j] = 0;
							break;
						}
					}
					if(ok) break;
				}
				if(ok == false) break;
			}
			if(ok == false && n > 1) continue;
			ans++;
		}
		printf("Case #%i: %i\n", tc, ans);
	}
}