#include <bits/stdc++.h>

//LIFE IS NOT A PROBLEM TO BE SOLVED

using namespace std;

#define rep(i,a,b) for(int i = int(a); i < int(b) ; i++)
#define pb push_back
#define mp make_pair
#define F first
#define S second

typedef long long int ll;
typedef unsigned long long int ull;
typedef pair < int, int > ii;
typedef pair < ii, ii > iii;
typedef pair < int, iii > iiii;

const int INF = 0x3f3f3f3f;
const ll LINF = 1LL<<58;

int N, R, O, Y, G, B, V, yep, inicio;
map<iiii, int> pd;
map<iiii, int> save;

int solve(int i, int r, int y, int b, int l){
	
	if(yep) return 1;
	if(i==N){
		if(l==1) return inicio==1?yep=0:yep=1;
		if(l==2) return inicio==2?yep=0:yep=1;
		if(l==3) return inicio==3?yep=0:yep=1;
	}
	
	iiii aux=mp(i, mp(mp(r, y), mp(b, l)));
	if(pd.count(aux)) return pd[aux];
	
	int ret=0;
	if(l==1){
		if(y){
			int cmp=solve(i+1, r, y-1, b, 2);
			if(cmp>ret){
				ret=cmp;
				save[aux]=2;	
			}
		}
		if(b){
			int cmp=solve(i+1, r, y, b-1, 3);
			if(cmp>ret){
				ret=cmp;
				save[aux]=3;
			}
		}
	}
	if(l==2){
		if(r){
			int cmp=solve(i+1, r-1, y, b, 1);
			if(cmp>ret){
				ret=cmp;
				save[aux]=1;
			}
		}
		if(b){
			int cmp=solve(i+1, r, y, b-1, 3);
			if(cmp>ret){
				ret=cmp;
				save[aux]=3;
			}
		}
	}
	if(l==3){
		if(r){
			int cmp=solve(i+1, r-1, y, b, 1);
			if(cmp>ret){
				ret=cmp;
				save[aux]=1;
			}
		}
		if(y){
			int cmp=solve(i+1, r, y-1, b, 2);
			if(cmp>ret){
				ret=cmp;
				save[aux]=2;
			}
		} 
	}
	
	return pd[aux]=ret;
	
}


void rec(int i, int r, int y, int b, int l){
	if(i==N) return;
	
	iiii aux=mp(i, mp(mp(r, y), mp(b, l)));
	int go=save[aux];
	
	if(go==1){
		printf("R");
		rec(i+1, r-1, y, b, 1);
	}
	
	if(go==2){
		printf("Y");
		rec(i+1, r, y-1, b, 2);
	}
	
	if(go==3){
		printf("B");
		rec(i+1, r, y, b-1, 3);
	}
	
}

bool my_comp(ii a, ii b){
	if(a.F>b.F) return true;
	return false;
}

int main(){

	
	int T; cin >> T;
	
	rep(z, 1, T+1){
		
		//scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
		ii vet[3];
		scanf("%d %d %d %d %d %d %d", &N, &vet[0].F, &O, &vet[1].F, &G, &vet[2].F, &V);
		vet[0].S=1, vet[1].S=2, vet[2].S=3;
		sort(vet, vet+3, my_comp);
		
		printf("Case #%d: ", z);
		
		if(vet[1].F+vet[2].F<vet[0].F){
			puts("IMPOSSIBLE");
			continue;
		}
		
		int last=vet[0].S, ini=last; vet[0].F--;
		if(last==1) printf("R");
		if(last==2) printf("Y");
		if(last==3) printf("B");
		
		rep(i, 1, N-2){
			sort(vet, vet+3, my_comp);
			
			if(vet[0].S==last) last=vet[1].S, vet[1].F--;
			else last=vet[0].S, vet[0].F--;
			
			if(last==1) printf("R");
			if(last==2) printf("Y");
			if(last==3) printf("B");
		}
		
		sort(vet, vet+3, my_comp);
		
		if(vet[0].S==ini) last=vet[0].S, vet[0].F--;
		else last=vet[1].S, vet[1].F--;
		
		if(last==1) printf("R");
		if(last==2) printf("Y");
		if(last==3) printf("B");
		
		sort(vet, vet+3, my_comp);
		
		last=vet[0].S, vet[0].F--;
		if(last==1) printf("R");
		if(last==2) printf("Y");
		if(last==3) printf("B");
		
		printf("\n");
		
		
		
		
		
		
		
		/*printf("Case #%d: ", z);
		
		int v[3]; v[0]=R, v[1]=Y, v[2]=B; sort(v, v+3);
		if(v[0]+v[1]<v[2]){
			puts("IMPOSSIBLE");
			continue;
		}
		
		yep=0; pd.clear();
		
		if(R){
			inicio=1;
			if(solve(1, R-1, Y, B, 1)){
				printf("R");
				rec(1, R-1, Y, B, 1);
				printf("\n");
			}else{
				puts("IMPOSSIBLE");
			}
		}
		
		else if(Y){
			inicio=2;
			if(solve(1, R, Y-1, B, 2)){
				printf("Y");
				rec(1, R, Y-1, B, 2);
				printf("\n");
			}else{
				puts("IMPOSSIBLE");
			}
		}
		
		else if(B){
			inicio=3;
			if(solve(1, R, Y, B-1, 3)){
				printf("B");
				rec(1, R, Y, B-1, 3);
				printf("\n");
			}else{
				puts("IMPOSSIBLE");
			}
		}
		
		cout << pd.size() << '\n';*/
		
		
	}

	return 0;
	
}
