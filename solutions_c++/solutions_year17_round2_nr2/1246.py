#include <bits/stdc++.h>
using namespace std;

#define fr(i,a,b) for(int i = a; i < (b); i++) 
#define fi first
#define se second
#define pb push_back
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d %d", &a, &b)
#define sc3(a,b,c) scanf("%d %d %d", &a, &b)
#define pri(a) printf("%d\n", a)
#define mp make_pair
#define DESYNC ios_base::sync_with_stdio(false)

typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef long long int ll;

const int INF = 0x3f3f3f3f;
const ll LINF = 0x3f3f3f3f3f3f3f3f;
const int MOD = 1000000007;
const double PI = acos(-1);

int main(){
	int t, n, r, o, y, g, b, vi;
	vector<char> v;
	int qtd[3];
	string ans;
	
	cin>>t;
	
	fr(num, 1, t+1){
		cin>>n>>r>>o>>y>>g>>b>>vi;
		int maxi = max(r, max(y,b));
		if(maxi > n/2){
			printf("Case #%d: IMPOSSIBLE\n", num);
			continue;
		}
		v.clear();
		if(r >= y && r >= b){
			v.pb('R');
			qtd[0] = r;
		
			if(b > y){
				v.pb('B');
				v.pb('Y');
				qtd[1] = b;
				qtd[2] = y;
			}
			else{
				v.pb('Y');
				v.pb('B');
				qtd[1] = y;
				qtd[2] = b;
			}
		}
		else if(y >= r && y >= b){
			v.pb('Y');
			qtd[0] = y;
			if(b > r){
				v.pb('B');
				v.pb('R');
				qtd[1] = b;
				qtd[2] = r;
			}
			else{
				v.pb('R');
				v.pb('B');
				qtd[1] = r;
				qtd[2] = b;
			}
		}
		else{
			v.pb('B');
			qtd[0] = b;
			if(y > r){
				v.pb('Y');
				v.pb('R');
				qtd[1] = y;
				qtd[2] = r;
			}
			else{
				v.pb('R');
				v.pb('Y');
				qtd[1] = r;
				qtd[2] = y;
			}
		}
		
		ans.clear();
		fr(i,0,n) ans.pb('E');
	
		printf("Case #%d: ", num);
		bool pos = 1;
		int i = 0;
		while(qtd[0] > 0){
			if(ans[(i+1)%n] != 'E' || ans[(i+n-1)%n] != 'E' || ans[i] != 'E'){
				printf("IMPOSSIBLE\n");
				pos = 0;
				break;
			}
			ans[i] = v[0];
			qtd[0]--;
			if(qtd[0] > 0){
				i += 2;
				i %= n;
			}
		}
	
		if(pos == 1){
			int ch = 0;
			while(qtd[1] + qtd[2] > 0){
				while(ans[i] != 'E'){
					i++;
					i %= n;
				}
				if(ans[(i+1)%n] == v[ch+1] || ans[(i+n-1)%n] == v[ch+1]){
					printf("IMPOSSIBLE\n");
					pos = 0;
					break;
				}
				ans[i] = v[ch+1];
				qtd[ch+1]--;
				ch ^= 1;
				if(qtd[ch+1] == 0) ch ^= 1;
			}
			
			int r1 = 0, b1 = 0, y1 = 0;
			fr(i,0,n){
				if(ans[i] == 'R') r1++;
				if(ans[i] == 'B') b1++;
				if(ans[i] == 'Y') y1++;
			}
			
			if(pos == 1){
				cout<<ans<<'\n';
			}
		}
	}

	return 0;
}
