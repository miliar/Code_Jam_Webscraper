#include <fstream>
#include <string.h>
#include <vector>

using namespace std;

int main(void)
{
	ifstream in;
	ofstream out;
	in.open("in.txt");
	out.open("out.txt");
	int t;
	in >> t;
	for(int q=1;q<=t;q++)
	{
		int n,tot=0;
		string tmp;
		in >> tmp >> n;
		for(int e=0;e<=tmp.size()-n;e++)
		{
			if(tmp[e]=='-')
			{
				for(int p=e;p<e+n;p++)
				{
					if(tmp[p]=='-') tmp[p]='+';
					else tmp[p]='-';
				}
				tot++;
			}
		}
		int check=0;
		for(int e=0;e<tmp.size();e++) if(tmp[e]=='-') check++;
		if(check==0) out << "Case #"<<q<<": "<<tot<<endl;
		else out << "Case #"<<q<<": IMPOSSIBLE"<<endl;
	}
}

