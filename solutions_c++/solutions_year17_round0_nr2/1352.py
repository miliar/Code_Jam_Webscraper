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
typedef vector<char> VC;

const int N_MAX=20;

int main() {
	int t;
	scanf("%d", &t);
	for(int kase=1; kase<=t; kase++) {
		printf("Case #%d: ", kase);
		char s[N_MAX];
		scanf("%s", s);
		int n = strlen(s);

		char ans[N_MAX];
		for(int i=0; i<n; i++) {
			bool flag = true;
			for(int j=i+1; j<n; j++) {
				if(s[j] != s[i]) {
					flag = (s[j] > s[i]);
					break;
				}
			}
			if(flag)
				ans[i] = s[i];
			else {
				ans[i] = s[i]-1;
				for(int j=i+1; j<n; j++)
					ans[j] = '9';
				break;
			}
		}
		int st=0;
		while(st<n && ans[st] == '0')
			++st;
		assert(st<n);
		ans[n] = '\0';
		printf("%s\n", ans+st);
	}
	return 0;
}
