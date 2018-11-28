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

typedef long double ld;
typedef pair<long double, long double> pldld;

int main()
{
    size_t num_cases;
    cin >> num_cases;
    for(size_t caso = 1; caso <= num_cases; caso++)
    {
        long double ingredients, packages;
        cin >> ingredients >> packages;
        vector<long double> portion;
        vector<vector<long double>> grid;
        for(size_t i = 0; i < ingredients; i++)
        {
            long double tmp;
            cin >> tmp;
            portion.push_back(tmp);
        }
        for(size_t i = 0; i < ingredients; i++)
        {
            vector<long double> tmp;
            for(size_t j = 0; j < packages; j++)
            {
                long double tmp2;
                cin >> tmp2;
                tmp.push_back(tmp2 / portion[i]);
            }
            sort(tmp.begin(), tmp.end());
            grid.push_back(tmp);
        }
        auto get_range = [](const long double value) -> pldld
        {
            return make_pair(ceil(value * (10.0 / 11.0)), floor(value * (10.0 / 9.0)));
        };
        auto merge_ranges = [](pldld r1, pldld r2) -> pldld
        {
            return make_pair(max(r1.first, r2.first), min(r1.second, r2.second));
        };
        vector<size_t> indexes((size_t)ingredients);
        size_t cnt = 0;
        while(!count(indexes.begin(), indexes.end(), size_t(packages)))
        {
            ld minval = grid[0][indexes[0]];
            size_t minindex = 0;
            auto rng = get_range(grid[0][indexes[0]]);
            bool ok = rng.first <= rng.second;
            for(size_t i = 1; i < size_t(ingredients); i++)
            {
                rng = merge_ranges(rng, get_range(grid[i][indexes[i]]));
                if(grid[i][indexes[i]] < minval)
                {
                    minval = grid[i][indexes[i]];
                    minindex = i;
                }
                if(rng.first > rng.second)
                    ok = false;
            }
            if(ok)
            {
                cnt++;
                for(size_t i = 0; i < indexes.size(); i++)
                {
                    indexes[i]++;
                }
            }
            else
            {
                indexes[minindex]++;
            }
        }
        cout << "Case #" << caso << ": " << cnt << endl;
    }
    return 0;
}
