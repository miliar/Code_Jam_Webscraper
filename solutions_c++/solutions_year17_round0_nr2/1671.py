#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t;
    in >> t;
    for (int i = 0; i < t; ++i) {
        string s;
        in >> s;
        reverse(s.begin(), s.end());
        for (int i = 0; i < 20; ++i) {
            int j = 1;
            while (j < s.size() && s[j - 1] >= s[j]) {
                ++j;
            }
            if (j < s.size()) {
                for (int k = 0; k < j; ++k)
                    s[k] = '9';
                --s[j];
                while (s[j] < 0) {
                    s[j] = '9';
                    ++j;
                }
            }
            while (s.back() == '0') {
                s.pop_back();
            }
        }
        reverse(s.begin(), s.end());
        out << "Case #" << i + 1 << ": " << s << '\n';
    }
}
