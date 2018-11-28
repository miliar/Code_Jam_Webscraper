#include<iostream>
#include<string>

using namespace std;

int solution(string& s, int k)
{
	int res = 0;
	int n = s.size();
	int i;
	for(i = 0; i <= n - k; i++)
	{
		if(s[i] == '-')
		{
			for(int j = 0; j < k; j++)
				s[i+j] = s[i+j] == '+' ? '-' : '+';
			res++;
		}
	}
	while(i < n && s[i] == '+')
		i++;
	return i == n ? res : -1;
	
}

int main()
{
	int t, k, res;
	string s;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cin >> s >> k;
		res = solution(s, k);
		cout << "Case #" << i << ": ";
		if(res >= 0)
			cout << res << endl;
		else
			cout <<  "IMPOSSIBLE" << endl;
	}
	return 0;
}
