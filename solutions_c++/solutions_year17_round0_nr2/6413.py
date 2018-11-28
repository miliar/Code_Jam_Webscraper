#include <iostream>
using namespace std;

string N;
string P;

bool search(int k, char min, bool ext)
{
    if (k == N.length()) {
        return true;
    }

    char p = ext ? '9' : N[k];
    while(p >= min) {
        P.push_back(p);
        if (search(k + 1, p, ext || p != N[k])) return true;
        P.pop_back();
        p--;
    }

    return false;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        P = "";
        search(0, '0', false);
        int j;
        for (j = 0; j < P.length(); j++) {
            if (P[j] != '0') break;
        }
        cout << "Case #" << i + 1 << ": " << P.substr(j) << endl;
    }
    return 0;
}
