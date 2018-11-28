#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define sz(a) (int)a.size()
#define rep(i, a, n) for(int i = a; i < n; i++)
#define dec(i, a, n) for(int i = a; i >= n; i--)
#define clr(a,v) memset(a,v,sizeof(a))
#define all(a) a.begin(),a.end()
#define MAXN 100010 // 1e5
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector <int> vi;

map <string, int> mapa;

ll trans(string a){
	ll b=0;
	rep(i,0,sz(a)){
		b*=10;
		b+=a[i]-'0';
	}
	return b;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output2.txt", "w", stdout);
	queue<string> fila;
	rep(i,'1','9'+1) {
		string ini;
		ini+=char(i);
		fila.push(ini);
		mapa[ini]=1;
	}	
	while(sz(fila)){
		string a=fila.front();fila.pop();
		if(sz(a)>=18)break;
		rep(i,a[sz(a)-1],'9'+1) {
			fila.push(a+(char)i);
			mapa[a+(char)i]=1;
		}
	}
	vector <ll> nums;
	for ( map <string, int> :: iterator it = mapa.begin(); it != mapa.end(); it++) {
		nums.pb(trans((*it).x));
	}
	sort(all(nums));
	int tt;
	scanf("%d", &tt);
	rep(caso,1,tt+1){
		ll numero;
		cin >> numero;
		ll ans=0;
		int l=0,r=sz(nums)-1;
		
		while(r-l>=0){
			int mid=(l+r)>>1;
			if(nums[mid]<=numero) {l=mid+1;ans=nums[mid];}
			else r=mid-1;
		}
		cout << "Case #" << caso << ": " << ans << endl;
	}
}
