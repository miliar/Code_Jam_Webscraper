#include <iostream>
#include <string>

using namespace::std;

int main() {
    int T;
    cin>>T;
    for (int i = 0; i < T; i++) {
        string N;
        cin>>N;
        int j = 1;
        while (j < N.length()) {
            int previous = N[j-1];
            int current = N[j];
            if (current < previous) {
                for (int k = j; k < N.length(); k++) {
                    N[k] = '9';
                }
                N[j-1] -= 1;
                j = 1;
                continue;
            }
            j++;
        }
        if (N[0] == '0') {
            N.erase(0, 1);
        }
        cout<<"Case #"<<i+1<<": "<<N<<'\n';
    }
    return 0;
}
