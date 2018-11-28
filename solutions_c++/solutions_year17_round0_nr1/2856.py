#include <fstream>
#include <string>
using namespace std;

int solve(string& s, int k)
{
	int len = s.size();
	
	int ans = 0;
	while(1)
	{
		int i;
		for(i = 0;i < len;++i)
		{
			if(s[i] == '-')
			{
				break;
			}
		}
		if(i == len)
		{
			break;
		}
		if(i + k > len)
		{
			return -1;
		}
		for(int j = i;j < i + k;++j)
		{
			if(s[j] == '-')
			{
				s[j] = '+';
			}
			else
			{
				s[j] = '-';
			}
		}
		++ans;
	}
	
	return ans;
}

int main()
{
	ifstream in("A.in");
	ofstream out("A.out");

	int t;
	in >> t;
	
	for(int i = 0;i < t;++i)
	{
		string s;
		int K;
		
		in >> s >> K;
		int ans = solve(s, K);
		
		out<<"Case #"<<i + 1<<": ";
		if(ans == -1)
		{
			out<<"IMPOSSIBLE\n";
		}
		else
		{
			out<<ans<<"\n";
		}
	}
	
	in.close();
	out.close();
}
