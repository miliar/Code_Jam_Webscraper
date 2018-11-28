#include<bits/stdc++.h>

#define fname "A-large"
#define pb push_back
#define mp make_pair
#define ss second
#define fff first

using namespace std;

typedef long double ld;
typedef long long ll;
const int maxn = (1e5) + 10;
const int INF = (1e9);
const ll inf = (1e18);
const double eps = (1e-9);
const ld PI = acos(-1);
int t,k,f,ff,fff,cur,ans,n;
string s;
int main() {    

	ios_base::sync_with_stdio(false);
    cin.tie(0);
	freopen(fname".in", "r", stdin);
	freopen(fname".out", "w", stdout);
	cin>>t;
	for(int tt=1;tt<=t;++tt){
		cout<<"Case #"<<tt<<": ";
		cin>>s>>k;
		n=s.size();
		ans=0;
		ff=0;
		while(true){
			f=1;
			for(int i=0;i<n;++i)
			if(s[i]=='-'){
				f=0;
				break;
			}
			if(f)
			break;
			for(int i=0;i<n;++i)
			if(s[i]=='-'){
				if(i+k>n){
					ff=1;
					break;
				}
				for(int j=i;j<i+k;++j){
					if(s[j]=='+')
					s[j]='-';
					else
					s[j]='+';
				}
				ans++;
				break;
			}
			/*
			for(int i=0;i<n;++i)
			cout<<s[i];
			cout<<"\n";
			*/
			if(ff)
			break;
		}
		if(ff)
		cout<<"IMPOSSIBLE";
		else
		cout<<ans;
		cout<<"\n";
	}
	return 0;
}



