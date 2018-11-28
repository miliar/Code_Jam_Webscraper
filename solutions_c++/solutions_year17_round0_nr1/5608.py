#include <iostream>
using namespace std;

bool is_happy(string s)
{
    for (char& c : s)
    {
        if (c == '-') return false;
    }
    return true;
}

void flip(string &s, size_t pos, size_t k)
{
    for (auto p = pos; p < pos + k; ++p)
    {
        auto c = s[p];
        if (c == '+') s[p] = '-';
        else          s[p] = '+';
    }
}

string compute(int k, string s)
{
    // k: number of pancakes that can be flipped at a time
    // s: pancake line
    int nb = 0;
    auto pos = s.find_first_of('-');
    
    if (pos == string::npos)
    {
        return to_string(nb);
    } 
    while (pos <= s.size() - k)
    {
        flip(s, pos, k);
        nb++;
        pos = s.find_first_of('-', pos + 1);
    }
    
    if (is_happy(s)) return to_string(nb);
    return "IMPOSSIBLE";
}

int main() {
    int t;
    cin >> t;  // read T
    for (int i = 1; i <= t; ++i) {
        int k;
        string s;
        cin >> s;  // read S
        cin >> k; // read K
        cout << "Case #" << i << ": " << compute(k, s) << endl;
    }
}
