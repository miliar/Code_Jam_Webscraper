#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=(a);i<=(b);i++)
#define ll long long
#define pll pair<ll, ll>
#define pii pair<int,int>
#define pb push_back
#define F first
#define S second
#define mod 1000000007
#define maxn 100005
#define boost ios::sync_with_stdio(false);cin.tie(0)
#define fr freopen("source.txt","r",stdin),freopen("output.txt","w",stdout)
#define SET(a,b) memset(a,b,sizeof(a))

int main(){
	boost;
	
	int t;
	cin>>t;
	rep(tc,1,t){
		cout<<"Case #"<<tc<<": ";
		ll n;
		cin>>n;
		if(n<10){
			cout<<n<<endl;
			continue;
		}
		vector<int>dig;
		while(n>0){
			dig.pb(n%10);
			n/=10;
		}
		reverse(dig.begin(), dig.end());
		int ind=-1;
		rep(i,0,dig.size()-2){
			if(dig[i+1]<dig[i]){
				ind=i;
				break;
			}
		}
		if(ind==-1){
			rep(i,0,dig.size()-1)cout<<dig[i];
			cout<<endl;
			continue;
		}
		int x=dig[ind];
		int j=-1;
		for(int i=ind;i>=0;i--){
			if(x!=dig[i])break;
			dig[i]--;
			j=i;
		}
		vector<int>ans;
		for(int i=0;i<=j;i++)ans.pb(dig[i]);
		for(int i=j+1;i<dig.size();i++)ans.pb(9);
		while(ans[0]==0)ans.erase(ans.begin());
		rep(i,0,ans.size()-1)cout<<ans[i];
		cout<<endl;
	}


	return 0;
}