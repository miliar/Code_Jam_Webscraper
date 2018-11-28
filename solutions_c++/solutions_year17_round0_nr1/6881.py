#include<bits/stdc++.h>

using namespace std;

typedef long long int ll;

typedef vector <int> vi;
typedef vector <long> vl;
typedef vector <long long> vll;
typedef pair<int,int> pai;

typedef pair<int,string> pas;

typedef vector <pai> vpai;
typedef vector<pas > vpas;

const ll INF=ll(1e18);
const int MOD=1e9+7;


#define init(x) memset(x,0,sizeof(x))



int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	freopen("inu.in","r",stdin);
	freopen("outputf.txt","w",stdout);
	int t,p=1;
	cin>>t;
	while(p<=t)
	{
		cout<<"case #"<<p<<": ";
		string s,s1="";
		cin>>s;
		int n=s.length(),i=0,k,c=0;
		cin>>k;
		for (int i = 0; i < n; i++)
		{
			if(s[i]=='-' && i<=n-k)
			{
				for(int j=i;j<k+i;j++)
				{
					if(s[j]=='+')
					{
						s[j]='-';
					}
					else
					{
						s[j]='+';
					}
				}
				c++;
			}
		}
		std::size_t found=s.find('-');
		if (found!=std::string::npos)
		{
			cout<<"IMPOSSIBLE\n";
			//cout<<s<<"\n";
		}
		else
		{
			cout<<c<<"\n";
		}
		
		p++;
	}
}
