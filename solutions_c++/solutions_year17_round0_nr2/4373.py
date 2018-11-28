#include<bits/stdc++.h>
using namespace std;

int main() {
    string N = "";
    int tc = 0, start = 0;
    bool reduse = false;
    cin >> tc;
    for(int t = 1; t <= tc; ++t) {
        cin >> N;
        for(int k = 0; k <= N.size(); ++k) {
            for(int i = 0 ; i < N.size() - 1; ++i) {
                if(N[i+1] < N[i]) {
                    N[i] = N[i] - 1;
                    for(int j = i + 1; j < N.size(); ++j) N[j] = '9';
                    break;
                }
            }
        }
        cout << "Case #" << t << ": ";
        start = 0;
        while(N[start] == '0') ++start;
        for(int i = start ; i < N.size(); ++i) {
            cout << N[i];
        }
        cout << endl;
    }
    return 0;
}
