#include <bits/stdc++.h>
using namespace std;

#define   f(i,n) 			for(int i=0;i<(n);i++)
#define   ff(i,n)           for(int i=1;i<=(n);i++)
#define   m0(X) 			memset((X), 0, sizeof((X)))
#define   m1(X) 			memset((X), -1, sizeof((X)))
#define   pb(x) 			push_back(x)
#define   mx 				9999999999999
#define   ay                100005
#define   rt                return 0
#define   sr(x,n)           sort(x+1,x+n+1)
#define   sv(v)             sort(v.begin(),v.end())
typedef long long ll;
typedef unsigned long long ull;

const double pi = acos(-1.0);
const int mod = 1000 * 1000 * 1000 + 7;
const ll inf = 1e18;


int main()
{
	int t,c=1;
	cin>>t;
	string s;
		ofstream out;
		out.open("file.txt");
	while(t--){
		cin>>s;
		if(s.size()==1){
			out<<"Case #"<<c++<<": "<<s<<"\n";
			continue;
		}
		int a=s.size();
		for(int i=a-1;i>=1;i--){
			if(s[i]<s[i-1]){
				s[i-1]=s[i-1]-1;
				for(int j=i;j<a;j++)s[j]='9';
			}
		}
		string s2;
		if(s[0]!='0') s2=s;
		else{
		
		for(int i=1;i<s.size();i++){
			s2+=s[i];
		}
	}
	out<<"Case #"<<c++<<": "<<s2<<"\n";
	}
}
