#include <iostream>
#include <string>

using namespace std;


int main() {
    int T, c, x;
    string N;

    c=0;

    cin >> T;

    while(T) {
        T--;
        c++;

        cin >> N;

        for(x=1; x<N.length(); x++) {
            if(N[x]>=N[x-1]) continue;
            N[x-1]--;
            while(x<N.length()) {
                N[x]='9';
                x++;
            }
            x=0;
        }

        cout << "Case #" << c << ": ";

        for(x=0; x<N.length(); x++) if(N[x]!='0') break;
        while(x<N.length()) {
            cout << N[x];
            x++;
        }

        cout << endl; 
    }

    return 0;
}

