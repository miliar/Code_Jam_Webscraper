#include<iostream>
#include<string>

using namespace std;

int is_tidy(string n) {
    char a=n[0];
    int i=1;
    for (; i<n.size(); i++) {
        if(a>n[i]) {
            return i;
        }
        a = n[i];
    }
    return i;
}

string prev_tidy(string n) {
    int p = is_tidy(n);
    if (p==n.size()) {
        n[n.size()-1]--;
        if (is_tidy(n)==n.size()) {
            return n;
        }
    }
    string pa = prev_tidy(n.substr(0, p));
    string pb = string(n.size()-p, '9');
    return pa + pb;
}

string leading_zeroes(string n) {
    int i=0;
    while (n[i] == '0') i++;
    return n.substr(i);
}

int main() {
    int n_cases;
    string n;
    
    cin >> n_cases;
    
    for (int i=0; i<n_cases; i++) {
        cout << "Case #" << i+1 <<  ": ";
        cin >> n;
        if (is_tidy(n) == n.size()) {
            cout << n << endl;
        }
        else {
            cout << leading_zeroes(prev_tidy(n)) << endl;
        }
    }
    return 0;
}
