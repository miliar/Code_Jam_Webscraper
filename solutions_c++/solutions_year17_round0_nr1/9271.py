#include<bits/stdc++.h>
using namespace std;
int main()
{
    	/*ifstream input;
	input.open("B-small-attempt1.doc");
	ofstream output;
	output.open("udit");*/
	int t;
	cin>>t;
	int k;
	for(k=1;k<=t;k++)
	{

		string s;
		cin>>s;
		int m;
		cin>>m;
		int pussy=0;
		int udit=0;
		//cout<<"slength= "<<s.length()<<endl;
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='-' && s.length()-i>=m)
			{
				pussy++;
				for(int j=i;j<i+m;j++)
				{
					if(s[j]=='-')
					{
						s[j]='+';
					}
					else
					{
						s[j]='-';
					}
				}
			}
		}

		for(int i=0;i<s.length();i++)
		{
		    //cout<<s[i];
			if(s[i]=='+')
			{
				udit++;
			}
		}
		if(udit==s.length() && pussy==0)
		{
			cout<<"Case #"<<k<<": "<<"0"<<endl;
		}
		else if(udit==s.length() && pussy>0)
		{
			cout<<"Case #"<<k<<": "<<pussy<<endl;
		}
		else
		{
			cout<<"Case #"<<k<<": "<<"IMPOSSIBLE"<<endl;
		}
	}
}
