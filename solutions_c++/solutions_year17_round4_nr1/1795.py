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
typedef vector < pair<int, int> > vii;
typedef long double ld;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;	

int T, N, P, ans, x;
int residue[4];

int main(){
	ios_base::sync_with_stdio(false); cin.tie(0);
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-out.out","w",stdout);
	cin >> T;
	for(int t = 1; t <= T; t++){
		cin >> N >> P;
		for(int i = 0; i < N; i++){
			cin >> x;
			residue[x%P]++;
		}
		ans=residue[0];
		if(P==2){
			ans+=(residue[1]+1)/2;
		}
		else if(P==3){
			ans+=(min(residue[1],residue[2]));
			if(residue[1]<=residue[2]){
				residue[2]-=residue[1];
				residue[1]=0;
			}
			else{
				residue[1]-=residue[2];
				residue[2]=0;
			}
			if(residue[1]>0){
				ans+=(residue[1]+2)/3;
			}
			if(residue[2]>0){
				ans+=(residue[2]+2)/3;
			}
		}
		cout << "Case #" << t << ": " << ans << '\n';
		residue[0]=0;
		residue[1]=0;
		residue[2]=0;
		residue[3]=0;
	}
}
