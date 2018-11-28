#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void flip(string &s, string::size_type p, unsigned short k);

int main()
{
    unsigned short T = 0;
    cin >> T;
    for (unsigned short t = 1; t <= T; ++t)
    {
        string s;
        unsigned short k;
        cin >> s >> k;
        bool possible = true;
        vector<string::size_type> ps;
        string::size_type p = 0;
        while (possible && ( (p = s.find_first_of("-")) != string::npos) )
        {
            possible = (find(ps.cbegin(), ps.cend(), p) == ps.cend());
            if (possible)
            {
                ps.push_back(p);
                flip(s, p, k);
            }
        }
        cout << "Case #" << t << ": "
             << ((possible)? to_string(ps.size()) : "IMPOSSIBLE") << '\n';
    }
}

void flip(string &s, string::size_type p, unsigned short k)
{
    p = (p + k >= s.size())? s.size() - k : p;
    for (string::size_type i = p; i < p+k; ++i)
        s[i] = static_cast<char>(88 - static_cast<int>(s[i]));
}

