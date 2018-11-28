
#include <iostream>
#include <string>
using namespace std;

string tidynum(string);

int main() {
    int cases;
    string n;
    cin >> cases;
    for (int c = 1; c <= cases; c++) {
        cin >> n;
        cout << "Case #" << c << ": " << tidynum(n) << endl;
    }
}

string tidynum(string n) {
    if (n.empty() || n.length() == 1) return n;
    int i = (int)n.length()-2;
    while (i >= 0) {
        if (n[i] > n[i+1]) {
            n[i]--;
            int k = i+1;
            while (k < n.length() && n[k] != '9')
                n[k++] = '9';
        }
        i--;
    }

    i = 0;
    while (i < n.length() && n[i] == '0') i++;
    return n.substr(i, n.length()-i+1);
}
