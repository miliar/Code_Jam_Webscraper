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
	freopen("A-large.in","r",stdin);
	freopen("optest.txt","w",stdout);
	int t;
	cin>>t;
	int l=0;
	while(t--)
	{
		
		string s;
		cin>>s;
		int k;
		cin>>k;
		string s1=s;
		for(int i=0;i<s.length();i++)
			s1[i]=s[s.length()-1-i];
		bool c1,c2;
		c1=c2=1;
		int m1,m2;
		m1=m2=0;
		for(int i=0;i<s.length();i++)
		{
				if(i+k-1==s.length())
				{
					for(int j=i;j<i+k-1;j++)
					{
						if(s[j]=='-')
							c1=0;
					}
					break;
				}
				else
				{
					if(s[i]=='-')
					{
						m1++;
					//	trace2(i,s[i]);
						for(int j=i;j<i+k;j++)
						{
							if(s[j]=='-')
								s[j]='+';
								else
									s[j]='-';
						}
					}
				}
		}
		int ans;
		if(!c1)
		{
		for(int i=0;i<s.length();i++)
			s1[i]=s[s.length()-1-i];
		for(int i=0;i<s1.length();i++)
		{
				if(i+k-1==s1.length())
				{
					for(int j=i;j<i+k-1;j++)
					{
						if(s1[j]=='-')
							c2=0;
					}
					break;
				}
				else
				{
					if(s1[i]=='-')
					{
						m2++;
					//	trace2(i,s1[i]);
						for(int j=i;j<i+k;j++)
						{
							if(s1[j]=='-')
								s1[j]='+';
								else
									s1[j]='-';
						}
					}
				}
		}
		if(c2)
			ans=m1+m2;
			else
				ans=-1;
		
		}
		else
			ans=m1;
		
		
		
				l++;
		if(ans!=-1)
			cout<<"Case #"<<l<<": "<<ans;
			else
				cout<<"Case #"<<l<<": IMPOSSIBLE";
				cout<<endl;
		
	}
	
	return 0;
}

