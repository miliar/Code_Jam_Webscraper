#include <bits/stdc++.h>

using namespace std;

template<typename T>
ostream& operator<<(ostream& o, const vector<T>& v)
{
    o << "[";
    for(size_t i = 0; i < v.size(); i++)
    {
        o << v[i];
        if(i != v.size() - 1)
            o << ", ";
    }
    o << "]";
    return o;
}

int main()
{
    size_t num_cases;
    cin >> num_cases;
    for(size_t caso = 1; caso <= num_cases; caso++)
    {
        int rows, cols;
        cin >> rows >> cols;
        vector<vector<char>> grid;
        for(int i = 0; i < rows; i++)
        {
            string tmp;
            cin >> tmp;
            grid.push_back(vector<char>(tmp.begin(), tmp.end()));
        }
        function<vector<char>(int, vector<char>)> calc = [&grid, &calc](int row, vector<char> pattern) -> vector<char>
        {
            if(row == grid.size())
                return vector<char>();
            if(count(grid[row].begin(), grid[row].end(), '?') == grid[row].size())
            {
                if(pattern.size())
                {
                    grid[row] = pattern;
                    calc(row + 1, pattern);
                    return pattern;
                }
                else
                {
                    auto tmp = calc(row + 1, pattern);
                    assert(tmp.size());
                    grid[row] = tmp;
                    return tmp;
                }
            }
            else
            {
                for(int i = 0; i < grid[row].size(); i++)
                {
                    if(grid[row][i] != '?')
                    {
                        int j = i - 1;
                        while(j >= 0 && grid[row][j] == '?')
                        {
                            grid[row][j] = grid[row][i];
                            j--;
                        }
                        j = i + 1;
                        while(j < grid[row].size() && grid[row][j] == '?')
                        {
                            grid[row][j] = grid[row][i];
                            j++;
                        }
                    }
                }
                calc(row + 1, grid[row]);
                return grid[row];
            }
        };
        calc(0, vector<char>());
        cout << "Case #" << caso << ":" << endl;
        for(size_t i = 0; i < grid.size(); i++)
        {
            for(size_t j = 0; j < grid[i].size(); j++)
            {
                cout << grid[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}
