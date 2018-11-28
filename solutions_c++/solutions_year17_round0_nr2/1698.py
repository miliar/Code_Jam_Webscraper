/*********** [ scopeInfinity ] ******************/
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef std::vector<ll> vll;
typedef std::vector<int> vi;

#define forv(it,m) for (auto it = (m).begin(); it != (m).end(); ++it)
#define rep(i,n) for (int i=0;i<n;i++)
#define endl '\n' 
#define mp make_pair
#define pb(x) push_back((x))
#define what_is(x) cerr << #x << " is " << (x) << endl;

ll MOD = 1e9+7/4;
ll INF = LLONG_MAX/4;

vector<string> &split(const std::string &s, char delim, vector<string> &e) {
    stringstream ss(s);
    string item;
    while(getline(ss, item, delim))
        e.push_back(item);
    return e;
}


ll Pow(ll a ,ll b ,ll Mo){
    ll ans = 1;
    for (; b; b >>= 1, a = a * a % Mo)
        if (b&1) ans = ans * a % Mo;
    return ans;
}

vector<int> Zfunc(string &s) {
    int n=s.length();
    vector<int> z(n,0);
    for(int i=1,l=0,r=0;i<n;i++) {
        if(i<=r) 
            z[i] = min(z[i-l],r-i+1);
        while(i+z[i]<n && s[i+z[i]]==s[z[i]])
            z[i]++;
        if(r<i+z[i]-1)
            l=i,r=i+z[i]-1;
    }
    return z;
}

ll solve() {
	string s;
	cin>>s;
	int j=  s.length();
	for (int i = s.length()-1; i >=1; --i)
	{
		if(s[i-1]>s[i]) {
			j=i-1;
			assert(s[i-1]>'0');
			s[i-1]--;
		}
	}
	for (int i = j+1; i < s.length(); ++i)
	{
		s[i]='9';
	}
	if(s[0]=='0')
		s=s.substr(1);
	assert(s.length()==1 || s[0]!='0');
	cout<<s;
	
	return 0;
}

int main(int argc, char const *argv[])
{
	std::ios::sync_with_stdio(false);cin.tie(0);
	// cout<<fixed<<setprecision(1);
	
	
	int T;
	cin>>T;
	for (int i = 0; i < T; ++i)
	{
			cout<<"Case #"<<i+1<<": ";
			solve();
			cout<<endl;
	}
	

	return 0;
}

