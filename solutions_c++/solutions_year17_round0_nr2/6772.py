#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ofstream out("AnswerB.out");
	ifstream in("QuestionB.in");
	int t=0,i=0,j=0,k=0,n=0;
	string s;
	in>>t;
	for(k=1;k<=t;k++)
	{
		in>>s;
		n=s.length();
		for(i=0;i<n-1;i++)
		{
			if(s[i+1]<s[i])
			{
				j=i;
				while(s[i]==s[i-1]&&i>0)
				{
					i--;
				}
				s[i]--;
				for(j=i+1;j<n;j++)
				{
					s[j]='9';
				}
			}
		}
		//out<<s<<" ";
		i=0;
		while(s[i]=='0')
		{
			i++;
		}
		out<<"Case #"<<k<<": "<<&s[i]<<endl;
	}
	return 0;
}
