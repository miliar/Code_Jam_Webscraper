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
		string s;
		int k;
		cin>>s>>k;
		int n=s.size();
		s='$'+s;
		int cnt=0;
		rep(i,1,n-k+1){
			if(s[i]=='+')continue;
			cnt++;
			rep(j,i,i+k-1){
				if(s[j]=='+')s[j]='-';
				else s[j]='+';
			}
			//cout<<i<<" "<<s<<endl;
		}
		int f=0;
		//cout<<s<<endl;
		rep(i,1,n)if(s[i]=='-')f=1;
		if(f==1)cout<<"IMPOSSIBLE\n";
		else cout<<cnt<<"\n";
	}

	return 0;
}