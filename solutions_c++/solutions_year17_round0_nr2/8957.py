#include <iostream>
#include <cmath>
#include <string>
using namespace std;

long long inf = (long long) pow(10, 18) + 2;
string process(string s)
{
	long long prev_min_index = inf;
	for(int i = 1; i < s.size();i++)
	{
		if(s[i] != s[i - 1])
		{
			if(s[i] < s[i - 1])
			{
				if(prev_min_index == inf)
				{
					prev_min_index = i - 1;
				}
				s[prev_min_index]--;
				for(int j = prev_min_index + 1;j < s.size();j++)
				{
					s[j] = '9';
				}
				break;
			}
			prev_min_index = inf;
		}
		else
		{
			prev_min_index = (prev_min_index < i - 1 ? prev_min_index : i - 1);
		}
	}
	return s;
}
int main()
{
	int t;
	freopen ("/Users/saravanakumars/Downloads/input_1.txt","r",stdin);
	freopen ("/Users/saravanakumars/Downloads/output_1.txt","w",stdout);
	cin>>t;
	for(int i = 1;i <= t;i++)
	{
		string g;
		cin>>g;
		cout<<"Case #"<<i<<": "<<stoll(process(g))<<endl;
	}
}
