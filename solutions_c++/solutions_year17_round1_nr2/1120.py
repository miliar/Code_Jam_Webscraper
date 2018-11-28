#include <bits/stdc++.h>

using namespace std;

#define ff first
#define ss second
#define pb push_back
#define mp make_pair



int main(){
	long long t;
	long long n,r[55],p,mark[55][55];
	vector<long long> s[55];
	set<long long> m[55][55];
	scanf("%lld",&t);
	for(long long caso = 1; caso <= t; caso++){
		scanf("%lld %lld",&n,&p);
		//printf("%lld\n",n );
		for(long long i = 0; i < n; i++){
			scanf("%lld",&r[i]);
			//printf("%lld %lld\n",i,r[i] );
		}
		for(long long i = 0; i < 50; i++){
			for(long long j = 0; j < 50; j++){
				m[i][j].clear();
				s[i].clear();
				mark[i][j] = 0;
			}
		}
		for(long long i = 0; i < n; i++){
			for(long long j = 0; j < p; j++){
				long long x;
				scanf("%lld",&x);
				s[i].pb(x);
			}
		}
		long long ans = 0;
		for(long long i = 0; i < n; i++){
			for(long long j = 0; j < p; j++){
				long long qtd1,qtd2 = s[i][j]/r[i];
				//printf("%lld %lld %lld %lld\n",s[i][j],r[i],i,n );
				qtd1 = qtd2;
				qtd2++;
				while(qtd1 * r[i] + (qtd1 * r[i])/10 >= s[i][j] && qtd1 * r[i] - (qtd1 * r[i])/10 <= s[i][j] && qtd1 > 1) qtd1--;
				while(qtd2 * r[i] + (qtd2 * r[i])/10 >= s[i][j] && qtd2 * r[i] - (qtd2 * r[i])/10 <= s[i][j]) qtd2++;
				for(long long k = qtd1; k <= qtd2; k++){
					if(k * r[i] + (k * r[i])/10 >= s[i][j] && k * r[i] - (k * r[i])/10 <= s[i][j] && k >= 1){
						m[i][j].insert(k);
						if(n == 1){
							ans++;
							break;	
						} 
						else{
							if(i == 1){
								for(int l = 0; l < p; l++){
									if(m[0][l].count(k) && !mark[0][l]){
										ans++;
										mark[0][l] = 1;
									}
								}
							}
						}
					}
				}
			}
		}
		printf("Case #%lld: %lld\n",caso,ans );
	}
	return 0;
}