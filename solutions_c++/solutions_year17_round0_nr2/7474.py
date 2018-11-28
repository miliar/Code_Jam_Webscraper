#include<bits/stdc++.h>
#define maxn 500009
#define inf 1000000007
#define llinf 1000000000000000007
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define mid(a,b) (a+b)/2
#define endl "\n"
#define sz size()
#define MOD 1000000007
#define M 100000
#define pii pair<int,int>
#define all(x) x.begin(),x.end()
#define tr(i, c) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)
using namespace std;
typedef long long ll;
//priority_queue < pii, vector< pii >, greater< pii > > Q;


vector < int > v;


int main(){
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	int T, pos;
	cin>>T;
	for(int q=1; q<=T; q++){
		ll x;
		bool f = 0;
		cin>>x;
		v.clear();
		while(x){
			v.pb(x%10);
			x/=10;
		}
		reverse(all(v));
		pos = 0;
		for(int i=1; i<v.sz; i++){
			if(v[i] < v[i-1]){
				f = 1;
				break;
			}
			else if(v[i] > v[i-1])
				pos = i;
		}
		if(f){
			v[pos]--;
			for(int i=pos+1; i<v.sz; i++)
				v[i] = 9;
			for(int i=v.sz-2; i>=0; i--)
				v[i] = min(v[i], v[i+1]);
		}
		x = 0;
		while(v[x] == 0)
			x++;
		cout<<"Case #"<<q<<": ";
		for(int i=x; i<v.sz; i++)
			cout<<v[i];
		cout<<endl;
		
	}

return 0;
}

