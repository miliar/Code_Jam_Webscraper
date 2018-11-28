#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool is_tidy(size_t n)
{
    size_t biggest = 0;
    auto s = to_string(n);
    for (char& c : s)
    {
        if (c < biggest) return false;
        if (c > biggest) biggest = c;
    }
    return true;
}


size_t get_first_highest_pos(string s)
{
    static vector<char> numbers {'9', '8', '7', '6', '5', '4', '3', '2', '1'};
    for (auto& num : numbers)
    {
        auto pos = s.find_first_of(num);
        if (pos != string::npos) return pos;
    }
    return string::npos;
}

size_t compute(size_t n)
{
    while (!is_tidy(n))
    {
        auto s = to_string(n);
        auto pos = get_first_highest_pos(s);
        s[pos]--;
        for (auto p = pos + 1; p < s.size(); ++p)
        {
            s[p] = '9';
        }
        n = stoull(s);;
    }
    return n;
}

int main() {
    int t;
    cin >> t;  // read T
    for (int i = 1; i <= t; ++i) {
        size_t n;
        cin >> n; // read N
        cout << "Case #" << i << ": " << compute(n) << endl;
    }
}
