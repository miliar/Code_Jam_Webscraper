#include <string>
#include <iostream>
#include <deque>
#include <cassert>

using namespace std;

char flip(char c) {
    if (c == '-') return '+';
    else if (c == '+') return '-';
    else return c;
}

int main() {
    int T;
    cin >> T;
    for (int cs=1; cs<=T; ++cs) {
        string S;
        int K;
        cin >> S >> K;
        deque<int> idxs;
        int f=0;
        const int z=S.length();
        char c='+';
        for (int i=0; i<z; ++i) {
            if (idxs.size() && idxs.front() == i) {
                c = flip(c);
                idxs.pop_front();
            }
            if (S[i] == c) continue;
            if (z-i<K) goto impossible;
            c = flip(c);
            ++f;
            idxs.push_back(i+K);
        }
        cout << "Case #" << cs << ": " << f << "\n";
        continue;

      impossible:
        cout << "Case #" << cs << ": IMPOSSIBLE\n";
    }
}
