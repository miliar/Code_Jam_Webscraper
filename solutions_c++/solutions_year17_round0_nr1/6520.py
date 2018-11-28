#include <iostream>
#include <vector>
#include <string.h>
using namespace std;
#define f(i,n) for(int i=0;i<n;i++)
int main()
{
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
	int t;
	cin>>t;
	f(j,t)
	{
		string a;
		int k;
		cin>>a>>k;
		int l=strlen(a.c_str());

		int li=-k-1;
		int moves=0,all=1;

		vector<int >v;

		f(i,l)
		{
			if(a[i]=='-')	all=0;
			int s=v.size()-1,c=0;
			while(s>=0)
			{
				if(i-v[s]>=k)
					break;
				c++;
				s--;
			}
			if(c%2==1)
			{
				if(a[i]=='-')	a[i]='+';
				else			a[i]='-';
			}
			if(a[i]=='-')
			{
				moves++;
				li=i;
				v.push_back(i);
			}
		}
		cout<<"Case #"<<j+1<<": ";
		if(all==1)
			cout<<"0\n";
		else if(li<=l-k)
			cout<<moves<<"\n";
		else	cout<<"IMPOSSIBLE\n";
	}

	return 0;
}
