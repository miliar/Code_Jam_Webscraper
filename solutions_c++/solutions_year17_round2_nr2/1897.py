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
#define vpi vector< pair<ll,ll> >  >  
typedef pair<pair<int, int>,int> P;

 
bool less_vectors(const vector<int>& a,const vector<int>& b) 
{
   return a.size() > b.size();
}

int gcd(int a,int b)
{
	if(a%b==0)
		return b;
		else
			return gcd(b,a%b);
}
int main()
{
	
	freopen("B-small-attempt1.in","r",stdin);
	freopen("outbs2.txt","w",stdout);
	int l=0;
	int t;
	cin>>t;
	while(t--)
	{
		int n,r,o,y,g,b,v;
		cin>>n>>r>>o>>y>>g>>b>>v;
		string s="";
		if(r>(n/2)+(n%2) || y>(n/2)+(n%2) || b>(n/2)+(n%2))
			s="IMPOSSIBLE";
		else
		{
			map<int,char> m;
			int d,e,f;			
			m[0]=' ';
			if(r>=b && r>=y)
			{
				d=r;
				m[1]='R';
				if(b>y)
				{
						e=b;
						m[2]='B';
						f=y;
						m[3]='Y';
				}
				else
				{
						e=y;
						m[2]='Y';
						f=b;
						m[3]='B';
				}
			}
			else
			{
				if(y>=b && y>=r)
				{
				d=y;
				m[1]='Y';
				if(b>r)
				{
						e=b;
						m[2]='B';
						f=r;
						m[3]='R';
				}
				else
				{
						e=r;
						m[2]='R';
						f=b;
						m[3]='B';
				}
				}
				else
				{
					d=b;
				m[1]='B';
				if(y>r)
				{
						e=y;
						m[2]='Y';
						f=r;
						m[3]='R';
				}
				else
				{
						e=r;
						m[2]='R';
						f=y;
						m[3]='Y';
				}
				}
			
			}
			vi v(n,0);
			int cc=0;
			bool ch=1;
			int j=d,k=e,l=f;
			for(int i=0;i<d;i++)
			{
				if(cc>n-1)
				{
					ch=0;
					break;
				}
				v[cc]=1;
				cc+=2;
				
				j--;
			}
			cc=1;
			for(int i=0;i<e-f;i++)
			{
				if(cc>n-1)
				{
					ch=0;
					break;
				}
				v[cc]=2;
				cc+=2;
				k--;
			}
			cc=0;
			int pre=0;
			for(int i=0;i<n;i++)
			{
				if(v[i]==0)
				{
					if(pre)
						{v[i]=2;k--;}
					else
						{v[i]=3;l--;}
					pre=!pre;		
				}
			}
			
			for(int i=0;i<n;i++)
			{
				s=s+m[v[i]];
				if(i>0)
					if(s[i]==s[i-1] || s[i]==' ')
						ch=0;
			}
			if(s[0]==s[n-1])
				ch=0;
				if(j!=0 || k!=0 || l!=0)
					ch=0;
			if(ch==0)
				s="IMPOSSIBLE";
		}
		l++;
			cout<<"Case #"<<l<<": "<<s<<endl;
	}
	
return 0;
}
