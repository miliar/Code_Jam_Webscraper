#include <bits/stdc++.h> 
using namespace std;

#define mp make_pair

bool cmp(pair<int, char> a, pair<int, char> b) {
	return a > b;
}

void out(int ch, int &RY, int &YB, int &BR) {
	char ch2 = ch == 'Y' ? 'V' : ch == 'R' ? 'G' : 'O';
	int *t = ch == 'Y' ? &BR : ch == 'R' ? &YB : &RY;
	putchar(ch);
	while((*t)--) {
		putchar(ch2);
		putchar(ch);
	}
	(*t)++;
}

int main() {
	//freopen("B-large.in", "r",stdin);
	//freopen("out.out","w",stdout);
	int T; scanf("%d",&T);
	while(T--) { 
		char flg[300] = {0};
		int R, RY, Y, YB, B, BR, N;
		scanf("%d%d%d%d%d%d%d", &N, &R, &RY, &Y, &YB, &B, &BR);
		int true_R = R - YB, true_Y = Y - BR, true_B = B - RY;
		static int cas = 1;
		printf("Case #%d: ", cas++);
		
		if(N == 1) {
			puts(R ? "R" : RY ? "O" : Y ? "Y" : YB ? "G" : B ? "B" : "V");
			continue;	
		}
		
		if(true_R < 0 || true_Y < 0 || true_B < 0) {
			puts("IMPOSSIBLE");
			continue;
		}
		
		
		if(R != 0 && YB == R || Y != 0 && BR == Y || B != 0 && RY == B) {
			// If only two colors exists
			if((Y == 0) + (R == 0) + (B == 0) == 2) {
				char c1 = Y ? 'Y' : R ? 'R' : 'B';
				char c2 = YB ? 'G' : BR ? 'V' : 'O';
				
				for(int i = 0; i < Y+R+B; ++i)
					printf("%c%c", c1, c2);
				puts("");
			}
			else puts("IMPOSSIBLE");
		}
		else {
			if(true_R + true_Y + true_B == 1) {
				if(N == 1) puts(R ? "R" : Y ? "Y" : "B");
				else puts("IMPOSSIBLE");
			}
			else {
				vector<pair<int, char> > tt = {mp(true_R, 'R'), mp(true_Y, 'Y'), mp(true_B, 'B')};
				sort(tt.begin(), tt.end(), cmp);
				if(tt[0].first > tt[1].first + tt[2].first) {
					puts("IMPOSSIBLE");
					continue;
				}
				while(tt[0].first) {
					out(tt[0].second, RY, YB, BR);
					tt[0].first--;
					if(tt[2].first >= tt[1].first)
						swap(tt[1], tt[2]);
					out(tt[1].second, RY, YB, BR);//putchar(tt[1].second);
					tt[1].first--;
				}
				
				
				//if(tt[1].first == tt[2].first)
					swap(tt[1], tt[2]);
				
				while(tt[1].first) {
					out(tt[1].second, RY, YB, BR);//putchar(tt[1].second);
					tt[1].first--;
					if(tt[2].first) {
						out(tt[2].second, RY, YB, BR);//putchar(tt[2].second);
						tt[2].first--;
					}
				}
				puts("");
			}
		}
		
	}
	//fclose(stdout);
	return 0;
}
