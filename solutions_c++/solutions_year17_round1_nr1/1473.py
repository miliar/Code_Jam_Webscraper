#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

string expand(string s) {
    int n = s.size();
    for(int i = 0; i<s.size(); i++) {
        int j = i;
        while(s[i] == '?' && i<s.size()) {
            i++;
        }
        if(i<s.size()) {
            for(int k = j; k<i; k++) {
                s[k] = s[i];
            }
        }
    }
    int i = s.size()-1;
    while(s[i] == '?') {
        i--;
    }
    for(int k = i+1; k<s.size(); k++) {
        s[k] = s[i];
    }
    return s;
}

void docase() {
    int r,c;
    cin >> r >> c;
    vector<string > map = vector<string >(r);
    for(int i = 0; i<r; i++) {
        cin >> map[i];
    }

    int j = 0;
    while(map[j] == string(c,'?')) {
        j++;
    }
    for(int i = j; i<r; i++) {
        if(map[i] == string(c,'?')) {
            map[i] = map[i-1];
        }
        else {
            map[i] = expand(map[i]);
        }
    }
    for(int i = 0; i<j; i++) {
        map[i] = map[j];
        }
    cout << endl;
    for(int i = 0; i<r; i++) {
        cout << map[i] << endl;
    }
}

int main() {
    int T;
    cin >> T;
    for(int i = 0 ; i<T; i++) {
        cout << "Case #" << i+1 << ": ";
        docase();
    }
}
