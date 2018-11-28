#include <bits/stdc++.h>
using namespace std;

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define Max(x,y,z) max(x,max(y,z))
#define Min(x,y,z) min(x,min(y,z))
#define fr(i,s,e) for(i=s;i<e;i++)
#define rf(i,s,e) for(i=s-1;i>=e;i--)
#define pb push_back
#define eb emblace_back
#define mp make_pair
#define ff first
#define ss second
#define ll long long
#define trace1(x)                cerr<<#x<<": "<<x<<endl
#define trace2(x, y)             cerr<<#x<<": "<<x<<" | "<<#y<<": "<<y<<endl
#define trace3(x, y, z)          cerr<<#x<<":" <<x<<" | "<<#y<<": "<<y<<" | "<<#z<<": "<<z<<endl
#define trace4(a, b, c, d)       cerr<<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<endl
#define trace5(a, b, c, d, e)    cerr<<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<" | "<<#e<< ": "<<e<<endl
#define trace6(a, b, c, d, e, f) cerr<<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<" | "<<#e<< ": "<<e<<" | "<<#f<<": "<<f<<endl
#define vl vector<long long>

#define vi vector<int> 
#define vii vector< vector<int> >
#define vll vector< vector<long long> >
#define vpi vector< vector<pair<ll,ll> > >  


bool less_vectors(const vector<int>& a,const vector<int>& b) 
{   return a.size() > b.size();
}
class CompareDist
{
public:
    bool operator()(pair<int,int> p1,pair<int,int> p2)
	{
        	
		if(p1.ss-p1.ff!=p2.ss-p2.ff)
		return p1.ss-p1.ff<p2.ss-p2.ff;
		else
			return p1.ff>p2.ff;
		
    }
};
 
int main()
{
	IOS;
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("stalloutput2.txt","w",stdout);
	int t;
	cin>>t;
	int l=0;
	while(t--)
	{
		int n,k;
		cin>>n>>k;
		priority_queue<pair<int,int>,vector<pair<int,int> > ,CompareDist> pq;
		ll cnt=0;
		int ansl,ansr;
		pq.push(mp(1,n+2));
		while(!pq.empty())
		{
			int l=pq.top().ff;
			int r=pq.top().ss;
			pq.pop();
			if(l-r==1)
				break;
			int a=(r-l)/2;
			if(l+a==r-a)
			{
				cnt++;
				if(cnt==k)
				{
					ansl=a-1;
					ansr=a-1;
					break;
				}
				else
				{
					pq.push(mp(l,l+a));
					pq.push(mp(l,r-a));
				}
			}
			else{
				cnt++;
				if(cnt==k)
				{
					ansl=a-1;
					ansr=a;
					break;
					
				}
				else
				{
					pq.push(mp(l,l+a));
					pq.push(mp(l+a,r));
				}
			}
		}
		l++;
		cout<<"Case #"<<l<<": "<<max(ansl,ansr)<<" "<<min(ansr,ansl)<<endl;
	}
	
	return 0;
}

