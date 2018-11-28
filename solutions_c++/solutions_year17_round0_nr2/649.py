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

set<ll> s;

void gen(ll num, int qtd, int last){
	s.insert(num);
	
	if(qtd == 18) return;
	
	num *= 10;
	fr(i,last,10){
		gen(num+i, qtd+1, i);
	}
	
	return;
}

int main(){
	gen(0, 0, 1);
	s.insert(1000000000000000001LL);
	
	int t;
	ll n;
	set<ll>::iterator it;
	
	cin>>t;
	fr(i,1,t+1){
		cin>>n;
		it = s.upper_bound(n);
		it--;
		cout<<"Case #"<<i<<": "<<*it<<'\n';
	}
	
	return 0;
}
