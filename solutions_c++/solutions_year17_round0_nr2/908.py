#include <fstream>
#include <string.h>
#include <vector>

using namespace std;
long long int dp[200][22],hap[81];
int main(void)
{
	ifstream in;
	ofstream out;
	in.open("in2.txt");
	out.open("out2.txt");
	int t;
	in >> t;
	for(int q=1;q<=t;q++)
	{
		string tmp,kk;
		in >> tmp;
		for(int e=0;e<tmp.size()-1;e++)
		{
			if(tmp[e]>tmp[e+1])
			{
				tmp[e]--;
				for(int p=e+1;p<tmp.size();p++) tmp[p]='9';
				for(int p=e;p>0;p--)
				{
					if(tmp[p-1]>tmp[p])
					{
					 	tmp[p]='9';
						tmp[p-1]--;
					}
				}
				break;
			}
		}
		if(tmp[0]=='0') 
		{
			for(int e=1;e<tmp.size();e++) kk+=tmp[e];
		}
		else
		{
			for(int e=0;e<tmp.size();e++) kk+=tmp[e];
		}
		out << "Case #"<<q<<": "<<kk<<endl;
	}
}

