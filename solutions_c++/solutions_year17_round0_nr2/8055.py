#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
using namespace std;
long long f(long long n)
{
	int dig;
	string s="";
	long long n1 = n;
	while (n != 0)
	{
		dig= n% 10;
		n /= 10;
		s += dig + '0';
	}
	reverse(s.begin(), s.end());
	
	bool t= true;
	for (int i = 1; i < s.size(); ++i)
	{
		if (s[i] <s[i-1] && s[i - 1]=='1')
		{
			s.pop_back();
			for (int j = 0; j < s.size(); ++j)
				s[j] = '9';
			
			break;
		}
		if (s[i] < s[i - 1])
		{
			s[i] = '9';
			if (t)
			{
				s[i - 1] = s[i - 1] - 1;
				t = false;
			}
			for (int j = i - 1; j >= 1; --j)
			{
				if (s[j] < s[j - 1])
				{
					s[j] = '9';
					s[j - 1] = s[j - 1] - 1;
				}
			}
		}
	}
	long long ans = 0;
	long long j = 1;
	for (int i = int(s.size()) - 1; i >= 0; --i)
	{
		ans += (s[i] - '0')*j;
			j *= 10;
	}
	return ans;
}
int main()
{
	int j = 1;
	ifstream inp  ("input.txt");
	ofstream out ("output.txt");
	long long ans;
	int t;
	inp >> t;
	while (t != 0)
	{
		long long n;
		inp >> n;
		ans = f(n);
		out << "Case #" << j << ": " <<ans<<endl;
		++j;
		--t;
	}
	

}