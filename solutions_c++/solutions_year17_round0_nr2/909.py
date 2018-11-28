#include <fstream>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define cin fin
#define cout fout
ifstream fin("a.in");
ofstream fout("a.out");

long long wei[100];

void calc_wei()
{
	wei[0] = 1;
	for(int i = 1; i <= 20; i++)
		wei[i] = wei[i - 1] * 10;
}

long long slv(long long x)
{
	long long ans = 1;
	for(int i = 0; i <= 18; i++)
	{
		long long res = wei[i] - 1;
		int k = x / wei[i] % 10 - 1;
		
		for(int j = i; j <= 18; j++)
		{
			if(x / wei[j] % 10 < k)
				k = x / wei[j] % 10;
			res += k * wei[j];
		}
		if(res > ans && res <= x) ans = res;
	}
	bool f = true;
	for(int i = 0; i <= 18; i++)
		if(x / wei[i] % 10 < x / wei[i + 1] % 10)
			f = false;
	if(f) ans = x;
	return ans;
}

int main()
{
	int T;
	cin >> T;
	calc_wei();
	for(int i = 1; i <= T; i++)
	{
		long long x;
		cin >> x;
		long long ans = slv(x);
		cout << "Case #" << i << ": " << ans << endl;
	}
	
	
	
	return 0;
}

