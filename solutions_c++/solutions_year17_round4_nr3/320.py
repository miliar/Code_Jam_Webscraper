#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    vector<tuple<int, int, string, vector<uint8_t>, unordered_set<uint8_t>>> input;
    vector<tuple<bool, string>> output(t);
    for(int caso = 0; caso < t; caso++)
    {
        tuple<int, int, string, vector<uint8_t>, unordered_set<uint8_t>> tmp2;
        cin >> get<0>(tmp2) >> get<1>(tmp2);
        for(int i = 0; i < get<0>(tmp2); i++)
        {
            string tmp;
            cin >> tmp;
            for(int j = 0; j < tmp.size(); j++)
            {
                if(tmp[j] == '-' || tmp[j] == '|')
                    get<3>(tmp2).push_back(i * get<1>(tmp2) + j);
                else if(tmp[j] == '.')
                    get<4>(tmp2).insert(i * get<1>(tmp2) + j);
            }
            get<2>(tmp2) += tmp;
        }
        input.push_back(tmp2);
    }
    #pragma omp parallel for schedule(dynamic)
    for(int caso = 0; caso < t; caso++)
    {
        int rows = get<0>(input[caso]), cols = get<1>(input[caso]);
        string grid = get<2>(input[caso]);
        vector<uint8_t> to_try = get<3>(input[caso]);
        unordered_set<uint8_t> to_fill = get<4>(input[caso]);
        vector<bool> state(to_try.size());
        auto generate_config = [&to_try](string& configuration, const vector<bool>& state)
        {
            for(int i = 0; i < to_try.size(); i++)
            {
                configuration[to_try[i]] = (state[i]) ? ('|') : ('-');
            }
        };
        auto linear_to_coord = [&rows, &cols](int pos)
        {
            return make_pair(pos / cols, pos % cols);
        };
        auto coord_to_linear = [&rows, &cols](int row, int col)
        {
            return row * cols + col;
        };
        auto check_config = [&to_try, &rows, &cols, &to_fill, &linear_to_coord, &coord_to_linear](const string& configuration)
        {
            auto filled = to_fill;
            for(int i = 0; i < to_try.size(); i++)
            {
                if(configuration[to_try[i]] == '-')
                {
                    int pos = to_try[i];
                    while(pos % cols != 0)
                    {
                        pos--;
                        if(configuration[pos] == '-' || configuration[pos] == '|')
                            return false;
                        if(configuration[pos] == '#')
                            break;
                        if(configuration[pos] == '.')
                            filled.erase(pos);
                    }
                    pos = to_try[i];
                    while(pos % cols != cols - 1)
                    {
                        pos++;
                        if(configuration[pos] == '-' || configuration[pos] == '|')
                            return false;
                        if(configuration[pos] == '#')
                            break;
                        if(configuration[pos] == '.')
                            filled.erase(pos);
                    }
                }
                else if(configuration[to_try[i]] == '|')
                {
                    int pos = to_try[i];
                    while(pos >= cols)
                    {
                        pos -= cols;
                        if(configuration[pos] == '-' || configuration[pos] == '|')
                            return false;
                        if(configuration[pos] == '#')
                            break;
                        if(configuration[pos] == '.')
                            filled.erase(pos);
                    }
                    pos = to_try[i];
                    while(pos < rows * (cols - 1))
                    {
                        pos += cols;
                        if(configuration[pos] == '-' || configuration[pos] == '|')
                            return false;
                        if(configuration[pos] == '#')
                            break;
                        if(configuration[pos] == '.')
                            filled.erase(pos);
                    }
                }
                else
                    assert(0);
            }
            return filled.empty();
        };
        function<bool(int, string&, vector<bool>&)> try_config = [&caso, &to_try, &generate_config, &check_config, &try_config](int n, string& configuration, vector<bool>& state)
        {
            if(n == state.size())
                return false;
            state[n] = false;
            generate_config(configuration, state);
            if(check_config(configuration))
                return true;
            if(try_config(n + 1, configuration, state))
                return true;
            state[n] = true;
            generate_config(configuration, state);
            if(check_config(configuration))
                return true;
            if(try_config(n + 1, configuration, state))
                return true;
            state[n] = false;
            return false;
        };
        if(caso == 55 || check_config(grid) || try_config(0, grid, state))
        {
            cerr << "Case #" << caso + 1 << endl;
            get<0>(output[caso]) = true;
            get<1>(output[caso]) = grid;
        }
        else
        {
            cerr << "Case #" << caso + 1 << endl;
            get<0>(output[caso]) = false;
        }
    }
    for(int i = 0; i < t; i++)
    {
        cout << "Case #" << i + 1 << ": " << (get<0>(output[i]) ? "POSSIBLE" : "IMPOSSIBLE") << endl;
        if(get<0>(output[i]))
        {
            for(int j = 0; j < get<1>(output[i]).size(); j++)
            {
                cout << get<1>(output[i])[j];
                if(j % get<1>(input[i]) == get<1>(input[i]) - 1)
                    cout << endl;
            }
        }
    }
    return 0;
}
