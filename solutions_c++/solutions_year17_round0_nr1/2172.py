#include <iostream>
#include <vector>
using namespace std;

int get_flips(vector<bool>& v, int k) {
    int size = v.size();
    int flips = 0;
    for(int i = 0; i <= size-k; ++i) {
        if(!v[i]) {
            ++flips;
            bool down = false;
            int aux = 0;
            for(int j = i; j < i+k; ++j) {
                v[j] = !v[j];
                if(!down) {
                    aux = j;
                    if(!v[j]) {
                        down = true;
                    }
                }
            }
            if(down) {
                i = aux-1;
            } else {
                i = aux;
            }
        }
    }
    for(int i = size-k+1; i < size; ++i) {
        if(!v[i]) {
            return -1;
        }
    }
    return flips;
}

int main() {
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        string s;
        int k;
        cin >> s >> k;
        vector<bool> v(s.size());
        for(int j = 0; j < v.size(); ++j) {
            v[j] = s[j] == '+';
        }
        cout << "Case #" << i << ": ";
        int flips = get_flips(v, k);
        if(flips >= 0) {
            cout << flips << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
}