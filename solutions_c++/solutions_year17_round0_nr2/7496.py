#include<iostream>
#include<string>
using namespace std;




bool solve(int k)
{
	int prev = 10;
	while (k)
	{
		int nextK = k / 10;
		int cur = k - nextK * 10;
		if (prev < cur)return false;
		else prev = cur;
		k = nextK;
	}
	return true;
}

int main()
{
	int T;
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	ios::sync_with_stdio(false);
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		int N;
		cin >> N;
		int ret = 0;
		for (int i = 0; i <= N; i++)if(solve(i))ret = i;
		cout << "Case #" << tc << ": " << ret << endl;;
		
	}
	fclose(stdin);
	fclose(stdout);

	return 0;
}