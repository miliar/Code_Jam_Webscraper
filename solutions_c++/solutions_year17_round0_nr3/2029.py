#include <iostream>
#include <fstream>
#include <limits>
#include <map>

using namespace std;

typedef unsigned long long ulong;

typedef map< pair<ulong, ulong>, pair<ulong, ulong> > MemType;

pair <ulong, ulong> solve(const pair<ulong, ulong>& key, MemType& mem) {
    if (mem.find(key) != mem.end()) {
        return mem[key];
    }
    if (key.second == 0) {
        return make_pair<ulong, ulong>(std::numeric_limits<ulong>::max(), std::numeric_limits<ulong>::max());
    }

    if (key.second == 1) {
        pair<ulong, ulong> p;
        p.first  = (key.first - 1)/2;
        p.second =  key.first/2;
        mem[key] =  p;
        return p;
    }

    pair <ulong, ulong> n_key;
    n_key.first  = (key.first - 1)/2;
    n_key.second = (key.second - 1)/2;

    pair <ulong, ulong> left  = solve(n_key, mem);
    n_key.first  = key.first/2;
    n_key.second = key.second/2;
    pair <ulong, ulong> right = solve(n_key, mem);

    pair <ulong, ulong> res;
    res.first  = min(left.first, right.first);
    res.second = min(left.second, right.second);

    mem[key] = res;

    return res;
}

int main()
{
    ifstream fin("data/C-large.in");
    ofstream fout("data/C-large.out");

    int test_cnt = 0;
    fin >> test_cnt;

    for (int test_case = 1; test_case <= test_cnt; ++test_case) {
        ulong n, k;
        fin >> n >> k;

        MemType mem;
        pair <ulong, ulong> key;
        key.first = n; key.second = k;
        pair <ulong, ulong> res = solve(key, mem);

        fout << "Case #" << test_case << ": " << res.second << " " << res.first << endl;
    }

    fin.close();
    fout.close();

    return 0;
}
