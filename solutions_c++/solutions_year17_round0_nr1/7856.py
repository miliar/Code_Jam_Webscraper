#include <bits/stdc++.h>

#define INF 0x3F3F3F3F
#define DINF 1e+12
#define rep(i, a, b) for (int i = int(a); i < int(b); i++)
#define pb push_back
#define pi 3.1415926535897932384626433832795028841971
#define debug(x) if(1) cout << #x << " = " << x << endl;
#define debug2(x,y) cout << #x << " = " << x << " --- " << #y << " " << y << "\n";
#define all(S) (S).begin(), (S).end()
#define MAXV 1005
#define F first
#define S second
#define EPS 1e-9
#define mp make_pair

// freopen("in.txt", "r", stdin);
// freopen("out.txt", "w", stdout);

using namespace std;

typedef long long ll;
typedef pair < int, int >  ii;

char s[1005];
int K, N;

int main(){
	
	int T, tt=1;
	
//	freopen("inALarge.in", "r", stdin);
   // freopen("outALarg.txt", "w", stdout);
	
	cin >> T;
	
	while(T--){
		
		cin >> s >> K;
		N = strlen(s);
		
		int ans = 0;
		int pos = K-1;
		
		while(pos < N){
			
			bool fu = 0;
			while(s[pos-K+1] == '+'){
				pos++;
				if(pos >= N){
					fu = 1;
					break;
				}
			}
			
			if(fu) break;
			
			bool menos = 0;
			rep(i, pos-K+1, pos+1){
				if(s[i] == '-') s[i] = '+', menos = 1;
				else s[i] = '-';
			}
			
			if(menos) ans++;
			pos++;
		}
		
		rep(i, 0, N) if(s[i] == '-') ans = -1;
		
		printf("Case #%d: ", tt++);
		if(ans == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	
	return 0;
}
