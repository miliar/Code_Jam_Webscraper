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
int ch=-1,t;
int main()
	{
	cincout;
	ifstream cin;
	cin.open("B-large.in",ifstream::in);
	ofstream cout;
	cout.open("ans.out",ofstream::out);
	cin>>t;
	for(int j=1;j<=t;j++)
		{
		ch=-1;
		cin>>s;
		for(int i=1;i<s.length();i++)
			if(s[i-1]>s[i])
				{
				ch=i-1;
				break;
				}
		for(int i=ch;i>=0;i--)
			if(s[i]==s[ch])
				ch=i;
		cout<<"Case #"<<j<<": ";
		if(ch==-1)
			cout<<s<<endl;
		else if(s[ch]=='1')
			{
			for(int i=0;i<s.length()-1;i++)
				cout<<9;
			cout<<endl;
			}
		else
			{
			for(int i=0;i<s.length();i++)
				{
				if(i<ch)
					cout<<s[i];
				else if(i==ch)
					cout<<(char)(s[i]-1);
				else
					cout<<9;
				}
			cout<<endl;
			}
		}
  	return 0;
  	}