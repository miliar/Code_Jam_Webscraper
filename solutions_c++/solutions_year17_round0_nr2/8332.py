#include<fstream>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
	ifstream cin("B-large.in");
	ofstream cout("out");
	int num;
	cin>>num;
	string str;
	for(int a=1;a<=num;a++)
	{
		cin>>str;
		bool is=0;
		while(!is_sorted(str.begin(),str.end()))
		{
			for(int i=0;i<str.size()-1;i++)
			{
				if(str[i]>str[i+1])
				{
					str[i]--;
					for(int j=i+1;j<str.size();j++)
					{
						str[j]='9';
					}
					break;
				}
			}
		}
		while(str[0]=='0')
			str.erase(str.begin());
		cout<<"Case #"<<a<<": "<<str<<"\n";
	}
}
