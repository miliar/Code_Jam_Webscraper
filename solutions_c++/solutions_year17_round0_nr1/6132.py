#include <vector>
#include <iostream>

using namespace std;



int solve(vector<bool> t, int i, int n, int K)
{
	if(n - i < K)
	{
		bool ok = true;
		for(int j = i; ok && j < n; j++)
			ok = t[j];
		if(ok)
			return 0;
		else
			return -1;
	}
	else
	{
		if(t[i])
			return solve(t, i+1, n, K);
		else
		{
			for(int j = i; j < i+K; j++)
				t[j] = !t[j];
			int m = solve(t, i+1, n, K);
			if(m == -1)
				return -1;
			else
				return m+1;
		}
	}

}



int main()
{	
	int T;
	cin >> T;
	
	for(int i = 1; i <= T; i++)
	{
		cout << "Case #" << i << ": ";
		string s;
		int K;
		cin >> s >> K;
		
		int n = s.size();
		vector<bool> t(n, false);
		for(int j = 0; j < n; j++)
			t[j] = (s[j] == '+');
		
		int m = solve(t, 0, n, K);
		if(m == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << m << endl;
		
	}
}
