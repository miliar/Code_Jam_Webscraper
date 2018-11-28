#include <bits/stdc++.h>
using namespace std;

#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define BUFF ios::sync_with_stdio(false);
#define db(x) cerr << #x << " == " << x << endl
#define dbs(x) cerr << x << endl		//dbs(a _ b);
#define _ << ", " <<
#define endl '\n'
#define cl(x, v) memset((x), (v), sizeof(x))

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<int, pii> piii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

const double PI = acos(-1), EPS = 1e-9;
const long long LINF = 0x3f3f3f3f3f3f3f3fLL;
const int INF = 0x3f3f3f3f, MOD = 1e9+7, N = 1e5+5;

int n, T;

bool check(int x){
	if(x<10)
		return true;
	int x1 = x%10;
	int x2 = (x%100 - x1)/10;
	if(x<100){
		if(x2 <= x1)
			return true;
		else
			return false;
	}
	int x3 = (x%1000 - x2 - x1)/100;
	if(x<1000){
		if(x3 <= x2 and x2 <= x1)
			return true;
		else
			return false;
	}
	return false;
}

main(){
	scanf("%d", &T);
	for(int t=1; t<=T; t++){
		scanf("%d", &n);
		while(!check(n))
			n--;
		printf("Case #%d: %d\n", t, n);
	}
}