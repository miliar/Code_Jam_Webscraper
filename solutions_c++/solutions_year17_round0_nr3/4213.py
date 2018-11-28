#include <iostream>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

void print(int testNum, const string& answer) {
    cout << "Case #" << testNum << ": " << answer << "\n";
}


int main(void) {
    int t;
    cin >> t;

    for (int testNum = 1; testNum <= t; testNum++) {
        int n, k;
        cin >> n >> k;
        multiset <int> st;
        st.insert(n);
        int mn, mx;
        for (int i = 0; i < k; i++) {
            auto pp = st.rbegin();
            mn = ((*pp) - 1) / 2;
            mx = ((*pp)) / 2;
            st.erase(st.find(*pp));
            st.insert(mn);
            st.insert(mx);
        }
        print(testNum, to_string(mx) + " " + to_string(mn));
    }
    return 0;
}
