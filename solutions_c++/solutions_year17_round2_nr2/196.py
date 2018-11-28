#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cassert>

using namespace std;
/*
	R
	Y
	B
	O = (R, Y) -> {B}
	G = (Y, B) -> {R}
	V = (R, B) -> {Y}
*/
int N,R,O,Y,G,B,V;
string sym[6];
inline void solve(int cas) {
	R -= G;
	Y -= V;
	B -= O;
	if(R + Y < B || R + B < Y || Y + B < R) {
		printf("Case #%d: IMPOSSIBLE\n", cas);
		return;
	}
	if(R < 0 || Y < 0 || B < 0) {
		printf("Case #%d: IMPOSSIBLE\n", cas);
		return;
	}
	if((O != 0 && B == 0 && 2 * O < N)
		|| (G != 0 && R == 0 && 2 * G < N) 
		|| (V != 0 && Y == 0 && 2 * V < N)) {
		printf("Case #%d: IMPOSSIBLE\n", cas);
		return;
	}
	printf("Case #%d: ",cas);
	if(B >= R && B >= Y) {
		for(int i = 1; i <= B; ++i) {
			if(R > 0) {
				printf("R");
				while(G > 0) {
					printf("GR");
					G--;
				}
				R--;
			}
			printf("B");
			while(O > 0) {
				printf("OB");
				O--;
			}
			if(B - i <= Y && Y > 0) {
				printf("Y");
				Y--;
				while(V > 0) {
					printf("VY");
					V--;
				}
				
			}

		}
	} else if(Y >= R && Y >= B) {
		for(int i = 1; i <= Y; ++i) {
			if(R > 0) {
				printf("R");
				while(G > 0) {
					printf("GR");
					G--;
				}
				R--;
			}
			printf("Y");
			while(V > 0) {
					printf("VY");
					V--;
			}
			
			if(Y - i <= B && B > 0) {
				printf("B");
				B--;
				while(O > 0) {
					printf("OB");
					O--;
				}
			}

		}
	} else if(R >= B && R >= Y){
		for(int i = 1; i <= R; ++i) {
			if(B > 0) {
				printf("B");
				while(O > 0) {
					printf("OB");
					O--;
				}
				B--;
			}
			printf("R");
			while(G > 0) {
					printf("GR");
					G--;
				}
			if(R - i <= Y && Y > 0) {
				printf("Y");
				Y--;
				while(V > 0) {
					printf("VY");
					V--;
				}
			}

		}
	} else {
		assert(0);
	}
	while(G > 0) {
					printf("GR");
					G--;
				}
	while(V > 0) {
					printf("VY");
					V--;
				}
	while(O > 0) {
					printf("OB");
					O--;
				}
	printf("\n");
}
int main() {
	int T;
	cin >> T;
	for(int cas = 1; cas <= T; ++cas) {
		cin >> N >> R >> O >> Y >> G >> B >> V;
		solve(cas);
		
	}
	return 0;
}