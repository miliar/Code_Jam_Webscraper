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

const int MAXN = 25 + 10;

char s[MAXN][MAXN];

int main() {
	int T;
	scanf("%d", &T);
	for(int kase=1; kase<=T; kase++) {
		int n, m;
		scanf("%d%d", &n, &m);
		for(int i=0; i<n; i++)	scanf("%s", s[i]);

		for(int i=0; i<n; i++) {
			char p = '?';
			bool flag = false;
			for(int j=0; j<m; j++) {
				if(s[i][j] != '?') {
					p = s[i][j];
					flag = true;
				}
				s[i][j] = p;
			}
			for(int j=m-1; j>=0; j--) {
				if(s[i][j] != '?') {
					p = s[i][j];
					flag = true;
				}
				s[i][j] = p;
			}
			if(!flag && i) {
				for(int j=0; j<m; j++)	s[i][j] = s[i-1][j];
			}
		}
		for(int i=n-2; i>=0; i--) {
			if(s[i][0] == '?') {
				for(int j=0; j<m; j++)	s[i][j] = s[i+1][j];
			}
		}

		printf("Case #%d:\n", kase);
		for(int i=0; i<n; i++)	puts(s[i]);
	}
    
    return 0;
}
