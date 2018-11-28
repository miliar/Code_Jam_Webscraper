#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int q = 1; q <= T; q++) {
        string inp;
        cin >> inp;
        for (int x = inp.size() - 1; x > 0; x--) {
            if (int(inp[x]) < int(inp[x - 1])) {
                string b = to_string(int(inp[x - 1]) - 49);
                char a = b[0];
                inp[x - 1] = a;
                for (int i = x; i < inp.size(); i++) {
                    inp[i] = '9';
                }
            }
        }
        int x = 0;
        while (inp[x] == '0')
            x++;
        inp = inp.substr(x, inp.size());
        cout << "Case #" << q << ": " << inp << endl;
    }
    return 0;
}