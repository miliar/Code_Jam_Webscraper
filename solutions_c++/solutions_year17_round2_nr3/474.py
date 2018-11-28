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
	ll N,Q;
	cin>>N>>Q;
	std::vector<pair<ll,ll> > C(N);
	for (int i = 0; i < N; ++i)
	{
		cin>>C[i].first>>C[i].second;
	}
	std::vector<std::vector<ll> > D(N,std::vector<ll>(N,2));
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < N; ++j)
		{
			cin>>D[i][j];
		}
	}
	for (int k = 0; k < N; ++k)
	{
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < N; ++j)
			if(D[i][k]!=-1 && D[k][j]!=-1 )
			{
				if(D[i][j]==-1)
					D[i][j]=D[i][k]+D[k][j];
				else
					D[i][j]=min(D[i][j],D[i][k]+D[k][j]) ;
			}
		}
	}
	for (int i = 0; i < Q; ++i)
	{
		ll s,d;
		cin>>s>>d;
		
		s--;
		d--;

		std::vector<ld> timeh(N,INF);
		timeh[s]=0;
		priority_queue<pair<ld,int> ,vector<pair<ld,int> >,greater<pair<ld,int> > > q;
		q.push(mp((ld)0,s));
		std::vector<int> marked(N,0);
		while(!q.empty()) {
			int current = q.top().second;
			q.pop();
			if(marked[current])
				continue;
			marked[current]=1;
			for (int j = 0; j < N; ++j)
			if(D[current][j]!=-1) {
				ld traveltime = ((ld)D[current][j])/((ld)C[current].second);
				if(timeh[j]>timeh[current]+traveltime && D[current][j]<=C[current].first) {
					timeh[j]=timeh[current]+traveltime;
					assert(!marked[j]);
					q.push(mp(timeh[j],j));
				}
			}
		}

		// timeh[s]=0;
		// for (int i = 0; i < N-1; ++i)
		// {
  //         assert(d!=-1);
  //         ll cantravel = C[i].first;
  //         int j=i+1;
  //         ld timemore = 0;
  //         while(cantravel>0 && j<N) {
  //         	cantravel-=D[j-1][j];
  //         	// cerr<<cantravel<<" from "<<i<<" to "<<j<<endl;
  //         	if(cantravel<0)
  //         		break;
  //         	timemore+=((ld)D[j-1][j])/((ld)C[i].second);
  //         	if(timeh[j]==-1 || timeh[j]>timemore+timeh[i]) {
  //         		timeh[j]=timemore+timeh[i];
  //         		// cerr<<"+"<<(D[j-1][j])<<"/"<<((ld)C[i].second)<<" from city "<<i<<" to "<<j<<endl;
          	
  //         	}
  //         	j++;
  //         }
  //         // cerr<<timeh[i]<<"Done for "<<i<<endl;
		// }
		cout<<timeh[d]<<' ';
	}
	
	return 0;
}

int main(int argc, char const *argv[])
{
	std::ios::sync_with_stdio(false);cin.tie(0);
	cout<<fixed<<setprecision(10);
	
	
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

