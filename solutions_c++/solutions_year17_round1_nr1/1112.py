#include <iostream>
#include <vector>
#include <cassert>

void first_problem()
{
    int num_instances;
    std::cin >> num_instances;
    for (int i = 0; i < num_instances; ++i) {
        int rows, columns;
        std::cin >> rows >> columns;
        std::vector< std::vector<int> > cake;
        for (int j = 0; j < rows; ++j) {
            std::vector<int> row;
            std::string s;
            std::cin >> s;
            for (int k = 0; k < columns; ++k) {
                row.push_back(s[k]);
            }
            cake.push_back(row);
        }

        //find first row with char

        int cur_row = -1;

        bool found = false;
        for (int m = 0; m < cake.size(); ++m) {
            for (int j = 0; j < cake[m].size(); ++j) {
                if(cake[m][j] != '?')
                {
                    cur_row = m;
                    found = true;
                    break;
                }
            }
            if(found)
            {
                break;
            }
        }

        assert(cur_row != rows);

        int first_row = cur_row;

        while(cur_row < rows)
        {
            auto & row = cake[cur_row];
            int first_idx = -1;
            for (int j = 0; j < row.size(); ++j) {
                if(row[j] != '?')
                {
                    first_idx = j;
                    break;
                }
            }

            if(first_idx != -1)
            {
                int sign = row[first_idx];
                for (int j = 0; j < row.size(); ++j) {
                    if(row[j] != '?')
                    {
                        sign = row[j];
                    }
                    row[j] = sign;
                }
            }
            else
            {
                auto & prev_row = cake[cur_row - 1];
                for (int j = 0; j < row.size(); ++j) {
                    row[j] = prev_row[j];
                }
            }
            cur_row ++;
        }

        for (int l = 0; l < first_row; ++l) {
            for (int j = 0; j < columns; ++j) {
                cake[l][j] = cake[first_row][j];
            }
        }

        std::cout << "Case #" << i + 1 << ": " << "\n";

        for (int n = 0; n < rows; ++n) {
            for (int j = 0; j < columns; ++j) {
                std::cout << (char)cake[n][j];
            }
            std::cout << "\n";
        }

    }
}

int main() {
    first_problem();
    return 0;
}