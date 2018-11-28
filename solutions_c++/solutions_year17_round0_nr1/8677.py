#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
    ifstream fin("A-large.in");
    ofstream fout("outfilelarge.out");
	int t;fin>>t;
	for(int it=1;it<=t;it++)
	{
		string st; int k, counter=0, flag=0;
		fin>>st>>k;
		for(int i=0;i<st.size()-k+1;i++)
		{
			if(st[i]=='-')
            {
				for(int j=i;j<i+k;j++)
				{
				    counter++;
					if(st[j]=='+')
						st[j]='-';
					else if(st[j]=='-')
						st[j]='+';
				}
            }
		}
		for(int i=0;i<st.size();i++)
		{
			if(st[i]=='-')
				flag=1;
		}
		if(flag==1)
        {
            fout<<"Case #"<<it<<": IMPOSSIBLE"<<endl;
        }

        else
            fout<<"Case #"<<it<<": "<<counter/k<<endl;
	}
	fin.close();
    fout.close();
	return 0;
}
