#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define scan(x) scanf("%d",&x)
#define scanll(y) scanf("%lld",&y)
#define print(x) printf("%d\n",x)
#define printll(y) printf("%lld\n",y)

typedef pair<int,int>pii;
const int maxn=2e5+55;

ll n;

int main() {
	freopen("Task.in","r",stdin);freopen("Task.out","w",stdout);
	int t;
	scan(t);
	for(int j=1 ; j<=t ; j++) {
		string s;
		cin>>s;
		ll sz=s.size();
		ll a[sz+5];
		for(ll i=0 ; i<sz ; i++) {
			a[i]=s[i]-'0';
		}
		ll lev=-1;
		for(ll i=sz-1 ; i>0 ; i--) {
			if(a[i]<a[i-1]) {
				a[i]=9;
				a[i-1]--;
				lev=i;
			}
		}
		cout<<"Case #"<<j<<": ";
		if(lev!=-1) {
			if(a[0]!=0)
			{
				for(ll i=0 ; i<=lev ; i++)
					cout<<a[i];
				for(ll i=lev+1 ; i<sz ; i++)
					cout<<"9";
			}
			else
			{
				for(ll i=1 ; i<=lev ; i++)
					cout<<a[i];
				for(ll i=lev+1 ; i<sz ; i++)
					cout<<"9";
			}
		}
		else {
			for(ll i=0 ; i<sz ; i++) 
				cout<<a[i];
		}
		cout<<"\n";
	}
}