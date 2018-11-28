#include <iostream>

using namespace std;

void do_case() {
    string n;
    cin >> n;
    char digit = '0';
    int i = 0;
    while(digit <= n[i] && i<n.size()) {
        digit = n[i];
        i++;
    }
    if(i==n.size()) {
        cout << n << endl;
        return;
    }
    int indicestop = i;
    i--;
    digit = n[i]-1;
    while(digit < n[i] && i>= 0) {
        i--;
    }
    if(i<0 && n[0] == '1') {
        cout << string(n.size()-1,'9') << endl;
        return;
    }
    i++;
    n[i]--;
    i++;
    for(;i<n.size();i++) {
        n[i] = '9';
    }
    cout << n << endl;
}

int main() {
    int T;
    cin >> T;
    for(int i = 0; i<T; i++) {
        cout << "Case #" << i+1 << ": ";
        do_case();
    }
    return 0;
}
