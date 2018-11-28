#include<iostream>
#include<string>
#include<vector>
using namespace std;
int main(void)
{
	int T;
	cin>>T;
	for(int z = 1; z<= T; ++z)
	{
		string n;
		vector<int> x;
		string ans;
		
		cin>>n;
		for (int i=0;i<n.size();++i)
		{
			x.push_back(n[i]-'0');
		}
		
		int idx;
		for (idx = 0; idx < x.size() - 1; ++idx)
			if (x[idx] > x[idx+1])
				break;
		if (idx != x.size() -1)
		{
			for (; idx > 0; --idx)
			{
				if (x[idx] > x[idx-1])
					break;
			}
			x[idx]--;
			for (int i=idx+1;i<x.size();++i)
				x[i] = 9;
		}
		
		bool leading = true;
		for (int i=0;i<x.size();++i)
		{
			if (leading && x[i] == 0)
				continue;
			ans += (char)(x[i] + '0');
			leading = false;
		}
		cout << "Case #" << z << ": " << ans <<endl;
	}
}
