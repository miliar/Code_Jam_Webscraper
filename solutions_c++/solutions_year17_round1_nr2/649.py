#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(lli i=(lli)a;i<=(lli)b;i++)
#define endl "\n"
#define mp make_pair
#define X first
#define Y second
#define inf 1e18
#define mod 1000000007
#define pb push_back
#define pi 3.14159265359
#define gc getchar
#define Case cout<<"Case #"<<++cas<<": ";
#define fastio ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define all(v) v.begin(),v.end()
// #define lli int
typedef long long int lli;
typedef pair<int,int> pii;
typedef pair<lli,int> pli;
typedef vector<pii> vii;
typedef pair<lli,lli> pll;
typedef vector<lli> vl;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vl> vvl;

#define pr(...) dbs(#__VA_ARGS__, __VA_ARGS__)
template <class T> void dbs(string str, T t) {cerr << str << " : " << t << "\n";}
template <class T, class... S> void dbs(string str, T t, S... s) {int idx = str.find(','); cerr << str.substr(0, idx) << " : " << t << ","; dbs(str.substr(idx + 1), s...);}
template <class S, class T>ostream& operator <<(ostream& os, const pair<S, T>& p) {return os << "(" << p.first << ", " << p.second << ")";}
template <class T>ostream& operator <<(ostream& os, const vector<T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class T>ostream& operator <<(ostream& os, const set<T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class S, class T>ostream& operator <<(ostream& os, const map<S, T>& p) {os << "[ "; for (auto& it : p) os << it << " "; return os << "]";}
template <class T> void prc(T a, T b) {cerr << "["; for (T i = a; i != b; ++i) {if (i != a) cerr << ", "; cerr << *i;} cerr << "]\n";}

lli R[60],ind[60];
lli Q[60][60],n;

// bool poss1(lli x)
// {
// 	double a=R[1];
// 	double bs=(double)x*10.0/(9.0*a);
// 	double as=(double)x*10.0/(11.0*a);
// 	lli b=ceil(as);
// 	lli c=floor(bs);
// 	if(c>=b) return 1;
// 	return 0;
// }

// bool poss2(lli x,lli y)
// {
// 	double a=R[1];
// 	double b=R[2];
// 	double bs1=(double)x*10.0/(9.0*a);
// 	double as1=(double)x*10.0/(11.0*a);
// 	double bs2=(double)y*10.0/(9.0*b);
// 	double as2=(double)y*10.0/(11.0*b);
// 	lli b1=ceil(as1);
// 	lli c1=floor(bs1);
// 	lli b2=ceil(as2);
// 	lli c2=floor(bs2);
// 	if(b1>c1 || b2>c2) return 0;
// 	if((b1>=b2 && b1<=c2) || (c1>=b2 && c1<=c2) || (b2>=b1 && b2<=c1) || (c2>=b1 && c2<=c1))
// 		return 1;
// 	return 0;
// }

bool poss()
{
	double mas=inf;lli mb=-1,mc=inf,index;
	FOR(i,1,n)
	{
		double a=R[i];lli x=Q[i][ind[i]];
		double bs=(double)x*10.0/(9.0*a);
		double as=(double)x*10.0/(11.0*a);
		if(as<mas) {index=i;mas=as;}
		lli b=ceil(as);
		lli c=floor(bs);
		mb=max(mb,b);
		mc=min(mc,c);
	}
	if(mc>=mb) return 1;
	ind[index]++;
	return 0;
}

int main()
{
	lli T,p,cas=0;
	cin>>T;
	while(T--)
	{
		bool flag=0;
		lli ans=0,fans=0;vl v;
		cin>>n>>p;
		FOR(i,1,n)
		cin>>R[i];
		FOR(i,1,n)
		FOR(j,1,p)
		cin>>Q[i][j];
		FOR(i,1,n)
		sort(Q[i]+1,Q[i]+p+1);
		FOR(i,1,n)
		ind[i]=1;
		while(1)
		{
			FOR(i,1,n)
			if(ind[i]==p+1)
			{
				flag=1;break;
			}
			if(flag) break;
			if(poss())
			{
				fans++;
				FOR(i,1,n)
				ind[i]++;
			}
		}
		Case;
		cout<<fans<<endl;
		// if(n==1)
		// {
		// 	FOR(i,1,p)
		// 	if(poss1(Q[1][i]))
		// 		ans++;
		// 	Case;
		// 	cout<<ans<<endl;
		// }
		// else if(n==2)
		// {
		// 	FOR(i,1,p)
		// 	v.pb(i);
		// 	do{
		// 		ans=0;
		// 		FOR(i,0,v.size()-1)
		// 		if(poss2(Q[1][i+1],Q[2][v[i]]))
		// 			ans++;
		// 		fans=max(fans,ans);
		// 	} while(next_permutation(v.begin(),v.end()));
		// 	Case;
		// 	cout<<fans<<endl;
		// }
	}
}