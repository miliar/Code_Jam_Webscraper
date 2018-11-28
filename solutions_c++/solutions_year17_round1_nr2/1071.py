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
    vector<int> recipe;
    vector<vector<pair<int, int>>> package;
	void input()
    {
        cin >> n >> p;
        for (int i = 0; i < n; i++)
        {
            int input;
            cin >> input;
            recipe.push_back(input);
        }
        package.resize(n);
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < p; j++)
            {
                int input;
                cin >> input;
                int left = INT_MAX;
                int right = INT_MIN;
                for (int h = 1;; h++)
                {
                    if (h * recipe[i] * 9 > 10 * input)
                    {
                        break;
                    }
                    if (h * recipe[i] * 9 <= 10 * input &&
                        h * recipe[i] * 11 >= 10 * input)
                    {
                        left = min(left, h);
                        right = max(right, h);
                    }
                }
                package[i].push_back({ left, right });
            }
        }
    }
    int answer = 0;
	void process()
    {
        if (n == 2)
        {
            vector<int> bottom(p);
            iota(bottom.begin(), bottom.end(), 0);
            do
            {
                int sum = 0;
                for (int i = 0; i < p; i++)
                {
                    auto a = package[0][i];
                    auto b = package[1][bottom[i]];

                    if (a.first == INT_MIN || a.first == INT_MAX ||
                        a.second == INT_MIN || a.second == INT_MAX ||
                        b.first == INT_MIN || b.first == INT_MAX ||
                        b.second == INT_MIN || b.second == INT_MAX)
                    {
                        continue;
                    }
                    if (a.second < b.first || a.first > b.second)
                    {
                        continue;
                    }
                    sum++;
                }
                answer = max(answer, sum);
            } while (next_permutation(bottom.begin(), bottom.end()));
        }
        else
        {
            int sum = 0;
            for (int i = 0; i < p; i++)
            {
                auto a = package[0][i];
                if (a.first == INT_MIN || a.first == INT_MAX ||
                    a.second == INT_MIN || a.second == INT_MAX)
                {
                    continue;
                }
                sum++;
            }
            answer = max(answer, sum);
        }
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
