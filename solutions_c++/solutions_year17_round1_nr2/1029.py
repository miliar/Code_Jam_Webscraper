#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<int, int> ii;

int T, r[111], n, p, mi[111][111], ma[111][111], qnt[111][111], mt[111][111];
vector<ii> pairs[111];

int inter(int a, int b, int c, int d){
	return !((b<c)||(d<a));
}

int main(){
	scanf("%d", &T);
	for(int cas=1; cas<=T; cas++){
		scanf("%d %d", &n, &p);
		for(int i=0; i<n; i++){
			scanf("%d", &r[i]);
			pairs[i].clear();
		}
		for(int i=0; i<n; i++){
			for(int j=0; j<p; j++){
				scanf("%d", &qnt[i][j]);	
				ma[i][j] = (int)floor((double)qnt[i][j]/(0.9*r[i]));
				mi[i][j] = (int)ceil((double)qnt[i][j]/(1.1*r[i]));
				//printf("(%d, %d) ", mi[i][j], ma[i][j]);
				pairs[i].push_back(ii(mi[i][j], ma[i][j]));		
			}		
			//printf("\n");
		}
		for(int i=0; i<n; i++){
			sort(pairs[i].begin(), pairs[i].end());
		}
		int pos[55], ans=0;
		memset(mt, 0, sizeof(mt));
		for(int g=0; g<p; g++){
			int mii = pairs[0][g].first, maa = pairs[0][g].second;
			if(mii>maa) continue;
			memset(pos, -1, sizeof(pos));
			int cnt=0;			
			for(int i=1; i<n; i++){
				for(int j=0; j<p; j++){
					if(!mt[i][j]&&(pairs[i][j].first<= pairs[i][j].second) && inter(mii, maa, pairs[i][j].first, pairs[i][j].second)){
						pos[i] = j;
						cnt++;
						break;
					}
				}
			}
			if(cnt==n-1){
				mt[0][g] = 1;				
				for(int i=1; i<n; i++){
					mt[i][pos[i]] = 1;
				}
				ans++;
			}
		}
		printf("Case #%d: %d\n", cas, ans);
		
	}
	return 0;
}
