#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <climits>

using namespace std;

int main() {
    int T; cin >> T;
    for(int cs = 1; cs <= T; cs++) {
        cout << "Case #" << cs << ": ";
        string Ns; cin >> Ns;
        int len = Ns.length();
        for(int i = len - 1; i > 0; i--) {
            if(Ns[i-1] > Ns[i]) {
                for(int j = i; j < len; j++)
                    Ns[j] = '9';
                while(Ns[i-1] == '0') {
                    Ns[i-1] = '9';
                    i--;
                }
                Ns[i-1]--;
            }
        }
        int index = 0;
        while(Ns[index] == '0')
            index++;
        for(; index < len; index++) {
            cout << Ns[index];
        }
        cout << endl;
    }
    return 0;
}
