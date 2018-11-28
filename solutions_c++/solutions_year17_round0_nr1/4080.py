#include <string>
#include <iostream>

using namespace std;

bool proper(const string &str)
{
	for(unsigned int i=0; i<str.size(); ++i)
		if(str[i]!='+') return false;
	return true;
}

void flip(string &str, int s, const int &k)
{
	for(int i=0; i<k; ++i)
	{
		if(str[s+i]=='-')
			str[s+i]='+';
		else str[s+i]='-';
	}
}
int main()
{
	int t,k,res=0;
	cin >> t;
	
	string in;
	for(int i=0; i<t; ++i)
	{
		res=0;
		cin >> in >> k;
		if(k>0)
		{
			for(unsigned int j=0; j<in.size()-(k-1);++j)
			{
				if(proper(in)) break;
				else if(in[j]=='-')
				{
					++res;
					flip(in,j,k);
				}
			}
		}
		if(!proper(in))
			cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << i+1 << ": " << res << endl;	
	}
	return 0;
}
