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

using namespace std;

typedef long long ll;
typedef pair < int, int >  ii;


int main(){
	
//	freopen("bsmall.in", "r", stdin);
 //   freopen("outbsmall.txt", "w", stdout);
	
	int T, N, tt=1;
	char s[123];
	
	cin >> T;
	
	while(T--){
		
		cin >> N;
		printf("Case #%d: ", tt++);
		for(int i = N; i >= 0; i--){
			vector<int> v;
			int x = i;
			while(x){
				v.pb(x%10);
				x/=10;
			}
			bool ok = 1;
			rep(j, 1, v.size()){
				if(v[j] > v[j-1]) { ok = 0; break; }
			}
			if(ok){
				printf("%d\n", i);
				break;
			}
		}
	}
	
	return 0;
}
