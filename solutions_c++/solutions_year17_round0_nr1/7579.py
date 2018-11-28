#include <bits/stdc++.h>
#define pb push_back
using namespace std;
typedef long long int ll;

int main(int argc, char const *argv[])
{
	int t,cs=1;
	cin>>t;
	ofstream ofile;
	ofile.open("out.txt",ios::out);
	while(t--)
	{
		string s;

		int k;
		cin>>s>>k;

		int i=0, count=0;
		bool np=0;
		while(i<s.size())
		{
			if(s[i]=='+')
				i++;
			else
			{
				if((i+k)>s.size())
				{
					np=1;
					// cout<<" For case "<<cs<<" "<<s<<endl;
					break;
				}
				count++;
				for(int z=i;z<i+k;z++)
				{
					s[z] = (s[z]=='+')?'-':'+';
				}
				i++;
			}
		}

		if(np)
			ofile<<"Case #"<<cs<<": IMPOSSIBLE\n";
		else
			ofile<<"Case #"<<cs<<": "<<count<<endl;
		cs++;
	}
	return 0;
}