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


int memo[4][101][101][101];

int solve(int resto, int P, int uno, int dos, int tres){
	if(uno+dos+tres==0)return 0;
	if(memo[resto][uno][dos][tres]!=-1)return memo[resto][uno][dos][tres];
	int act = 0;
	if(uno){
		act = max(act, solve((resto-1+P)%P,P,uno-1,dos,tres));
	}
	if(dos){
		act = max(act, solve((resto-2+P)%P,P,uno,dos-1,tres));
	}
	if(tres){
		act = max(act, solve((resto-3+P)%P,P,uno,dos,tres-1));
	}
	if(resto==0)act++;
	memo[resto][uno][dos][tres] = act;
	return memo[resto][uno][dos][tres];
}

int main(){
	int T;
	cin >> T;
	for(int caso=1; caso<=T; caso++){
		int N, P, Gs[105];
		memset(memo, -1, sizeof memo);
		cin >> N >> P;
		int mods[5] = {0};
		for(int i=0; i<N; i++){
			cin >> Gs[i];
			mods[Gs[i]%P]++;
		}
		int res = mods[0];
		res += solve(0, P, mods[1], mods[2], mods[3]);
		cout << "Case #" << caso << ": " << res << endl;
	}
	return 0;
}
