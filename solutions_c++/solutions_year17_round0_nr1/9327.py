#include<bits/stdc++.h>
using namespace std;

void update_visited(int& visited, int number) {
    while(number) {
        visited|=(1<<(number%10));
        number/=10;
    }
}

static const int dbg = 0;
#define dout if(dbg)cout

void solve() {
    string pancakes;
    int K;
    cin >> pancakes >> K;
    int n = 0;
    string clone = pancakes;
    for(int i=0; i<=pancakes.length()-K; ++i) {
        dout << "DEBUG i = " << i << " counter = " << n << endl; 
        dout << " pancakes[i] " << pancakes[i] << endl;
        if( pancakes[i] == '-') {
            ++n;
            for(int j=0; j<K; ++j) {
                if(pancakes[i+j]=='+') {
                    pancakes[i+j] = '-';
                } else {
                    pancakes[i+j] = '+';
                }
            }
        }
    }
    for(int i=pancakes.length()-K; i<pancakes.length(); ++i) {
        if(pancakes[i]=='-') {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << n << endl; 
}

int main() {
    int n_testcases, start_number;
    scanf("%d", &n_testcases);
    for(int i=1; i<=n_testcases; ++i) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
