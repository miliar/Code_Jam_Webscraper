#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <future>
#include <functional>
#include <string>
#include <map>
#include <list>
#include <numeric>
#include <cstdio>
#include <cstring>

using namespace std;

struct TestCase
{
    int n, m;
    char cake[100][100];

	void input()
    {
        cin >> n >> m;
        for (int i = 0; i < n; i++)
        {
            scanf("%s", cake[i]);
        }
    }
    void paint(int x, int y, int p, int q, char color)
    {
        for (int i = x; i < p; i++)
        {
            for (int j = y; j < q; j++)
            {
                cake[i][j] = color;
            }
        }
    }
    char pure(int x, int y, int p, int q)
    {
        char result = 0;
        for (int i = x; i < p; i++)
        {
            for (int j = y; j < q; j++)
            {
                if (cake[i][j] != '?' &&
                    result && cake[i][j] != result)
                {
                    return 0;
                }
                if (!result && cake[i][j] != '?')
                {
                    result = cake[i][j];
                }
            }
        }
        return result;
    }
    int count(int x, int y, int p, int q)
    {
        bool cnt[256];
        fill(cnt, cnt + 256, 0);
        for (int i = x; i < p; i++)
        {
            for (int j = y; j < q; j++)
            {
                cnt[cake[i][j]] = true;
            }
        }
        int result = 0;
        for (int i = 'A'; i <= 'Z'; i++)
        {
            result += cnt[i];
        }
        return result;
    }
    void solve(int x, int y, int p, int q)
    {
        char color;
        if ((color = pure(x, y, p, q)))
        {
            paint(x, y, p, q, color);
            return;
        }
        // left
        for (int pivot = x + 1; pivot < p; pivot++)
        {
            if (count(x, y, pivot, q) && count(pivot, y, p, q))
            {
                solve(x, y, pivot, q);
                solve(pivot, y, p, q);
                return;
            }
        }
        // up
        for (int pivot = y + 1; pivot < q; pivot++)
        {
            if (count(x, y, p, pivot) && count(x, pivot, p, q))
            {
                solve(x, y, p, pivot);
                solve(x, pivot, p, q);
                return;
            }
        }
    }
	void process()
    {
        solve(0, 0, n, m);
    }
	void output()
    {
        for (int i = 0; i < n; i++)
        {
            printf("\n");
            for (int j = 0; j < m; j++)
            {
                printf("%c", cake[i][j]);
            }
        }
    }
};

int main()
{
	int t;
	cin >> t;

	vector<TestCase> tc(t);
	vector<future<void>> f;
	for (int i = 0; i < t; i++) tc[i].input();
	for (int i = 0; i < t; i++)
		f.push_back(async(launch::async,
			[&](int p){ tc[p].process(); }, i));
	for (int i = 0; i < t; i++) f[i].wait();
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		tc[i].output();
		cout << endl;
	}
	return 0;
}
