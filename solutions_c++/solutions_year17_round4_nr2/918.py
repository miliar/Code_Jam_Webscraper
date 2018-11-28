#include <bits/stdc++.h>
using namespace std;

int f[1005], e[1005];
int n,m,c,tc;
int fc, ec;
int mx[1005], my[1005];
int vs[1005];

int aug ( int x ){
	if ( vs[x] ) return 0;
	vs[x] = 1;
	
	for ( int i = 0; i < ec; i++ ){
		if ( f[x] != e[i] ){
			if ( my[i] == -1 || aug(my[i]) ){
				mx[x] = i;
				my[i] = x;
				return 1;
			}
		}
	}
	return 0;
}

void solve(){
	for ( int i = 0; i < fc; i++ ) mx[i] = -1;
	for ( int i = 0; i < ec; i++ ) my[i] = -1;
	
	int res = 0;
	int tot = 0;
	int cnt = 0;
	for ( int i = 0; i < fc; i++ ){
		if ( mx[i] == -1 ){
			memset(vs,0,sizeof(vs));
			if ( aug(i) ){
				res++;
			} else {
				if ( f[i] == 1 ) res++;
				else cnt++;
			}
		}
	}
	
	for ( int i = 0; i < ec; i++ ){
		if ( my[i] == -1 ){
			if ( e[i] == 1 ) res++;
			else {
				if ( cnt > 0 ) {
					res++;
					cnt--;
					tot++;
				} else {
					res++;
				}
			}
		}
	}
	
	res += cnt;
	printf(" %d %d",res,tot);
}

int main(){
	
	freopen("out.txt","w",stdout);
	scanf("%d",&tc);
	for ( int t = 1; t <= tc; t++){
		scanf("%d%d%d",&n,&c,&m);
		fc = ec = 0;
		
		for ( int i = 0; i < m; i++ ){
			int x,y; 
			scanf("%d%d",&x,&y);
			if ( y == 1 ) f[fc++] = x;
			else e[ec++] = x;
		}
		
		sort(f,f+fc);
		sort(e,e+ec);
		
		printf("Case #%d:",t);
		solve();
		printf("\n");
	}	
		
	fclose(stdout);
	return 0;
}
