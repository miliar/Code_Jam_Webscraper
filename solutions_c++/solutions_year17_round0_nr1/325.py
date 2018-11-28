//#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <numeric>
#define min(x, y) (y ^ ((x ^ y) & -(x < y)))
#define max(x, y) (x ^ ((x ^ y) & -(x < y)))
using namespace std;
typedef long long LL;
typedef double D;

vector<int> res;
bool arr[1001];

void flip(int l, int r)
{
	for (int i = l; i < r; ++i)
		arr[i] ^= 1;
}

int main()
{
	int T, k, cnt;
	string s;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		cnt = 0;
		cin >> s;
		for (int i = 0; i < s.length(); ++i)
			arr[i] = s[i] == '+';
		cin >> k;
		for (int i = 0; i + k <= s.length(); ++i)
			if (!arr[i])
			{
				flip(i, i + k);
				cnt++;
			}
		bool b = 1;
		for (int i = 0; i < s.length(); ++i)
			if (!arr[i])
			{
				res.push_back(-1);
				b = 0;
				break;
			}
		if (b)
			res.push_back(cnt);
	}
	
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		if (res[t - 1] != -1)
			cout << res[t - 1] << '\n';
		else
			cout << "IMPOSSIBLE" << '\n';
	}
}

//const int n = 40;
//int G[n][4];
//bool used[n];
//int mass[n];
//int color[n];
//
//int dfs(int v, int clr)
//{
//	int res = 1;
//	color[v] = clr;
//	used[v] = 1;
//	for (int i = 0; i < 4; ++i)
//	{
//		if (G[v][i] == -1)
//			continue;
//		int to = G[v][i];
//		if (!used[to])
//			res += dfs(to, clr);
//	}
//	return res;
//}
//
//int N, M;
//int num(int i, int j)
//{
//	return i * M + j;
//}
//
//bool arr[2001][2001];
//int last[2001];
//int main()
//{
//	memset(G, -1, sizeof(G));
//	memset(last, -1, sizeof(last));
//	char c;
//	cin >> N >> M;
//	for (int i = 0; i < N; ++i)
//		for (int j = 1; j <= M; ++j)
//		{
//			cin >> c;
//			arr[i][j] = c == '+';
//		}
//	
//	int lst = -1;
//	for (int j = 1; j <= M; ++j)
//	{
//		if (lst != -1)
//			G[num(0, j)][1] = num(0, lst);
//		if (arr[0][j])
//		{
//			G[num(0, lst)][0] = num(0, j);
//			last[j] = 0;
//			lst = j;
//		}
//	}
//	
//	for (int i = 1; i < N; ++i)
//	{
//		lst = -1;
//		for (int j = 1; j <= M; ++j)
//		{
//			if (last[j] != -1)
//				G[num(i, j)][3] = num(last[j], j);
//			if (lst != -1)
//				G[num(i, j)][1] = num(i, lst);
//			
//			if (arr[i][j])
//			{
//				G[num(last[j], j)][2] = num(i, j);
//				G[num(i, lst)][0] = num(i, j);
//				last[j] = i;
//				lst = j;
//			}
//		}
//	}
//	
//	lst = -1;
//	for (int j = M; j >= 1; --j)
//	{
//		if (lst != -1)
//			G[num(N - 1, j)][1] = num(N - 1, lst);
//		if (arr[N - 1][j])
//		{
//			G[num(N - 1, lst)][0] = num(N - 1, j);
//			last[j] = 0;
//			lst = j;
//		}
//	}
//	
//	for (int i = N - 2; i >= 0; --i)
//	{
//		lst = -1;
//		for (int j = M; j >= 1; --j)
//		{
//			if (last[j] != -1)
//				G[num(i, j)][3] = num(last[j], j);
//			if (lst != -1)
//				G[num(i, j)][1] = num(i, lst);
//			
//			if (arr[i][j])
//			{
//				G[num(last[j], j)][2] = num(i, j);
//				G[num(i, lst)][0] = num(i, j);
//				last[j] = i;
//				lst = j;
//			}
//		}
//	}
//	
//	int mx = 0, R = 0, C = 0, clr = 1;
//	
//	for (int i = 0; i < N; ++i)
//		for (int j = 1; j <= M; ++j)
//		{
//			if (arr[i][j])
//				continue;
//			int val = 0;
//			vector<int> temp;
//			
//			for (int k = 0; k < 4; ++k)
//			{
//				if (G[num(i, j)][k] == -1)
//					continue;
//				
//				bool b = 1;
//				for (int l = 0; l < temp.size(); ++l)
//					if (color[G[num(i, j)][k]] == temp[l])
//					{
//						b = 0;
//						break;
//					}
//				if (b)
//				{
//					if (mass[color[G[num(i, j)][k]]])
//						val += mass[color[G[num(i, j)][k]]];
//					else
//					{
//						mass[clr] = dfs(G[num(i, j)][k], clr);
//						val += mass[clr];
//						clr++;
//					}
//					temp.push_back(color[G[num(i, j)][k]]);
//				}
//			}
//			
//			if (val > mx)
//			{
//				mx = val;
//				R = i + 1;
//				C = j;
//			}
//		}
//	cout << mx << '\n';
//	if (mx)
//		cout << R << ' ' << C;
//}


////#include <stdio.h>
//#include <memory.h>
//#include <algorithm>
//#include <iostream>
//#include <string>
//#include <vector>
//#define min(x, y) (y ^ ((x ^ y) & -(x < y)))
//#define max(x, y) (x ^ ((x ^ y) & -(x < y)))
//using namespace std;
//typedef long long LL;
//typedef double D;
//
//LL dp[60] = {0, 3};
//LL sum[60] = {0, 3};
//
//char f(char last, LL n)
//{
//	switch (last)
//	{
//		case 'a':
//		{
//			return 'b' + n;
//		}
//		case 'c':
//		{
//			return 'a' + n;
//		}
//	}
//	if (!n)
//		return 'a';
//	else
//		return 'c';
//}
//int main()
//{
//	LL n, k;
//	cin >> n >> k;
//	for (int i = 2; i <= 57; ++i)
//	{
//		dp[i] = dp[i - 1] << 1;
//		sum[i] = sum[i - 1] + dp[i];
//	}
//	if (n > 57)
//		n = 57;
//	if (k > sum[n])
//	{
//		cout << "NO";
//		return 0;
//	}
//	char last = (char)((k - 1) / (sum[n] / 3LL) + 'a');
//	cout << last;
//	k = (k - 1) % (sum[n] / 3LL) + 1;
//	n--;
//	while(n)
//	{
//		if (k == 1LL)
//			return 0;
//		else
//			k--;
//		last = f(last, (k - 1) / (sum[n] / 3LL));
//		k = (k - 1) % (sum[n] / 3LL) + 1;
//		cout << last;
//		n--;
//	}
//}
//
//
//
//
//
//
//
//
//
