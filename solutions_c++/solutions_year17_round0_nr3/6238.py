#include<iostream>
#include<vector>
#include<map>
#include<queue>
using namespace std;




int solve(int room, int n)
{
	int sum = 0;
	map<int, int> m;
	queue<int> q;
	q.push(room);
	m[room] = 1;
	int c = -1;
	while (sum < n)
	{
		c = q.front(); q.pop();
		sum += m[c];
		int c1 = c / 2;
		int c2 = c - c1 - 1;
		m[c1] += m[c];
		m[c2] += m[c];
		if (q.empty() || q.back() != c1)q.push(c1);
		if (q.empty() || q.back() != c2)q.push(c2);
	}
	return c;
	
}

int main()
{
	int T;
	freopen("Text.txt", "r", stdin);
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("C-small-2-attempt0.out", "w", stdout);
	ios::sync_with_stdio(false);
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		int n;
		int k;
		cin >> n >> k;
		int ret = solve(n, k);

		int Ls = ret / 2;
		int Rs = ret - Ls - 1;
		int M = Rs > Ls ? Rs : Ls;
		int m = Rs <= Ls ? Rs : Ls;
		cout << "Case #" << tc << ": " <<M <<" "<<m<< endl;;

	}
	fclose(stdin);
	fclose(stdout);

	return 0;
}