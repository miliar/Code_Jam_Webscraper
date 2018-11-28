#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <queue>
#include <cstring>
#include <map>
#include <set>
#include <algorithm>

# define ini(c) int c; scanf("%d",&(c))
# define outi(c) printf("%d \n",(c)) 
# define rf freopen("input.in","r",stdin)
# define wf freopen("output.txt","w",stdout)
# define pb(c) push_back(c)
# define mp(c,d) make_pair(c,d)
# define all(c) (c).begin(),(c).end()
# define tr(c,i) for(typeof((c).begin()) i=(c).begin();i!=(c).end();i++)

using namespace std;

typedef vector< int > vi;
typedef vector< vi > vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef long long ll;

int main()
{
    rf;wf;
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		int ans=0;
		for(int i=0;i<=(s.length()-k);i++)
		{
			if(s[i]=='-')
			{
				for(int j=0;j<k;j++)
				{
					if(s[i+j]=='-') s[i+j]='+';
					else			s[i+j]='-';
				}
				ans++;
			}
		}
		int flag=0;
		for(int i=(s.length()-k+1);i<s.length();i++)
		{
			if(s[i]=='-') flag=1;
		}

		if(flag==1) cout<<"Case #"<<test<<": IMPOSSIBLE"<<endl;
		else		cout<<"Case #"<<test<<": "<<ans<<endl;
	}
}
