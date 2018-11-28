#include <iostream>

using namespace std;

void do_case(int t) {
    string s;
    cin >> s;

    bool v[1000];
    for(int i = 0; i<s.size(); i++) {
        v[i] = (s[i] == '+');
    }

    int size;
    cin >> size;
    int count = 0;
    for(int i = 0; i<s.size()-size+1; i++) {
        if(!v[i]) {
            count++;
            for(int j = i+1; j<i+size; j++) {
                v[j] = !v[j];
            }
        }
    }
    for(int i = s.size()-size+1; i<s.size(); i++) {
        if(!v[i]) {
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << "Case #" << t << ": " << count << endl;
}

int main() {
    int T;
    cin >> T;
    for(int t = 0; t<T; t++) {
        do_case(t+1);
    }
}
