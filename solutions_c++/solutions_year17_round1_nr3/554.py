#include <bits/stdc++.h>

//LIFE IS NOT A PROBLEM TO BE SOLVED

using namespace std;

#define rep(i,a,b) for(int i = int(a); i < int(b) ; i++)
#define pb push_back
#define mp make_pair
#define F first
#define S second

typedef pair < int, int > ii;
typedef pair < ii, ii > iii;
typedef pair < iii, int > iiii;

int Hd, Ad, Hk, Ak, B, D;


void solve(){
	
	queue <iiii> q; iiii aux; iii go;
	aux.F.F.F=Hd, aux.F.F.S=Hk, aux.F.S.F=Ad, aux.F.S.S=Ak, aux.S=0;
	set <iii> vis; go=aux.F; vis.insert(go); q.push(aux);
	
	while(!q.empty()){
		iiii u=q.front(); q.pop();
		
		aux=u;
		aux.F.F.S-=aux.F.S.F;
		if(aux.F.F.S<=0){
			printf("%d\n", aux.S+1);
			return;
		}
		aux.F.F.F-=aux.F.S.S;
		if(aux.F.F.F>0){
			iii go=aux.F; aux.S++;
			if(!vis.count(go))
				vis.insert(go),
				q.push(aux);
		}
		
		aux=u;
		aux.F.S.F+=B;
		aux.F.F.F-=aux.F.S.S;
		if(aux.F.F.F>0){
			iii go=aux.F; aux.S++;
			if(!vis.count(go))
				vis.insert(go),
				q.push(aux);
		}
		
		aux=u;
		aux.F.F.F=Hd;
		aux.F.F.F-=aux.F.S.S;
		if(aux.F.F.F>0){
			iii go=aux.F; aux.S++;
			if(!vis.count(go))
				vis.insert(go),
				q.push(aux);
		}
		
		aux=u;
		aux.F.S.S-=D; if(aux.F.S.S<0) aux.F.S.S=0;
		aux.F.F.F-=aux.F.S.S;
		if(aux.F.F.F>0){
			iii go=aux.F; aux.S++;
			if(!vis.count(go))
				vis.insert(go),
				q.push(aux);
		}
		
	}
	
	puts("IMPOSSIBLE");
	return;
	
}
int main(){
	
	
	freopen("C.in", "r", stdin);
	freopen("C.sol", "w", stdout);

	int T, z=1; cin >> T;
	
	while(T--){
		
		scanf("%d %d %d %d %d %d", &Hd, &Ad, &Hk, &Ak, &B, &D);
		printf("Case #%d: ", z++);
		solve();
		
	}
	
	return 0;
	
}
