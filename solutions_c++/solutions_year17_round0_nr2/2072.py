#include<bits/stdc++.h>

# define ini(c) int c; scanf("%d",&(c))
# define outi(c) printf("%d \n",(c)) 
# define rf freopen("input.txt","r",stdin)
# define wf freopen("output.txt","w",stdout)
# define pb(c) push_back(c)
# define mp(c,d) make_pair(c,d)
# define all(c) (c).begin(),(c).end()
# define tr(c,i) for(typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
# define test(c) ini(c);while(c--)

using namespace std;

typedef vector< int > vi;
typedef vector< vi > vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef long long ll;

int main()
{
	rf;
	wf;
	int t;
	cin>>t;
	string s;
	int final[20];
	ll ans=0;
	int flag=0;
	ll target=0;
	for(int it=1;it<=t;it++)
	{
		flag=0;
		cin>>s;
		ans=s[0]-'1';
		for(int i=0;i<20;i++)final[i]=-1;
		for(int l=1;l<(s.length());l++)
			{
				ans=10*ans+9;
			}
		final[0]=s[0]-'0';
		for(int i=1;i<(s.length());i++)
		{
			if((s[i]-'0')<final[i-1]){
				flag=1;
				int x=i-1;
				while(final[x]==1 && x>0){
					x--;
				}
				if(x==0 && final[x]==1){
					target=-1;
				}
				else{
					while(final[x]==final[x-1] && x>1){
						x--;
					}
					if(x==1 && final[1]==final[0]){
						target=-1;
					}
					else{
					final[x]=final[x]-1;
					for(int j=x+1;j<s.length();j++)
					{
						final[j]=9;
					}
				}
				}
				i=30;
				break;
			}
			else{
				final[i]=s[i]-'0';
			}
		}
		if(target!=-1){
			target=0;
			for(int i=0;i<s.length();i++)
			{
				target=10*target+final[i];
			}
		}
		else{
			target=ans;
		}
		cout<<"Case #"<<it<<": "<<target<<endl;
	}
	
}
