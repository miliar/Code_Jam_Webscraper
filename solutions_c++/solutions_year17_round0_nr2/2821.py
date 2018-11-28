#include <fstream>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

unsigned long long solve(unsigned long long n)
{
	unsigned long long ans = 0;
	unsigned long long saven = n;
	
	vector<int> v;
	while(n)
	{
		v.push_back(n % 10);
		n /= 10;
	}
	
	reverse(v.begin(), v.end());
	int len = v.size();
	int index = -1;
	
	for(int i = 1;i < len;++i)
	{
		if(v[i - 1] > v[i])
		{
			index = i - 1;
			break;
		}
	}
	
	if(index == -1)
	{
		return saven;
	}
	else
	{
		int start = index;
		while(start > 0 && v[start] == v[start - 1])
		{
			--start;	
		}
		
		if(start == 0 && v[start] == 1)
		{
			for(int i = 0;i < len - 1;++i)
			{
				ans = 10 * ans + 9;
			}
		}
		else
		{
			for(int i = 0;i < start;++i)
			{
				ans = 10 * ans + v[i];
			}
			ans = 10 * ans + v[start] - 1;
			
			for(int i = start + 1;i < len;++i)
			{
				ans = 10 * ans + 9;
			}
		}
	}
	
	return ans;
}

int main()
{
	ifstream in("B.in");
	ofstream out("B.out");
	
	int t;
	in >> t;
	
	for(int i = 0;i < t;++i)
	{
		unsigned long long n;
		
		in >> n;
		unsigned long long ans = solve(n);
		out<<"Case #"<<i + 1<<": "<<ans<<"\n";
	}
	in.close();
	out.close();
}
