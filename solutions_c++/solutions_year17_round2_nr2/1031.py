#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<int,int> pii;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
int t;
int N, R, O, Y, G, B, V;
int main(){
	scanf("%d", &t);
	for(int tc = 1; tc <= t; ++tc){
		scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
		printf("Case #%d: ", tc);
		int cnt0 = (R == 0) + (Y == 0) + (B == 0);
		if(R == 0 || Y == 0 || B == 0){
			if(cnt0 == 2){
				puts("IMPOSSIBLE");
			}
			else{
				if(B == 0){
					if(R != Y) puts("IMPOSSIBLE");
					else{
						for(int i = 0;i < R; ++i) printf("RY");
						puts("");
					}
				}
				else if(Y == 0){
					if(R != B) puts("IMPOSSIBLE");
					else{
						for(int i = 0;i < R; ++i) printf("RB");
						puts("");
					}
				}
				if(R == 0){
					if(B != Y) puts("IMPOSSIBLE");
					else{
						for(int i = 0;i < B; ++i) printf("BY");
						puts("");
					}
				}
			}
		}
		else{
			if(R == Y && Y == B){
				for(int i = 0;i < R; ++i) printf("RYB");
					puts("");
			}
			else if(R > Y + B || Y > R + B || B > Y + R){
				puts("IMPOSSIBLE");
			}
			else{
				int maps[3] = {'R', 'Y', 'B'};
				int ar[3] = {R, Y, B};
				if(ar[0] > ar[1]) swap(ar[0], ar[1]), swap(maps[0], maps[1]);
				if(ar[1] > ar[2]) swap(ar[1], ar[2]), swap(maps[1], maps[2]);
				if(ar[0] > ar[1]) swap(ar[0], ar[1]), swap(maps[0], maps[1]);
				string s = "";
				for(int i = 0; i < ar[1]; ++i) {
					s += maps[2];
					s += maps[1];
				}
				ar[2] -= ar[1];
				ar[1] -= ar[1];
				for(int i = 0; i < ar[2]; ++i) {
					s += maps[2];
					s += maps[0];
				}
				ar[0] -= ar[2];
				ar[2] -= ar[2];
				for(int i = 0;i < ar[0]; ++i){
					
					for(int j = 1;j < s.length() - 1; ++j){
						if(s[j] != maps[0] && s[j-1] != maps[0]){
							s.insert(j, 1, maps[0]);
							break;
						}
					}
				}
				puts(s.c_str());
				//printf("%d %d\n", s.length(), N);
				assert(s[s.length() - 1] != s[0]);
				assert(s.length() == N);
				int countR = 0, countG = 0, countB = 0;
				for(int i = 0;i < s.length(); ++i){
					if(s[i] == 'R') countR++;
					else if(s[i] == 'G') countG++;
					else if(s[i] == 'B') countB++;
				}
				assert(countR == R);
				assert(countG == G);
				assert(countB == B); 
			}
		}
	}
	return 0;
}