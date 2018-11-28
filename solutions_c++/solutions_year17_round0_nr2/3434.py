#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<utility>
#define PB push_back
#define pii pair<int,int>
#define MP make_pair
#define sz size()
#define fi first
#define se second
using namespace std;
typedef long long ll;
int main()
{
	int t,i,j,k,cs,css;
	cin>>css;
	for(cs=1;cs<=css;cs++)
	{
		string s;
		cin>>s;
		while(1) {
			bool flag=false;
			for(i=1;i<s.sz;i++) {
				if(s[i-1]>s[i]) {
					flag=true;
					s[i-1]--;
					for(j=i;j<s.sz;j++)s[j]='9';
					break;
				}
			}			
			if(!flag)break;
		}
		ll ans=0;
		for(i=0;i<s.sz;i++) {
			ans*=10;
			ans+=(s[i]-'0');
		}
		cout<<"Case #"<<cs<<": ";
		cout<<ans<<endl;
	}
	return 0;
}
