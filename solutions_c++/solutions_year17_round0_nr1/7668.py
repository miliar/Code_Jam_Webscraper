#include <iostream>
#include <string>
#include <vector>
using namespace std;
void flip(vector<bool>& s, int pos, int k)
{
    for (int i = 0; i < k; ++i) {
        s[i + pos] = !s[i + pos];
    }
}
int numFlips(vector<bool>& s, int k, int first = 0, int last = -1)
{
    if (last == -1)
        last = s.size();
    while (first <= last && s[first] == 1)
        ++first;
    if (first == last)
        return 0;
    while (last - 1 >= first && s[last - 1] == 1)
        --last;
    if (last - first < k) {
        bool possible = true;
        for (int i = first; i < last; ++i) {
            if (s[i] == 0) {
                possible = false;
                break;
            }
        }
        if (!possible)
            return -1;
        return 0;
    }
    flip(s, first, k);
    int next = numFlips(s, k, first, last);
    if (next == -1)
        return next;
    return next + 1;
}
int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        string s;
        cin >> s;
        vector<bool> S;
        for (auto& i : s) {
            if (i == '+') {
                S.push_back(1);
            } else {
                S.push_back(0);
            }
        }
        int k = 3;
        cin >> k;
        int r = numFlips(S, k);
        cout << "Case #" << i << ": ";
        if (r == -1) {
            cout << "IMPOSSIBLE";
        } else {
            cout << r;
        }
        cout << endl;
    }
}