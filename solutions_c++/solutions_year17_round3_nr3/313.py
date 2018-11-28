/* In The Name Of God */
#include <bits/stdc++.h>

# define xx first
# define yy second
# define pb push_back
# define pp pop_back
# define eps 1e-9

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vint;
int U,n;
long double tmp;
multiset<int> s;
int main(){
	ios_base::sync_with_stdio (0);
	freopen("c.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;cin>>T;
	for(int tc=1 ; tc<=T ; tc++){
		cin>>n>>n;
		cin>>tmp;
		tmp += 0.00005;
		U = tmp*10000;
		while(n--){
			cin>>tmp;
			tmp += 0.00005;
			s.insert(tmp*10000);
		}
		while(U--){
			int mini = *s.begin();
			s.erase(s.begin());
			s.insert(mini+1);
		}
		long double ans = 1.0000000000;
		while(!s.empty()){
			int mini = *s.begin();
			s.erase(s.begin());
			ans = (ans * (double)mini/10000.0);
		}
		cout<<"Case #"<<tc<<": ";
		cout<<fixed<<setprecision(8)<<ans<<endl;
	}
	return 0;
}

