#include<iostream>
#include<cstring>

using namespace std;

bool T[2005];
int n;

pair<int, int> f(int p)
{
	int l, r;
	for (int i = p; i >= 0; i--)
		if (T[i])
		{
			l = p-i-1;
			break;
		}
	for (int i = p; i <= n+1; i++)
		if (T[i])
		{
			r = i-p-1;
			break;
		}
	return make_pair(l, r);
}

int main()
{
	//ios_base::sync_with_stdio(0);
	int tt;
	cin >> tt;
	for (int t = 1; t <= tt; t++)
	{
		int k;
		cin >> n >> k;
		memset(T, 0, sizeof(T));
		T[0] = T[n+1] = true;
		pair<int, int> M;
		for (int i = 0; i < k; i++)
		{
			M = make_pair(-1, -1);
			int m_pos = 1000000;
			for (int j = 1; j <= n; j++)
			{
				if (T[j]) continue;
				pair<int, int> P = f(j);
				int pos = j;
				if (min(P.first, P.second) > min(M.first, M.second))
					M = P, m_pos = pos;
				else if (min(P.first, P.second) == min(M.first, M.second) and max(P.first, P.second) > max(M.first, M.second))
					M = P, m_pos = pos;
				else if (min(P.first, P.second) == min(M.first, M.second) and max(P.first, P.second) == max(M.first, M.second) and pos < m_pos)
					M = P, m_pos = pos;
			}
			T[m_pos] = true;
		}
		cout << "Case #" << t << ": " << max(M.first, M.second) << " " << min(M.first, M.second) << "\n";
	}
	return 0;
}
