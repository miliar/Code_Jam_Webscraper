#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ofstream out("AnswerA.out");
	ifstream in("QuestionaA.in");
	int t=0,i=0,j=0,k=0,l=0,n=0,count=0;
	string s;
	in>>t;
	for(l=1;l<=t;l++)
	{
		out<<"Case #"<<l<<": ";
		count=0;
		in>>s>>k;
		n=s.length();
		for(i=0;i<n-k+1;i++)
		{
			if(s[i]=='-')
			{
				for(j=0;j<k;j++)
				{
					s[i+j]=88-s[i+j];
				}
				/*for(j=0;j<n;j++)
				{
					cout<<s[j];
				}
				cout<<endl;*/
				count++;
			}
		}
		/*for(j=0;j<n;j++)
		{
			cout<<s[j];
		}
		cout<<endl;*/	
		for(i=0;i<n;i++)
		{
			if(s[i]=='-')
			{
				break;
			}
		}	
		if(i==n)
		{
			out<<count<<endl;
		}
		else
		{
			out<<"IMPOSSIBLE"<<endl;
		}				
	}
	return 0;
}
