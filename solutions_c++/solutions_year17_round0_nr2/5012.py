#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int l=1;l<=t;l++)
	{
		string s;
		cin >> s;
		for(int j=0;j<s.length();j++)
		{
			int f1=0;
			for(int i=0;i<(s.length());i++)
			{
				//		cout << int(s[i]-'1') << endl;
				if(f1==1)
				{
					s[i]='9';
				}
				else if(int(s[i])>int(s[i+1]) && (i+1)<s.length())
				{

					f1=1;
					s[i]=int(s[i])-1;
					s[i+1]='9';
				}

			}
//			cout <<j << " " <<  s << endl;
		}
		int f2=0;
		cout << "Case #" << l << ": "; 
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='0' && f2==0)
			{
			}
			else
			{
				cout << s[i];
				f2=1;
			}
		}
		cout << endl;
	}
	return 0;
}
