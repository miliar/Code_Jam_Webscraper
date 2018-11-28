#include <cfloat>
#include <climits>
#include <cmath>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

typedef unsigned long long ulint;
typedef long long lint;
typedef long double lubb;

bool run(const int N, const int R, const int O, const int Y, const int G, const int B, const int V)
{
	int s = N >> 1;
	int r = R + O + V;
	int y = Y + O + G;
	int b = B + G + V;
	return (r <= s && y <= s && b <= s);
}

bool canR(char last, int R) {
	return (last != 'R' and last != 'V' and last != 'O' and R > 0);
} 
bool canY(char last, int Y) {
	return (last != 'Y' and last != 'O' and last != 'G' and Y > 0);
}
bool canB(char last, int B) {
	return (last != 'B' and last != 'G' and last != 'V' and B > 0);
}
bool canV(char last, int V) {
	return (last != 'V' and last != 'B' and last != 'R' and V > 0);
}
bool canO(char last, int O) {
	return (last != 'O' and last != 'R' and last != 'Y' and O > 0);
}
bool canG(char last, int G) {
	return (last != 'G' and last != 'B' and last != 'Y' and G > 0);
}
void prun(int N, int R, int O, int Y, int G, int B, int V) {
	char last = 'X';
	char first = 'X';
	while ( N > 0 ) {
		if ( O >= Y && O >= G && canO(last, O)) {
			cout << 'O'; O--; last = 'O';
			if (first == 'X') first = 'O';
			N--; continue;
		} else if ( G >= O && G >= V && canG(last,G)) {
			cout << 'G'; G--; last = 'G';
			if (first == 'X') first = 'G';
			N--; continue;
		} else if ( V >= O && V >= G && canV(last,V)) {
			cout << 'V'; V--; last = 'V';
			if (first == 'X') first = 'V';
			N--; continue;
		} else if ( R > O && R > Y && R > G && R > B && R > V && canR(last,R)) {
			cout << 'R'; R--; last = 'R';
			if (first == 'X') first = 'R';
			N--; continue;
		} else if ( B >R && B > O && B > Y && B > G && B > V && canB(last,B)) {
			cout << 'B'; B--; last = 'B';
			if (first == 'X') first = 'B';
			N--; continue;
		} else if ( Y > R && Y > O && Y > G && Y > B && Y > V && canY(last,Y)) {
			cout << 'Y'; Y--; last = 'Y';
			if (first == 'X') first = 'Y';
			N--; continue;
		} else if (first=='R' &&  R >= O && R >= Y && R >= G && R >= B && R >= V && canR(last,R)) {
			cout << 'R'; R--; last = 'R';
			if (first == 'X') first = 'R';
			N--; continue;
		} else if (first=='Y' &&  Y >= R && Y >= O && Y >= G && Y >= B && Y >= V && canY(last,Y)) {
			cout << 'Y'; Y--; last = 'Y';
			if (first == 'X') first = 'Y';
			N--; continue;
		} else if (first=='B' &&  B >= R && B >= O && B >= Y && B >= G && B >= V && canB(last,B)) {
			cout << 'B'; B--; last = 'B';
			if (first == 'X') first = 'B';
			N--; continue;
		} else if ( R >= O && R >= Y && R >= G && R >= B && R >= V && canR(last,R)) {
			cout << 'R'; R--; last = 'R';
			if (first == 'X') first = 'R';
			N--; continue;
		} else if ( Y >= R && Y >= O && Y >= G && Y >= B && Y >= V && canY(last,Y)) {
			cout << 'Y'; Y--; last = 'Y';
			if (first == 'X') first = 'Y';
			N--; continue;
		} else if ( B >= R && B >= O && B >= Y && B >= G && B >= V && canB(last,B)) {
			cout << 'B'; B--; last = 'B';
			if (first == 'X') first = 'B';
			N--; continue;
		} else if (canO(last,O)) {
			cout << 'O'; O--; last = 'O';
			if (first == 'X') first = 'O';
			N--; continue;
		} else if (canG(last,G)) {
			cout << 'G'; G--; last = 'G';
			if (first == 'X') first = 'G';
			N--; continue;
		} else if (canV(last,V)) {
			cout << 'V'; V--; last = 'V';
			if (first == 'X') first = 'V';
			N--; continue;
		} else if (canR(last,R)) {
			cout << 'R'; R--; last = 'R';
			if (first == 'X') first = 'R';
			N--; continue;
		} else if (canY(last,Y)) {
			cout << 'Y'; Y--; last = 'Y';
			if (first == 'X') first = 'Y';
			N--; continue;
		} else if (canB(last,B)) {
			cout << 'B'; B--; last = 'B';
			if (first == 'X') first = 'B';
			N--; continue;
		} else {
			cout << "IMPOSSIBLE";
			break;
		}
	}
}

void test() {
	int N, R, O, Y, G, B, P;
	cin >> N;
	cin >> R;
	cin >> O;
	cin >> Y;
	cin >> G;
	cin >> B;
	cin >> P;
	bool possible = run(N, R, O, Y, G, B, P);
	if (possible) {
		prun(N, R, O, Y, G, B, P);
	} else {
		cout << "IMPOSSIBLE";
	}	
}	

int main() {
	unsigned long T;
	cin >> T;
	for(unsigned long i = 1; i<=T; i++) {
		cout << "Case #" << i << ": ";
		test();	
		cout << endl;
	}
	return 0;
}
