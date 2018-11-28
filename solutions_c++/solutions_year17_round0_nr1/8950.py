#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<ll> vl;

#define MOD 1000000007
#define tc int t;scanf("%d",&t);while(t--)
#define pb push_back
#define ff(i,a,b) for(int i=a;i<b;i++)
#define mp make_pair
#define pf printf
#define sf scanf
#define bs binary_search
#define nl printf("\n")
#define si(x) int x;scanf("%d",&x)
#define sll(x) ll x;scanf("%lld",&x)
#define pi(x) printf("%d\n",x )

int main()
{
	int p=1;
	    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
	tc
	{
		string s;
		cin>>s;
		si(k);
		int i=0,count=0;
		while(s[i]!='\0')
		{
			if(s[i]=='-')
			{
				if(i+k>s.length())
					break;
				for(int j=i;j<k+i;j++)
				{
					if(j==s.length())
						break;
					if(s[j]=='-')
						s[j]='+';
					else if(s[j]=='+')
						s[j]='-';

				}
				count++;
			}
			//cout<<"s[i]="<<s[i]<<endl;
			i++;
		}
		i=0;
		int flag=1;
		while(s[i]!='\0')
		{
			if(s[i]=='-')
				flag=0;
			i++;
		}
		cout<<"Case #"<<p<<": ";
		if(flag==1)
			cout<<count<<"\n";
		else
			cout<<"IMPOSSIBLE\n";
		p++;
	}
	return 0;
}