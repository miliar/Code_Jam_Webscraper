#include <bits/stdc++.h>
 
using namespace std;
 
#define TEST(T) ll T; cin>>T; while(T--)
#define ll long long
#define F first
#define S second
#define pb push_back
#define pii pair<ll,ll>
#define all(V) V.begin(),V.end()
#define clr(V,val) memset(V,val,sizeof(V))
#define rf() freopen("in.txt","r",stdin)
#define wf() freopen("out.txt","w",stdout)


int main() {

	rf(); wf();
	
	ll cases=0;
	TEST(t)
	{

		string s;
		cin>>s;

		ll l,pos=-1,x;
		l=s.size();

		for(x=0;x<l-1;x++)
		{
			if(s[x]>s[x+1])
			{
				pos=x;
				break;
			}
		}

		cout<<"Case #"<<++cases<<": ";
		if(pos==-1) cout<<s;
		else
		{
			if(s[pos]=='1')
			{
				for(x=0;x<l-1;x++) cout<<"9";
			}
			else
			{
				string ss="";
				s[pos]--;

				for(x=pos;x>=1;x--)
				{
					ll curr=s[x]-48;
					ll nxt=s[x-1]-48;
					
					if(curr<nxt) ss+="9",s[x-1]--;
					else ss+=(char)(curr+48);
				}
				ss+=s[0];

				reverse(all(ss));
				cout<<ss;
				//cout<<(ll)(s[pos])-49;
				for(x=pos+1;x<l;x++) cout<<"9";
			}
		}
			cout<<"\n";
		
	}

}