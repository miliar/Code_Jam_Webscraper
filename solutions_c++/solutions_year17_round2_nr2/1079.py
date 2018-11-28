#include<bits/stdc++.h>
using namespace std;

#define INF (int)1e9
#define EPS 1e-9

#define pb push_back
#define fill(a,v) memset(a, v, sizeof a)
#define sz(a) a.size()
#define mp make_pair

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef map<int,int> mii;

int t,n,m,x,y;

int r,o,g,b,v;
char temp;

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		cin>>n>>r>>o>>y>>g>>b>>v;
		printf("Case #%d: ",tc);
		if((r>b+y)||(b>r+y)||(y>b+r))
		{
			cout<<"IMPOSSIBLE\n";
			continue;
		}
		char s[1001];
		fill(s,'0');
		int i=0;
		while(r--)
		{
			s[i]='R';
			i+=2;
		}

		for(i=0;s[i]!='0';i++);
		while(y--)
		{
			s[i]='Y';
			i+=2;
		}

		for(i=0;s[i]!='0';i++);
		while(b--)
		{
			if(i>=n)
			{
				x=i%n;
				temp=s[x];
				s[x]='B';
				for(int j=0;j<n;j++)
				{
					if(s[j]=='0')
					{
						s[j]=temp;
						break;
					}
				}
				i+=2;
				continue;
			}
			s[i]='B';
			i+=2;
		}
		for(int i=0;i<n;i++)
		{
			cout<<s[i];
		}
		cout<<endl;
	}
	return 0;	
}