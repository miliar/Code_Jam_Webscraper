#include <iostream>
#include <string>
using namespace std;

void solve(const int &tc) {
    string a;
    cin >> a;
    const int n = a.length();
    if(n == 1) {
        cout << "Case #" << tc << ": " << a << endl;
    } else {
        string ans;
        int i = 0;
        while(i < n-1 && a[i] <= a[i+1]) i++;
        if(i == n-1) ans = a;
        else {
            char x = a[i];
            while(i >= 0 && a[i] == x) i--;
            i++;
            a[i]--;
            for(int j=i+1;j<n;j++) a[j] = '9';
            ans = a;
        }
        if(ans[0] == '0') ans = ans.substr(1);
        cout << "Case #" << tc << ": " << ans << endl;
    }
}

int main() {
    int t; cin >> t;
    for(int i=1;i<=t;i++) solve(i);
}

