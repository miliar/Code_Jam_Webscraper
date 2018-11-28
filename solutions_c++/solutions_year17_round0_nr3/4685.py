#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) (n); i++)

int main() {
    int T;
    cin >> T;
    forn(t, T) {
        int k, n;
        cin >> n >> k;
        multiset<int, greater<int>> s;
        s.insert(n);
        int m1, m2;
        forn(i, k) {
            int c = *s.begin();
            s.erase(s.begin());
            if(c == 0) continue;
            c --;
            //forn(j, s.size()) cerr << s[j] << " "; cerr << endl;
            // cerr << i << " " << c + 1 << " " << c / 2 + c % 2 << " " << c / 2 << endl;
            m1 = c / 2 + c % 2;
            m2 = c / 2;
            s.insert(m1);
            s.insert(m2);
        }
        cout << "Case #" << t + 1 << ": " << m1 << " " << m2 << endl;
    }
}
