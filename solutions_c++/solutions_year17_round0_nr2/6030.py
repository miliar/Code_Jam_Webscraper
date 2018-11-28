#include <iostream>

using namespace std;

bool isTidy(unsigned long l) {
    string s = to_string(l);
    char last = '0';
    for (char i : s) {
        if (i < last) {
            return false;
        } else {
            last = i;
        }
    }
    return true;
}


unsigned long makeTidy(unsigned long s) {

    for (unsigned long i = s - 1; i != 0; i--) {
        if (isTidy(i)) {
            return i;
        }
    }

}

int main() {
    int t;
    cin >> t;

    for (unsigned i = 0; i < t; i++) {
        unsigned long temp;
        cin >> temp;
        unsigned long out;

        if (isTidy(temp)) {
            out = temp;
        } else {
            out = makeTidy(temp);
        }

        cout << "Case #" << i + 1 << ": " << out <<endl;
    }

    return 0;
}