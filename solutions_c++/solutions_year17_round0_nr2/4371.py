#include <stdio.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>

using namespace std;

string s;
int n;
int main()
{
    freopen("/Users/aleksandra/Documents/problems/-/B-large.in", "r", stdin);
    freopen("/Users/aleksandra/Documents/problems/-/B-large.out", "w", stdout);
    cin >> n;

    for (int k = 0; k < n; ++k)
    {
        cin >> s;
        for (int i = s.size() - 1; i > 0; --i) {
            if (s[i] < s[i - 1]) {
                while (s[i - 1] == '0') i--;
                if (s[i - 1] != '0') s[i - 1]--;
                for (int j = i; j < s.size(); ++j) {
                    s[j] = '9';
                }
            }
        }
        stringstream ss;
        ss << s;
        long long int res;
        ss >> res;
        cout << "Case #" << k + 1 << ": " << res << endl;
    }

}
