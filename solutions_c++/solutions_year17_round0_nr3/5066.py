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
		int n,k;
		cin>>n>>k;
		set<pair<int,pii> >s;
		s.insert({-n,{1,n}});
		rep(i,1,k-1){
			pii p=s.begin()->S;
			s.erase(s.begin());
			int l=p.F;
			int r=p.S;
			if(l==r){
				continue;
			}
			if(l+1==r){
				s.insert({1,{r,r}});
			}
			int mid=(l+r)/2;
			s.insert({-mid+l,{l,mid-1}});
			s.insert({-r+mid,{mid+1,r}});
		}
		pii p=s.begin()->S;	
		int l=p.F;
		int r=p.S;
		if(l==r){
			cout<<"0 0\n";
			continue;
		}
		if(l+1==r){
			cout<<"1 0\n";
			continue;
		}
		int mid=(l+r)/2;
		cout<<r-mid<<" "<<mid-l<<"\n";
	}

	return 0;
}