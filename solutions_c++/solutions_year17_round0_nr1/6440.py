#include<iostream>
#include<vector>
#include<algorithm>
#include<string.h>
#include<cstdio>
#include<math.h>
#include<cstdlib>
#include<map>
#include<utility>
#include<stack>
#include<fstream>
#include<set>
#include<queue>
#include<iomanip>

using namespace std;
#define ll long long int
vector <ll> v;
vector <ll> v1;
vector <ll> v2;
const ll inf=100000000000005;

#define cincout ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define me(a,i) memset(a,i,sizeof(a))
#define mp make_pair
#define pb push_back
#define sortv(v) sort(v.begin(),v.end())
#define sortvd(v) sort(v.begin(),v.end(),greater<int>())
#define printv(n,v) for(int i=0;i<n;i++)  {cout<<v[i]<<" ";}
#define vin(v,n,a) for(int i=0;i<n;i++)	{v.pb(a);cin>>v[i];}
string s;
int k,co=0,t,no[1005];
int main()
	{
	//cincout;	
	ifstream cin;
	cin.open("A-large.in",ifstream::in);
	ofstream cout;
	cout.open("ans.out",ofstream::out);
	cin>>t;
	for(int j=1;j<=t;j++)
		{
		me(no,0);
		co=0;
		cin>>s>>k;
		for(int i=0;i<s.length();i++)
			{
			if(s[i]=='+')
				s[i]='1';
			else
				s[i]='0';
			}
		for(int i=0;i<s.length();i++)
			{
			if(i<k)
				{
				if(co%2==1)
					s[i] = (char)(1-(s[i]-'0')+'0');
				}
			else
				{
				if((no[i-1] - no[i-k]) %2==1)
					s[i] = (char)(1-(s[i]-'0')+'0');
				}
			if(s[i]=='1')
				{
				no[i]=co;
				continue;
				}
			no[i]=(++co);
			if(s.length()-i<k)
				{
				co=-1;
				break;
				}
			}
		cout<<"Case #"<<j<<": ";
		if(co==-1)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<co<<endl;
		}
  	return 0;
  	}