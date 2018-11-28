#include <vector>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <queue>

void updateTime(int sourceCity, int currentCity, int endurance, int speed, double usedTime, const std::vector<std::vector<int>>& d, std::vector<std::vector<double>>& t)
{
    for (int i = 0; i < d.size(); i++)
    {
        if (d[currentCity][i] != -1 && d[currentCity][i] <= endurance)
        {
            double tt = usedTime + d[currentCity][i] / (double)speed;
            if (tt < t[sourceCity][i])
                t[sourceCity][i] = tt;

            updateTime(sourceCity, i, endurance - d[currentCity][i], speed, tt, d, t);
        }
    }
}

int main()
{
    freopen("/Users/screamer/Dropbox/Code/bin/input.txt", "r", stdin);
    freopen("/Users/screamer/Dropbox/Code/bin/output.txt", "w", stdout);

    std::cout.setf(std::ios_base::fixed, std::ios_base::floatfield);
    std::cout.precision(6);

    int T;
    std::cin >> T;
    for (int tc = 1; tc <= T; tc++)
    {
        int n, q;
        std::cin >> n >> q;

        std::vector<int> endurance(n), speed(n);
        for (int i = 0; i < n; i++)
            std::cin >> endurance[i] >> speed[i];

        std::vector<std::vector<int>> d(n, std::vector<int>(n));
        for (int i = 0; i < n; i++)
            std::copy_n(std::istream_iterator<int>(std::cin), n, d[i].begin());

        std::vector<std::pair<int, int>> requests(q);
        for (int i = 0; i < q; i++)
            std::cin >> requests[i].first >> requests[i].second;

        std::vector<std::vector<double>> t(n, std::vector<double>(n));
        for (int city = 0; city < n; city++)
        {
            for (int target = 0; target < n; target++)
            {
                if (d[city][target] != -1 && d[city][target] <= endurance[city])
                {
                    t[city][target] = d[city][target] / (double)speed[city];
                }
                else
                {
                    t[city][target] = std::numeric_limits<double>::max();
                }
            }
        }

        for (int i = 0; i < n; i++)
            updateTime(i, i, endurance[i], speed[i], 0, d, t);

        for (int i = 0; i < n; i++)
            t[i][i] = 0;

        for (int k=0; k<n; ++k)
	        for (int i=0; i<n; ++i)
		        for (int j=0; j<n; ++j)
			        t[i][j] = std::min(t[i][j], t[i][k] + t[k][j]);

        std::cout << "Case #" << tc << ": ";
        for (int i = 0; i < q; i++)
            std::cout << t[requests[i].first - 1][requests[i].second - 1] << " ";
        std::cout << std::endl;
    }

    return 0;
}