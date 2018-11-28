#include <iostream>
#include <string>

using namespace std;

bool check(int n) {
    string s = to_string(n);
    bool flag = true;
    for (int i = 0; i < s.size() - 1; i++)
    {
        if (s[i] > s[i + 1])
        {
            flag = false;
            break;
        }
    }
    return flag;
}

int main() {
    int t; cin >> t;
    for(int i = 0; i < t; i++) {
        int n; cin >> n;
        while(!check(n--));
        cout << "Case #" << i+1 << ": " << n + 1 << endl;
    }

    return 0;
}