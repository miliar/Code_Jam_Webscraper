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

string solve() {
	ll N,R, O, Y, G, B, V;
	cin>>N>>R>> O>> Y>> G>> B>> V;
	// cerr<<N<<endl;
	assert(O==0 && G==0 && V==0);

	std::vector<pair<int,char> > v;
	v.push_back(mp(R,'R'));
	v.push_back(mp(Y,'Y'));
	v.push_back(mp(B,'B'));
	sort(v.begin(),v.end());
	reverse(v.begin(),v.end());
	string s(4*N,'_');
	int offset = 0;
	for (int i = 0; i < 3; ++i)
	{
		if(i<=1)
		for (int k = 0; k < v[i].first; ++k)
		{
			s[k*4+i]=v[i].second;
		}
		else
		for (int k = 0; k < v[i].first; ++k)
		{
			s[((k+v[1].first)%v[0].first)*4+2]=v[i].second;
		}
			
	}
	string res = "";
	for (int i = 0; i < (int)s.length(); ++i)
	{
		if(s[i]!='_')
			res+=s[i];
	}
	// cerr<<res<<endl;

	assert(res.length()==N);
	if(res.length()<=1)
		return res;
	for (int i = 0; i < (int)res.length(); ++i)
	{
		if(res[i]==res[(i+1)%((int)res.length())]) {
			 return "IMPOSSIBLE";
			}
	}

	return res;
	


	
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
			cout<<solve();
			cout<<endl;
	}
	

	return 0;
}

