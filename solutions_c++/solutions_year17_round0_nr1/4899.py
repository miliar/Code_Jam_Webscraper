#include <iostream>
#include <string>
#include <vector>

using namespace std;

void find_flips(const string& s, int k);

int main() {
    int t, k;
    string s;
    cin >> t;
    for (int x = 1; x <= t; ++x) {
        cin >> s >> k;
        cout << "Case #" << x << ": ";
        find_flips(s, k);
        cout << endl;
    }
    return 0;
}

void find_flips(const string& s, int k) {
    vector<bool> happy_up;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == '+')
            happy_up.push_back(true);
        else if (s[i] == '-')
            happy_up.push_back(false);
    }
        
    int i, count = 0;
    for (i = 0; i <= happy_up.size()-k; ++i) {
        if (!happy_up[i]) {
            ++count;
            for (int j = 0; j < k; ++j)
                happy_up[i+j] = !happy_up[i+j];
        }
    }
    
    for (; i < happy_up.size(); ++i) {
        if (!happy_up[i]) {
            cout << "IMPOSSIBLE";
            return;
        }
    }
        
    cout << count;    
}
