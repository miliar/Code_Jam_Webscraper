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
    long long total, n;
    vector<double> start, speed;

	void input()
    {
        cin >> total >> n;
        for (int i = 0; i < n; i++)
        {
            long long a, b;
            cin >> a >> b;
            start.push_back(a);
            speed.push_back(b);
        }
    }
    double answer = numeric_limits<double>::max();
	void process()
    {
        for (int i = 0; i < n; i++)
        {
            if (speed[i] > answer)
            {
                continue;
            }
            double k = ((start[i] - 0) * speed[i]) / (total - start[i]) + speed[i];
            answer = min(answer, k);
        }
    }
	void output()
    {
        printf("%.6lf", answer);
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
