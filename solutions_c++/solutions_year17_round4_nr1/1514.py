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
	int n, p;
	vector<int> g;
	int answer = 0;

	void input()
    {
		cin >> n >> p;
		g.resize(n);
		for (int i = 0; i < n; i++)
		{
			cin >> g[i];
		}
    }
    
    int table[128][128][128][4];
    bool went[128][128][128][4];

    int modclamp(int n, int p)
    {
        while (n < 0) n += p;
        while (n >= p) n -= p;
        return n;
    }

    int solve(vector<int> state, int mod)
    {
        int i = state[0], j = state[1], k = state[2];

        int &result = table[i][j][k][mod];
        if (went[i][j][k][mod])
        {
            return result;
        }
        went[i][j][k][mod] = true;

        result = -1;

        if (state[0])
        {
            state[0]--;
            int mc = modclamp(mod + 1, p);
            int r = solve(state, mc);
            if (r != -1)
                result = max(result, r + !!(mc == 0));
            state[0]++;
        }
        if (state[1])
        {
            state[1]--;
            int mc = modclamp(mod + 2, p);
            int r = solve(state, mc);
            if (r != -1)
                result = max(result, r + !!(mc == 0));
            state[1]++;
        }
        if (state[2])
        {
            state[2]--;
            int mc = modclamp(mod + 3, p);
            int r = solve(state, mc);
            if (r != -1)
                result = max(result, r + !!(mc == 0));
            state[2]++;
        }
        return result;
    }

    void process()
    {
        for (int i = 0; i < 128; i++)
        {
            for (int j = 0; j < 128; j++)
            {
                for (int k = 0; k < 128; k++)
                {
                    for (int m = 0; m < 4; m++)
                    {
                        went[i][j][k][m] = false;
                    }
                }
            }
        }
        for (int m = 0; m < 4; m++)
        {
            went[0][0][0][m] = true;
            table[0][0][0][m] = -1;
        }
        table[0][0][0][0] = 0;

        vector<int> target(3);
        for (int i = 0; i < n; i++)
        {
            int mod = g[i] % p;
            if (mod != 0)
            {
                target[mod - 1]++;
            }
            answer += mod == 0;
        }
        answer += max(
            max(solve(target, 0), solve(target, 1)),
            max(solve(target, 2), solve(target, 3))
            );
    }
	void output()
    {
		cout << answer;
    }
};

int main()
{
	int t;
	cin >> t;

    bool serial = true;
    if (serial)
    {
        for (int i = 0; i < t; i++)
        {
            vector<TestCase> tc(1);
            tc[0].input();
            tc[0].process();
            cout << "Case #" << i + 1 << ": ";
            tc[0].output();
            cout << endl;
        }
    }
    else
    {
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
    }
	return 0;
}
