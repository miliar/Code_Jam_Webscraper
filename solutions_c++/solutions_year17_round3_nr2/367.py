#define Federico using
#define Javier namespace
#define Pousa std;
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <stack>
#include <queue>
#include <cstring>
#include <sstream>
#include <unordered_map>

Federico Javier Pousa

int As[2][1500];
int memo[2][1442][722];
#define INF 12314334;

int solve(int p, int m, int rc){
	if(m==0)return 0;
	if(memo[p][m][rc]!=-1)return memo[p][m][rc];
	if(As[p][1440-m]){
		memo[p][m][rc] = INF;
		return memo[p][m][rc];
	}
	
	if(p==0){
		memo[p][m][rc] = INF;
		if(rc)memo[p][m][rc] = min(memo[p][m][rc],solve(0, m-1, rc-1));
		if(m!=rc)memo[p][m][rc] = min(memo[p][m][rc], 1+solve(1, m-1, rc));
	}else{
		memo[p][m][rc] = INF;
		if(rc)memo[p][m][rc] = min(memo[p][m][rc], 1+solve(0,m-1,rc-1));
		if(m!=rc)memo[p][m][rc] = min(memo[p][m][rc], solve(1, m-1, rc));
	}
	return memo[p][m][rc];
}


int main(){
	int T;
	cin >> T;
	for(int caso=1; caso<=T; caso++){
		memset(memo, -1, sizeof memo);
		int Ac, Aj, aux1, aux2;		
		memset(As, 0, sizeof As);
		cin >> Ac >> Aj;
		for(int i=0; i<Ac; i++){
			cin >> aux1 >> aux2;
			for(int j=aux1; j<aux2; j++){
				As[0][j] = 1;
			}
		}
		for(int i=0; i<Aj; i++){
			cin >> aux1 >> aux2;
			for(int j=aux1; j<aux2; j++){
				As[1][j] = 1;
			}
		}
		int res = solve(0, 1440, 720);
		res = min(res, solve(1, 1440, 720));
		if(res&1)res++;
		cout << "Case #" << caso << ": " << res << endl;
	}
	
	return 0;
}
