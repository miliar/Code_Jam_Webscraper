#include <bits/stdc++.h>
using namespace std;
int N, R, O, Y, G, B, V;
int rr, bb, yy;
char str[1005];
void check(string s) {
	if(s == "IMPOSSIBLE") return;
	int n = s.length();
	int r = 0, y = 0, b = 0;
	for(int i = 0; i < n; i++) {
		if(s[i] == 'R') r++;
		if(s[i] == 'B') b++;
		if(s[i] == 'Y') y++;
		if(i > 0 && s[i] == s[i - 1]) printf("fail1!\n");
	}
	if(r != rr) printf("fail2!\n");
	if(b != bb) printf("fail3!\n");
	if(y != yy) printf("fail4!\n");
	if(s[0] == s[n - 1]) printf("fail5\n");
}

void solve_small(int cases) {
	cin >> N >> R >> O >> Y >> G >> B >> V;
	//printf("\n\n");
	//printf("y = %d, r = %d, b = %d\n", Y, R, B);
	string solution = "SHIT";
	if(O + G + V == 0) {
		solution = "IMPOSSIBLE";
		//rr = R;
		//bb = B;
		//yy = Y;
		if(B >= abs(R - Y) && B <= (R + Y)) {
			solution = "";
			if(R > Y) {
				while(R > 0 || Y > 0 || B > 0) {
					if(R > 0) {solution += 'R'; R--;}
					if(B > 0 && R + Y < B) {solution += 'B'; B--;}
					if(Y > 0) {solution += 'Y'; Y--;}
					if(B > 0 && R + Y < B) {solution += 'B'; B--;}
				}
			} else {
				while(R > 0 || Y > 0 || B > 0) {
					if(Y > 0) {solution += 'Y'; Y--;}
					if(B > 0 && R + Y < B) {solution += 'B'; B--;}
					if(R > 0) {solution += 'R'; R--;}
					if(B > 0 && R + Y < B) {solution += 'B'; B--;}
					//printf("y = %d, r = %d, b = %d, str = %s\n", Y, R, B, solution.c_str());
				}
			}
		} 
	}
	//check(solution);
	printf("Case #%d: %s\n", cases, solution.c_str());
}

void solve_big(int cases) {


}


int main() {
	//freopen("sample_in.txt", "r", stdin);
	freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.ou.txt", "w", stdout);

	int T, cases = 0;
	
	scanf("%d", &T);
	while(T--) {
		solve_small(++cases);
		//solve_big(++cases);
	}
	return 0;
}
