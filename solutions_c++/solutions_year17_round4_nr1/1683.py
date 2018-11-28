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
int a[5];
int main(){
	ios_base::sync_with_stdio (0);
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;cin>>T;
	for(int tc=1 ; tc<=T ; tc++){
		memset(a,0,sizeof a);
		int n,p;cin>>n>>p;
		while(n--){
			int tmp;cin>>tmp;
			a[tmp%p]++;
		}
		cout<<"Case #"<<tc<<": ";
		if(p==2)
			cout<<a[0] + a[1]/2 + a[1]%2 <<endl;
		if(p==3){
			int tmp = min(a[2],a[1]);
			a[1] -= tmp; a[2] -= tmp;
			cout<<a[0] + tmp + (a[1]+a[2])/3 + ((a[1]+a[2])%3 != 0)<<endl;
		}
	}
	return 0;
}

