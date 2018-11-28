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

bool ch(string s){
	rep(i,0,s.size()-1) if(s[i]=='-') return 0;
	return 1;
}

inline int solve(string s,int k){
	int ans=0;
	rep(i,0,s.size()-k){
		if(s[i]=='-'){
			ans++;
			for(int j=i;j<=i+k-1 && j<=s.size()-1;j++) s[j]=='-'?s[j]='+':s[j]='-';
		}
	}
	if(ch(s)) return ans;
	else return -1;
}


int main(){
	//fi;fo;
	fio;
	string s;
	int t,k,n;
	cin>>t;
	n=t;
	int ans;
	while(t--){
		cin>>s>>k;
		ans=solve(s,k);
		if(ans>=0)
			cout<<"Case #"<<n-t<<": "<<ans<<endl;
		else
			cout<<"Case #"<<n-t<<": "<<"IMPOSSIBLE"<<endl;
	}
	cout.flush();
	return 0;
}