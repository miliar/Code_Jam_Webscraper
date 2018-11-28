#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#ifdef _DEBUG_
	#define debug(...) printf(__VA_ARGS__)
#else
	#define debug(...) (void)0
#endif
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int MAXRC = 30;
char S[MAXRC][MAXRC];

int main() {
	int all_kase;
	scanf("%d", &all_kase);
	for(int num_kase = 1; num_kase <= all_kase; num_kase++) {
		int R, C;
		scanf("%d%d", &R, &C);
		for(int i = 0; i < R; i++)
			scanf("%s", S[i]);
		for(int i = 0; i < R; i++) {
			char first = '?';
			for(int j = 0; j < C; j++) {
				if(S[i][j] != '?') {
					first = S[i][j];
					break;
				}
			}
			if(first == '?') continue;
			char lst = first;
			for(int j = 0; j < C; j++) {
				if(S[i][j] == '?') S[i][j] = lst;
				else lst = S[i][j];
			}
		}
		int lst = -1;
		for(int i = 0; i < R; i++)
			if(S[i][0] != '?') {
				lst = i;
				break;
			}
		assert(lst >= 0);
		for(int i = 0; i < R; i++) {
			if(S[i][0] == '?') {
				for(int j = 0; j < C; j++)
					S[i][j] = S[lst][j];
			}
			else
				lst = i;
		}
		printf("Case #%d:\n", num_kase);
		for(int i = 0; i < R; i++)
			printf("%s\n", S[i]);
	}
	return 0;
}
