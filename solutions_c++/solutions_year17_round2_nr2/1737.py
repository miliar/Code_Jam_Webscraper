#include <cstdio>
#include <iostream>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
using namespace std;

int T, x, C;
int N, R, O, Y, G, B, V;
int BC, RC, YC;
char S[1001];

void put(char c, int i) {
	S[i] = c;
	if(c == 'R') R--;
	else if(c == 'O') O--;
	else if(c == 'Y') Y--;
	else if(c == 'G') G--;
	else if(c == 'B') B--;
	else if(c == 'V') V--;
}

bool check(char c, int i) {
//	printf("check %c %d\n", c, i);
	if(i != N) {
		if(c == 'R' && R == 0) return false;
		if(c == 'G' && G == 0) return false;
		if(c == 'V' && V == 0) return false;
		if(c == 'B' && B == 0) return false;
		if(c == 'Y' && Y == 0) return false;
		if(c == 'O' && O == 0) return false;
	}
	if(i == 0) {
		S[1000] = c;
		return true;
	}
	char p = S[i-1];
	if((p == 'R' || p == 'O' || p == 'V') && (c == 'R' || c == 'O' || c == 'V')) return false; 
	if((p == 'Y' || p == 'O' || p == 'G') && (c == 'Y' || c == 'O' || c == 'G')) return false; 
	if((p == 'B' || p == 'G' || p == 'V') && (c == 'B' || c == 'G' || c == 'V')) return false; 
	S[1000] = c;
	return true;
}

void solve() {
	if(V != 0 && O != 0 && V + O >= N/2) printf("IMPOSSIBLE\n");
	else if(V != 0 && G != 0 && V + G >= N/2) printf("IMPOSSIBLE\n");
	else if(G != 0 && O != 0 && G + O >= N/2) printf("IMPOSSIBLE\n");
	else if(B + G + V > N/2) printf("IMPOSSIBLE\n");
	else if(Y + O + G > N/2) printf("IMPOSSIBLE\n");
	else if(R + O + V > N/2) printf("IMPOSSIBLE\n");
	else {
		char p = 'B';
		if(RC > BC && RC > YC) p = 'R';
		if(YC > RC && YC > BC) p = 'Y';
		S[1000] = p;
		for(int i = 0 ; i < N ; ++i) {
			if(S[1000] == 'B') {
				char p1 = RC > YC ? 'R' : 'Y';
				char p2 = p1 == 'R' ? 'Y' : 'R';
				if(check('O', i)) put('O', i);
				else if(check(p1, i)) put(p1, i);
				else if(check(p2, i)) put(p2, i);
				else {
					printf("IMPOSSIBLE\n");
					return ;
				}
			} else if(S[1000] == 'R') {
				char p1 = YC > BC ? 'Y' : 'B';
				char p2 = p1 == 'Y' ? 'B' : 'Y';
				if(check('G', i)) put('G', i);
				else if(check(p1, i)) put(p1, i);
				else if(check(p2, i)) put(p2, i);
				else {
					printf("IMPOSSIBLE\n");
					return ;
				}
			} else if(S[1000] == 'Y') {
				char p1 = BC > RC ? 'B' : 'R';
				char p2 = p1 == 'B' ? 'R' : 'B';
				if(check('V', i)) put('V', i);
				else if(check(p1, i)) put(p1, i);
				else if(check(p2, i)) put(p2, i);
				else {
					printf("IMPOSSIBLE\n");
					return ;
				}
			} else if(S[1000] == 'O') {
				if(check('B', i)) put('B', i);
				else {
					printf("IMPOSSIBLE\n");
					return ;
				}
			} else if(S[1000] == 'G') {
				if(check('R', i)) put('R', i);
				else {
					printf("IMPOSSIBLE\n");
					return ;
				}
			} else if(S[1000] == 'V') {
				if(check('Y', i)) put('Y', i);
				else {
					printf("IMPOSSIBLE\n");
					return ;
				}
			} else {
				printf("IMPOSSIBLE\n");
				return ;
			}
			if(S[1000] == 'R') RC--;
			else if(S[1000] == 'B') BC--;
			else if(S[1000] == 'Y') YC--;
			else if(S[1000] == 'O') { RC--; YC--; }
			else if(S[1000] == 'G') { YC--; BC--; }
			else if(S[1000] == 'V') { RC--; BC--; }
			
//			for(int j = 0 ; j< N ; ++j) printf("%c", S[j]);
//			printf("\n");
		}
		if(!check(S[0], N)) {
			printf("IMPOSSIBLE\n");
			return ;
		}
		for(int i = 0 ; i < N ; ++i) printf("%c", S[i]);
		printf("\n");
	}
}

int main() {
	scanf("%d", &T);
	while (T--) {
		scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
//		printf("R O Y G B V\n");
//		printf("%d %d %d %d %d %d\n", R, O, Y, G, B, V);
		BC = B + G + V;
		RC = R + O + V;
		YC = Y + G + O;
		printf("Case #%d: ", ++C);
		solve();
	}
}
