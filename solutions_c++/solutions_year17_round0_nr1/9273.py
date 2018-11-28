/*input
3
---+-++- 3
+++++ 4
-+-+- 4
*/
#include <bits/stdc++.h>
using namespace std;
#define lint long long
#define inf LLONG_MAX
#define fori(a,b) for(lint i=a;i<b;i++)
#define forj(a,b) for(lint j=a;j<b;j++)
typedef vector<int> vi;
#define pair < lint , lint > pii
#define pb(y) push_back(y)
#define cin fin
#define cout fout
int main() {
	// your code goes here
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in",ios::in);
	fout.open("output a.txt",ios::out);
	lint t;
	cin>>t;
	for(lint zx=1;zx<=t;zx++)
	{
		cout<<"Case #"<<zx<<": ";
		string s;
		cin>>s;
		lint arr[s.size()];
		fori(0,s.size())
		{
			if(s[i]=='+')
				arr[i]=1;
			else
				arr[i]=0;
		}
		lint k;
		cin>>k;
		lint c=0;
		fori(0,s.size()-k+1)
		{
			if(arr[i]==0)
			{
				c++;
				forj(i+1,i+k)
				{
					if(arr[j]==0)
						arr[j]=1;
					else
						arr[j]=0;
				}
			}
		}
		lint flag=0;
		fori(s.size()-k+1,s.size())
		{
			if(arr[i]==0)
				flag=1;
		}
		if(flag==1)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<c<<"\n";
		
	}
	return 0;
}