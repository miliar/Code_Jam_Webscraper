#include<bits/stdc++.h>
using namespace std;
#define fwd(i,a,b) for(i=a;i<b;i++)
#define rev(i,a,b) for(i=a;i>b;i--)
#define ll long long 
#define vll vector< long long > 
#define vi vector<int> 
#define pb push_back
#define pii pair<int,int> 
#define pll pair< ll , ll >
#define vpll vector< pll >
#define F first
#define S second
#define dbl double
#define str string
#define P2 3.14159265358979323846  /* pi */
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sd(t) scanf("%d",&t)
#define pd(t) printf("%d\n",t)
#define slld(t) scanf("%lld",&t)
#define plld(t) printf("%lld\n",t)
#define MOD 1000000007
#define gc getchar_unlocked 
#define pc putchar_unlocked
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll n,i,j,q,r,g,m,e,h,tt,s,l,z,x,y,x1,y1,k,t,p;
	dbl sg,fg,d,sig,nd;
	str a,b,c;
	cin>>t;
	fwd(tt,1,t+1)
	{
		cin>>n>>m;
		vector<string> v(n);
		vector<vll> ch(n);
		cout<<"Case #"<<tt<<": "<<endl;
		fwd(i,0,n)
		{
			cin>>v[i];
			fwd(j,0,m)
			{
				if(v[i][j]!='?')
					ch[i].pb(j);
			}
		}
		fwd(i,0,n)
		{
			if(ch[i].size()!=0)
			{
				fwd(j,0,ch[i].size())
				{
					fwd(k,ch[i][j]+1,m)
					{							
						if(v[i][k]!='?')
							break;
						else	
							v[i][k]=v[i][ch[i][j]];
					}
					rev(k,ch[i][j]-1,-1)
					{							
						if(v[i][k]!='?')
							break;
						else	
							v[i][k]=v[i][ch[i][j]];
					}
				}		
			}
		}
		vll st;
		fwd(i,0,n)
		{
			if(ch[i].size()!=0)
				st.pb(i);
		} 
		fwd(j,0,st.size())
		{
			fwd(k,st[j]+1,n)
			{							
				if(ch[k].size()!=0)
					break;
				else	
					v[k]=v[st[j]];
			}
			rev(k,st[j]-1,-1)
			{							
				if(ch[k].size()!=0)
					break;
				else	
					v[k]=v[st[j]];
			}
		}	
		fwd(i,0,n)
			cout<<v[i]<<endl;
	}
	return 0;
}	