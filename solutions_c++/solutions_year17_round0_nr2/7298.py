#include <string>
#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int cs=1; cs<=T; ++cs) {
        string S;
        cin >> S;
        const int z=S.length();
        for (int i=z-1; i>0; --i) {
            if (S[i-1]<=S[i]) continue;
            --S[i-1];
            for (int j=i; j<z && S[j] != '9'; ++j) S[j] = '9';
        }
        int i=0;
        while (S[i]=='0') ++i;
        cout << "Case #" << cs << ": ";
        for (;i<z; ++i) cout << S[i];
        cout << "\n";
    }
}
