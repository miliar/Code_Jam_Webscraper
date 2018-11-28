#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

void Flip(char& p)
{
    p = (p == '+') ? '-': '+';
}

void Flip(string& s, int pos, size_t flip_size)
{
    for(int i = pos; i < pos + flip_size;++i)
        Flip(s[i]);
}

int GetNumFlips(string s, size_t flip_size)
{
    int num_flips = 0;
    auto it = find_if(s.begin(), s.end(), [](char ch){return ch == '-';});
    while(it != s.end())
    {
        if(distance(it, s.end()) < flip_size)
            return numeric_limits<int>::max();
        ++num_flips;
        Flip(s, it - s.begin(), flip_size);
        it = find_if(s.begin(), s.end(), [](char ch){return ch == '-';});
    }
    return num_flips;
}

int main()
{
    ifstream ifile("input.in");
    ofstream ofile("output");
    int t;
    ifile >> t;
    for(int i = 1; i <= t; ++i)
    {
        string s;
        size_t flip_size;
        ifile >> s >> flip_size;
        const auto num_flips = GetNumFlips(s,flip_size);
        string res = num_flips == numeric_limits<int>::max() ? "IMPOSSIBLE": to_string(num_flips);
        ofile << "Case #" << i << ": " << res << endl;    
    }
	return 0;
}
