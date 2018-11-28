#include<iostream>
#include<string>
#include<vector>

using namespace std;

#define _CRT_SECURE_NO_WARNINGS 1

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T = 3;

	scanf("%d", &T);
	for (int t = 0; t < T; ++t)
	{

		string s;
		cin >> s;
		int size = s.size( );
		vector< bool > v;
		for (int i = 0; i < size; ++i)
		{
			v.push_back(s[i] == '+');
		}
		int k, ans = 0;
		cin >> k;
		for (int i = 0; i < v.size(); ++i)
		{
			if (v.size() - i == k)
			{
				int p_cont = 0, m_count = 0;
				for (int j = i; j < v.size(); ++j)
				{
					if (v[j])
					{
						++p_cont;
					}
					else
					{
						++m_count;
					}
				}

				if (p_cont == 0)
				{
					++ans;
				}
				else if(m_count == 0)
				{

				}
				else
				{
					ans = -1;
				}

				break;
			}

			if (!v[i])
			{
				++ans;
				for (int j = i; j < i + k; ++j)
				{
					v[j] = !v[j];
				}
			}
		}

		if (ans < 0)
		{
			printf("Case #%d: IMPOSSIBLE\n", t + 1);
		}
		else
		{
			printf("Case #%d: %d\n", t + 1, ans);
		}

	}

	return 0;
}