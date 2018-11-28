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
	
 //freopen("alarge.in", "r", stdin);
 //freopen("out2.txt", "w", stdout);
	
	int tc;
	int d, n;
	double s;
	int k, tt=1;
	
	cin >> tc;
	
	while(tc--){
		
		double maior = 0;
		cin >> d >> n;
		rep(i, 0, n){
			cin >> k >> s;
			int dis = d-k;
			double tempo = dis/s;
			maior = max(maior, tempo);
		}
		
		double speed = d/maior;
		printf("Case #%d: %.6lf\n", tt++, speed);
	}
	
	return 0;
}
