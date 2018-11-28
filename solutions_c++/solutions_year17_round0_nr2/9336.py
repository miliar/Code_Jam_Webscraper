#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;
int main()
{
	int T;

	string line;

	cin>>T;
	for(int i=1;i<=T;i++)
	{
		vector<char> h;
		cin>>line;
		int num = stoi(line,nullptr,10);
		for(int j=0;j<line.length();j++)
		{
			h.push_back(line.at(j));
		}
		while(!is_sorted(h.begin(),h.end()))
		{
			num--;
			h.clear();
			string s = to_string((long long)num);
			for(int j=0;j<s.size();j++)
		{
			h.push_back(s.at(j));
		}
		}
		cout<<"Case #"<<i<<": "<<num<<endl;

	}
	
	return 0;
}