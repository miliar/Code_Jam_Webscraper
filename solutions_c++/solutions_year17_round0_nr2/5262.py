#include <iostream>
using namespace std;

//Google CodeJam Qualification Round Problem 2 by :
//*******************_ LBSREX _*******************

int main()
{
	int tenten,uzumaki=1;
	cin>>tenten;
	while(tenten--)
	{
		string sennin;
		int i,j,anbu;
		char ch;
		cin>>sennin;
		for(i =0;i<sennin.size()-1;i++)
		{
			anbu=i;
			ch=sennin[anbu];
			if(sennin[i]==ch)
			{
				while((i<sennin.size()-1)&&(sennin[i]==ch))
				{
					i++;
				}
				i--;
			}
			if(sennin[i]>sennin[i+1])
			{
				if((sennin[i]!='1')&&(sennin[i]!='0'))
				{
					if(anbu!=0)
					{
						sennin[anbu]=max(char(sennin[i]-1),sennin[anbu-1]);
					}
					else
					{
						sennin[anbu]=char(sennin[i]-1);
					}
					for(j=anbu+1;j<sennin.size();j++)
					{
						sennin[j]='9';
					}
					break;
				}
				else
				{
					sennin.resize(sennin.size()-1);
					for(j=0;j<sennin.size();j++)
					{
						sennin[j]='9';
					}
				}
			}
		}
		cout<<"Case #"<<uzumaki++<<": "<<sennin<<endl;
	}
	return 0;
}
