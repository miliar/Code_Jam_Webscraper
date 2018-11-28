#include<bits/stdc++.h>

using namespace std;

string s;

bool slozen()
{
	for (int i=0; i<s.size(); ++i)
		if (s[i]=='-')return false;
	return true;
}

int main ()
{
	int t,k;
	cin >>t;
	for (int i=0; i<t; ++i)
	{
		cin >>s>>k;
		int p=0;
		string poc=s;
		cout <<"Case #"<<i+1<<": ";
		while (!slozen())
		{
			p++;
			int maks=0,makspos=0;
			for (int j=0; j<s.size()-k+1; ++j)
			{
				if (s[j]=='+')
					continue;
				//cout <<j<<endl;
				int tmp=0;
				for (int l=j; l<j+k; ++l)
				{
					if (s[l]!='+')tmp++;
				}
				if (tmp>maks)
				{
					maks=tmp;
					makspos=j;
				}
			}
			//cout <<maks<<endl<<makspos<<endl;
			for (int j=makspos; j<makspos+k; ++j)
			{
				if (s[j]=='+')s[j]='-';
				else s[j]='+';
			}
			//cout <<s<<endl;
			if (p>10000)
			{
				cout <<"IMPOSSIBLE"<<endl;
				break;
			}
		}
		if (p<10000 || slozen())cout <<p<<endl;
	}
	return 0;
}
