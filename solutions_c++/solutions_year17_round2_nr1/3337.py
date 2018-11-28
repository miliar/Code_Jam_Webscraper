/******************************************************************
* Oh, Lord.                                                       *
* Oooh, You are so big... So absolutely huge.                     *
* Gosh, We're all really impressed down here, I can tell you.     *
* Forgive us, Oh Lord, for this our dreadful toadying... and bare-*
* faced flattery.                                                 *
* But you're so strong and, well just so... super.                *
* Fantastic.                                                      *
******************************************************************/
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
#define forr(i, n) for(int i=0;i<(n);i++)
#define forv(i, v) for(int i=0;i<(int)v.size();i++)
#define fords(it, ds) for(auto it = ds.begin();it!=ds.end();it++)
#define OO (ll)1e18
#define fr first
#define se second
#define II pair<int, int>
#define pb push_back
#define dist(x,y,xx,yy) sqrt((x-xx)*(x-xx)+(y-yy)*(y-yy))
ull gcd (ull a,ull b){ull c;while(a!=0){c=a;a=b%a;b=c;}return b;}
///////////////////// Solution Code

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	#ifndef ONLINE_JUDGE
	#ifdef _WIN64
	freopen("C:\\Users\\mamdouh\\Desktop\\a1.in","r",stdin);
	freopen("C:\\Users\\mamdouh\\Desktop\\A2.out","w",stdout);
	#elif __linux__
	freopen("/media/mamdouh/System/Users/Mamdouh/Desktop/a1.in","r",stdin);
	freopen("/media/mamdouh/System/Users/Mamdouh/Desktop/A2.out","w",stdout);
	#endif
	#endif
	int T;
	cin>>T;
	for (int t=1;t<=T;t++)
	{
		cout<<"Case #"<<t<<": ";
		int D, n;
		cin>>D>>n;
		int k[n],s[n];
		double tim[n];
		forr(i,n)
		{
			cin>>k[i]>>s[i];
			tim[i]= (double)(D-k[i]) / s[i];
		}
		sort(tim,tim+n);
		double m= tim[n-1];
		cout<<fixed<<setprecision(6)<<D/m<<"\n";
		
	}
	return 0;
}
///////////////// Prayer
/******************************************************************
* Oh, Lord.                                                       *
* Oooh, You are so big... So absolutely huge.                     *
* Gosh, We're all really impressed down here, I can tell you.     *
* Forgive us, Oh Lord, for this our dreadful toadying... and bare-*
* faced flattery.                                                 *
* But you're so strong and, well just so... super.                *
* Fantastic.                                                      *
******************************************************************/
/////////////////This shouldn't be here
/*

///////////////////Union Find
struct UnionFind{
	vector<int> rank, parent;
	int forests;
	UnionFind(int n)
	{
		rank = vector<int>(n);
		parent = vector<int> (n);
		forests = n;
		for(int i=0;i<n;i++) parent[i]=i,rank[i]=1;
	}
	int find_set(int x)
	{
		if(parent[x] == x)
			return x;
		return parent[x]= find_set(parent[x]);
	}
	void link(int x, int y)
	{
		if(rank[x]>rank[y]) swap(x,y);
		parent[x] = y;
		if(rank[x] == rank[y]) rank[y]++;
	}
	bool union_sets(int x, int y)
	{
		x = find_set(x), y = find_set(y);
		if(x != y)
		{
			link(x,y);
			forests -- ;
		}
		return x!=y;
	}
};
*/
/*
///////////////////////////////EDGE
struct edge{
	int from,to;
	ll cost;
	edge(int from=0, int to=0, ll cost=0):from(from),to(to),cost(cost){}
	bool operator < (const edge & e )const{return cost>e.cost;}
};*/
/*struct edge{
	pair<int, int> from, to ;
	int cost;
	edge(pair<int, int> from = {0,0}, pair<int, int> to = {0,0} , int cost): from(from), to(to), cost(cost){}
	bool operator < (const edge & e) const{
		return cost > e.cost;
	}
	friend ostream& operator<<(ostream& os, const edge& e)  
	{  
    	os <<"[{"<<e.from.first<<","<<e.from.second<<"},{"<<e.to.first<<","<<e.to.second<<"},"<<e.cost<<"]";  
    	return os;  
	}  
};*/
/*
int Bullshit(int& l,int& r)
{
	int mid,cmp;B
	while(l<r)
	{
		mid=(l+r+1)>>1;
		if(good(mid))

			l=mid;
		}
		else
		{
			r=mid-1;
		
	}
    return mid;
}
*/
/*ull combi(ull n,ull k)
{
	ull ans=1;
	k=k>n-k?n-k:k;
	int j=1;
	for(;j<=k;j++,n--)
	{
		if(n%j==0)
		{
			ans*=n/j;
		}else
		if(ans%j==0)
		{
			ans=ans/j*n;
		}else
		{
			ans=(ans*n)/j;
		}
	}
	return ans;
}*/
/*
long long pw( long long base, long long power)
{
	if (power == 0) return 1;
	if (power % 2) return pw(base, power - 1)*base % 1000000007;
	if (power % 2 == 0) return pw((base*base) % 1000000007, power / 2);
}
*/
/*
ll lcm(ll a, ll b)
{
	ll temp = gcd(a, b);
	return temp ? (a / temp * b) : 0;
}
*/
/*int t,so,st,bo,bt;
	string s;
	cin>>t;
	while(t--)
	{
		cin>>s;
		so=st=bo=bt=0;
	}*/
		/*template <typename K, typename V>
bool comparePairs(const std::pair<K,V>& lhs, const std::pair<K,V>& rhs)
{
	if(lhs.first < rhs.first)
		return 1;
	if(lhs.se > rhs.se)
		return 1;
	return 0;
}*/
