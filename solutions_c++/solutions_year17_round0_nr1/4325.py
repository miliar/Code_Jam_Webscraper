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

const int MAXN = 1000 + 10;

char s[MAXN];

int main() {
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++) {
		int k;
		scanf("%s%d", s, &k);
		int n = strlen(s);

		int ans = 0;
		for(int i=0; i<=n-k; i++) {
			if(s[i]=='-') {
				for(int j=0; j<k; j++)	s[i+j] = (s[i+j]=='+' ? '-' : '+');
				ans++;
			}
		}

		printf("Case #%d: ", t);
		bool flag = false;
		for(int i=0; i<n; i++)
			if(s[i]=='-') {
				puts("IMPOSSIBLE");
				flag = true;
				break;
			}
		if(!flag)
			printf("%d\n", ans);
	}
    
    return 0;
}
