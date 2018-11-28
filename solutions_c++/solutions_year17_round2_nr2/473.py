#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void docase() {
    int R,O,Y,G,B,V,N;
    cin >> N >> R >> O >> Y >> G >> B >> V;
    char last = ' ';
    string value = string(N,' ');
    if(max(max(R,Y),B) == R) {
        last = 'R';
        R--;
        value[0] = 'R';
    }
    else if(max(max(R,Y),B) == B) {
        last = 'B';
        B--;
        value[0] = 'B';
    }
    else {
        last = 'Y';
        Y--;
        value[0] = 'Y';
    }

    char special = last;

    for(int i = 1; i<N; i++) {
        if(last == 'R' && !B && !Y) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
        else if(last == 'B' && !R && !Y) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
        else if(last == 'Y' && !R && !B) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }

        if(last == 'R') {
            if(B > Y || (B == Y && special == 'B')) {
                value[i] = 'B';
                B--;
                last = 'B';
            }
            else {
                value[i] = 'Y';
                Y--;
                last = 'Y';
            }
        }
        else if(last == 'B') {
            if(R > Y || (R == Y && special == 'R')) {
                value[i] = 'R';
                R--;
                last = 'R';
            }
            else {
                value[i] = 'Y';
                Y--;
                last = 'Y';
            }
        }
        else if(last == 'Y') {
            if(B > R || (B == R && special == 'B')) {
                value[i] = 'B';
                B--;
                last = 'B';
            }
            else {
                value[i] = 'R';
                R--;
                last = 'R';
            }
        }
    }
    if(special == last) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    cout << value << endl;

}

int main() {
    int T;
    cin >> T;
    for(int i = 0 ; i<T; i++) {
        cout << "Case #" << i+1 << ": ";
        docase();
    }
}
