#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;

const int MM = 1e9 + 7;
const double eps = 1e-8;
const int MAXN = 2e6 + 10;

int n, m;

void prework(){

}

void read(){

}

string s;

int gao(int R, int B, int Y){
	s = "";
	int n = R + B + Y;
	if (R >= B && R >= Y){
		if (R > B + Y) return 0;
		for(int i = 1; i <= n; i++){
			if (i & 1){
				if (R) s.push_back('R'), R--;
				else{
					if (B > Y)
						s.push_back('B'), B--;
					else
						s.push_back('Y'), Y--;
				}
			}
			else{
				if (B > Y)
					s.push_back('B'), B--;
				else
					s.push_back('Y'), Y--;
			}
		}
		return 1;
	}
	if (B >= R && B >= Y){
		if (B > R + Y) return 0;
		for(int i = 1; i <= n; i++){
			if (i & 1){
				if (B) s.push_back('B'), B--;
				else{
					if (R > Y)
						s.push_back('R'), R--;
					else
						s.push_back('Y'), Y--;
				}
			}
			else{
				if (R > Y)
					s.push_back('R'), R--;
				else
					s.push_back('Y'), Y--;
			}
		}
		return 1;
	}
	if (Y >= B && Y >= R){
		if (Y > B + R) return 0;
		for(int i = 1; i <= n; i++){
			if (i & 1){
				if (Y) s.push_back('Y'), Y--;
				else{
					if (B > R)
						s.push_back('B'), B--;
					else
						s.push_back('R'), R--;
				}
			}
			else{
				if (B > R)
					s.push_back('B'), B--;
				else
					s.push_back('R'), R--;
			}
		}
		return 1;
	}
}

void solve(int casi){
	cout << "Case #" << casi << ": ";
	int N, R, O, Y, G, B, V;
	cin>>N;
	//puts("???");
	cin>>R>>O>>Y>>G>>B>>V;
	// O B
	// G R
	// V Y
	//puts("==");
	//cout<<R<<' '<<O<<' '<<Y<<' '<<G<<' '<<B<<' '<<V<<endl;
	if (O > B || (O != 0 && O == B && Y + G + R + V != 0)){
		puts("IMPOSSIBLE"); return ;
	}
	//puts("==");
	if (G > R || (G != 0 && G == R && O + B + Y + V != 0)){
		puts("IMPOSSIBLE"); return ;
	}
	//puts("==");
	if (V > Y || (V != 0 && V == Y && O + B + R + G != 0)){
		puts("IMPOSSIBLE"); return ;
	}
	//puts("==");
	if (O == B && Y + G + R + V == 0){
		for(int i = 1; i <= O; i++){
			putchar('O');
			putchar('B');
		}
		puts(""); return ;
	}
	//puts("==");
	if (G == R && O + B + Y + V == 0){
		for(int i = 1; i <= G; i++){
			putchar('G');
			putchar('R');
		}
		puts(""); return ;
	}
	//cout<<V<<' '<<Y<<' '<<O + B + R + G <<endl;
	if (V == Y && O + B + R + G == 0){
		for(int i = 1; i <= V; i++){
			putchar('V');
			putchar('Y');
		}
		puts(""); return ;
	}
	B -= O, R -= G, Y -= V;
	if (!gao(R, B, Y)){
		puts("IMPOSSIBLE");
		return ;
	}
	int fR = 1, fB = 1, fY = 1;
	for(int i = 0; i < s.size(); i++){
		putchar(s[i]);
		if (s[i] == 'R' && fR == 1){
			fR = 0;
			for(int j = 1; j <= G; j++){
				putchar('G');
				putchar('R');
			}
		}
		if (s[i] == 'B' && fB == 1){
			fB = 0;
			for(int j = 1; j <= O; j++){
				putchar('O');
				putchar('B');
			}
		}
		if (s[i] == 'Y' && fY == 1){
			fY = 0;
			for(int j = 1; j <= V; j++){
				putchar('V');
				putchar('Y');
			}
		}
	}
	puts("");
}

void printans(){

}

int main(){
	//std::ios::sync_with_stdio(false);
	prework();
	int T = 1;
	cin>>T;
	for(int i = 1; i <= T; i++){
		read();
		solve(i);
		printans();
	}
	return 0;
}

