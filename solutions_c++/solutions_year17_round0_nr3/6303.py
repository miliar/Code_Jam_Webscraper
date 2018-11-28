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
	
	//freopen("Csmall2.in", "r", stdin);
    //freopen("Csmallout2.txt", "w", stdout);
	
	int T, tt=1;
	int N, P;
	
	cin >> T;
	
	while(T--){
		
		cin >> N >> P;
		priority_queue<pair<int, ii> >q;
		
		q.push({N, {-1, N}});
		
		int cnt = 0;
		
		while(1){
			
			int qt = q.top().F;
			int ini = -q.top().S.F;
			int fim = q.top().S.S;
			q.pop();
			
			int s = fim-ini+1;
			int mid = (ini+fim)/2;
			
			if(cnt == P-1){
				int a = mid-(ini-1)-1; int b = (fim+1)-mid-1;
				printf("Case #%d: %d %d\n", tt++, max(a,b), min(a,b));
				break;
			}

			q.push({fim-mid+1, {-(mid+1), fim}});
			q.push({mid-ini+1, {-ini, mid-1}});
			
			cnt++;
		}
		
	}
	
	return 0;
}
