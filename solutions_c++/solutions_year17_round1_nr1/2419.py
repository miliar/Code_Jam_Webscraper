#include <iostream>
#include <string>
#include <vector>

using namespace std;

class  Solution
{
public:
    void AlphabetCake(vector<string>& cake)
    {
        int m = cake.size(), n = cake[0].size();
        vector<vector<int>> kids(m+1, vector<int>(n+1, 0));
        for (int i = 0; i < m; i++)
        {
            int sum = 0;
            for (int j = 0; j < n; j++)
            {
                sum += (cake[i][j] == '?') ? 0 : 1;
                kids[i + 1][j + 1] = sum + kids[i][j + 1];
            }
        }
        calc(cake, 0, m - 1, 0, n - 1, kids);
    }

private:
    void calc(vector<string>& cake, int upper, int lower, int left, int right, vector<vector<int>>& kids)
    {
        if (upper > lower || left > right) return;
        int kidsCount = kids[lower + 1][right + 1] + kids[upper][left] - kids[lower + 1][left] - kids[upper][right + 1];
        if (kidsCount == (lower - upper + 1) * (right - left + 1)) return;
        if (kidsCount == 1)
        {
            char kid;
            for (int i = upper; i <= lower; i++)
            {
                for (int j = left; j <= right; j++)
                {
                    if (cake[i][j] != '?')
                    {
                        kid = cake[i][j];
                        break;
                    }
                }
            }
            for (int i = upper; i <= lower; i++)
            {
                for (int j = left; j <= right; j++)
                {
                    cake[i][j] = kid;
                }
            }
            return;
        }
        int kc = 0;
        for (int i = upper; i < lower && kc < kidsCount; i++)
        {
            kc = kids[i + 1][right + 1] + kids[upper][left] - kids[i + 1][left] - kids[upper][right + 1];
            if (kc >= 1 && kc < kidsCount)
            {
                calc(cake, upper, i, left, right, kids);
                calc(cake, i + 1, lower, left, right, kids);
                return;
            }
        }
        kc = 0;
        for (int i = left; i < right && kc < kidsCount; i++)
        {
            kc = kids[lower + 1][i + 1] + kids[upper][left] - kids[lower + 1][left] - kids[upper][i + 1];
            if (kc >= 1 && kc < kidsCount)
            {
                calc(cake, upper, lower, left, i, kids);
                calc(cake, upper, lower, i+1, right, kids);
                return;
            }
        }
    }
};

void main() {
    int t;
    cin >> t;
    Solution sol;
    for (int i = 1; i <= t; ++i) {
        int r, c;
        cin >> r >> c;
        vector<string> cake;
        for (int j = 0; j < r; j++)
        {
            string line;
            cin >> line;
            cake.push_back(line);
        }
        sol.AlphabetCake(cake);
        cout << "Case #" << i <<":"<<endl;
        for (auto line: cake)
        {
            cout << line << endl;
        }
    }
}