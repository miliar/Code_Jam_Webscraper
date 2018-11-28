#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ifstream I("A-large.in");
	ofstream O("A-large.out");
	string s;
	int cp,k;
	int cont;
	bool id=false;
	I>>cp;
	for(int t=1;t<=cp;t++)
	{
		id=false;
		I>>s>>k;
		cont=0;
		for(int i=0;i<=s.size()-k;i++)
		{
			if(s[i]=='-')
			{
				for(int j=i;j<i+k;j++)
				{
					if(s[j]=='+')
						s[j]='-';
					else
						s[j]='+';
				}
				cont++;
			}
		}
		for(int i=0;i<s.size();i++)
		{
			if(s[i]=='-')
			{
				O<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
				id=true;
				break;
			}		
		}
		if(!id)
			O<<"Case #"<<t<<": "<<cont<<endl;
	}
	return 0;
}