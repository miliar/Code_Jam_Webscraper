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
	int t;
	double d;
	int n;
	cin>>t;
	
	fr(caseNum, 1, t+1){
		cin>>d>>n;
		double x, v;
		double t = 0;
		while(n--){
			cin>>x>>v;
			x = d-x;
			t = max(t, x/v); 
		}
		
		double ans = d/t;
		
		printf("Case #%d: %.8lf\n", caseNum, ans); 
	}
	
	return 0;
}
