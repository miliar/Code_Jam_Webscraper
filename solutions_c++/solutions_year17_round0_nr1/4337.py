#include <algorithm>
#include <iterator>
#include <iostream>
#include <utility>
#include <string>
#include <vector>

using namespace std;

void flip(string& s, int from, int k)
{
    for(int i = from; i < from + k; i++)
        if(s[i] == '+')
            s[i] = '-';
        else
            s[i] = '+';
}


int main()
{
    int t;
    cin >> t;

    for(int test = 1; test <= t; test++) {
        string s;
        int k;
        cin >> s >> k;
        int n = s.size();
        int out = 0;
        for(int i = 0; i < n; i++) {
            if(s[i] == '-') {
                if(i + k <= n) {
                    flip(s, i, k);
                    out++;
                } else {
                    break;
                }
            }
        }
        cout << "Case #" << test << ": ";
        if(count(s.begin(), s.end(), '-'))
            cout << "IMPOSSIBLE" << endl;
        else
            cout << out << endl;
    }
    
    return 0;
}
