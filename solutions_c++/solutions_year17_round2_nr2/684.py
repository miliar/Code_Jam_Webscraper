#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define fbo find_by_order
#define ook order_of_key

typedef long long ll;
typedef pair<ll,ll> ii;
typedef vector<int> vi;
typedef long double ld; 
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;

ll n, r, o, y, g, b, v;
vector < pair<ll, int> > horse;
string s;
vector <int> ans;

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	int t; cin>>t;
	string mune = "RBY";
	for(int zz = 1; zz <= t; zz++)
	{
		horse.clear();
		cout<<"Case #"<<zz<<": ";
		cin >> n >> r >> o >> y >> g >> b >> v;
		ll z = r + b + y;
		if(2*r > z || 2*b > z || 2*y > z){
			cout << "IMPOSSIBLE\n";
		}
		else{
		ans.clear();
		horse.pb(mp(r, 0));
		horse.pb(mp(b, 1));
		horse.pb(mp(y, 2));
		sort(horse.rbegin(), horse.rend());
		for(int i = 0; i < horse[1].fi; i++){
			ans.pb(horse[0].se);
			ans.pb(horse[1].se);
		}
		horse[0].fi -= horse[1].fi;
		horse[1].fi = 0;
		sort(horse.rbegin(), horse.rend());
		if(horse[1].se == ans[0]){
		for(int i = 0; i < horse[1].fi; i++){
			ans.pb(horse[1].se);
			ans.pb(horse[0].se);
		}
		}
		else{
		for(int i = 0; i < horse[1].fi; i++){
			ans.pb(horse[0].se);
			ans.pb(horse[1].se);
		}
		}
			
		horse[0].fi -= horse[1].fi;
		horse[1].fi = 0;
		for(int i = 0; i < ans.size(); i++){
			if(horse[0].fi && i > 0){
				horse[0].fi--;
				cout << mune[horse[0].se] << mune[ans[i]];
			}
			else{
				cout << mune[ans[i]];
			}
		}
		cout << endl;
		
		}
		cerr<<"Case #"<<zz<<" solved.\n";
	}
}

