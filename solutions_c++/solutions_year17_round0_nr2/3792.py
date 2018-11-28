#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define N ((ll)2010)

ll t,n;

ifstream fin("input.in");
ofstream fout("output.txt");

int main()
{
	fin>>t;
	for(int q=1;q<=t;q++)
	{
		fin>>n;
		vector <ll> ex;
		while(n)ex.push_back(n%10),n/=10;
		reverse(ex.begin(),ex.end());
		string res="";
		for(int i=0;i<ex.size();i++)
		{
			bool flg=0;
			for(int j=i+1;j<ex.size();j++)
			{
				if(ex[j]>ex[i])break;
				if(ex[j]<ex[i])
					flg=1;
			}
			if(flg)
			{
				res+=(char)(ex[i]-1+'0');
				for(int j=i+1;j<ex.size();j++)res+='9';
				break;
			}
			res+=(char)(ex[i]+'0');
		}
		while(res[0]=='0')
		{
			string ex="";
			for(int i=1;i<res.size();i++)ex+=res[i];
			res=ex;
		}
		fout<<"Case #"<<q<<": "<<res<<"\n";
	}
	return 0;
}
