#include <bits/stdc++.h>
using namespace std;

#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define ms(a,val) memset(a,val,sizeof(a))
#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define chtoi(x) (int)((x)-'a')
#define rep(i,a,b) for(int i=(a);i<=(b);++i)
#define rrep(i,a,b) for(int i=(a);i>=(b);--i)
#define fi freopen("input.txt", "r+", stdin); 
#define fo freopen("output.txt", "w", stdout);
#define endl '\n'
#define MAX 1000000004
#define MOD 10000000007
#define fio ios::sync_with_stdio(0); cin.tie(0); 

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<vector<int> > vvi;
typedef pair<int, int> ii;
typedef vector<pair<int, int> > vii;
typedef vector<vector<pair<int, int> > > vvii;
//std::cout << std::setprecision(6) << std::fixed;

bool ch(string st){
	if(st.empty()) return 1;
	for(int i=0;i<st.size()-1;i++){ if(st[i]>st[i+1]) return 0;}
	return 1;
}


inline string solve(string st){
	int index=st.size()-1;
	while(true){
		if(ch(st)) return st;
		if(index>0 && st[index]<st[index-1]){
			rep(i,index,st.size()-1){ if(st[i]=='9') break; st[i]='9'; }
			st[index-1]--;
		}
		index--;
		while(!st.empty() && st[0]=='0'){ st.erase(0,1);}
	}
}


int main(){
	//fi;fo;
	fio;
	int t,k,n;
	cin>>t;
	n=t;
	string ans,s;
	while(t--){
		cin>>s;
		ans=solve(s);
		cout<<"Case #"<<n-t<<": "<<ans<<endl;			
	}
	cout.flush();
	return 0;
}