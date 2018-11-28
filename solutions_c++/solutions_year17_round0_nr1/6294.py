#include <iostream>
#include <fstream>

using namespace std;

void flip(char& c) {
    if (c == '+')
        c = '-';
    else if (c == '-')
        c = '+';
}

int main() {
    ifstream in("a.in");
    ofstream out("a.out");
    int T = -1;
    in >> T;
    for (int t = 0; t < T; ++t) {
        std::string str;
        int k;
        in >> str;
        in >> k;
        cout << t << ":" << endl;
        int cnt = 0;
        for (int i = 0; i <= str.size() - k; ++i) {
            if (str[i] == '-') {
                cnt++;
                for (int j = 0; j < k; ++j)
                    flip(str[i + j]);
//                cout << str << endl;
            }
        }

        out << "Case #" << t + 1 << ": ";
        if (str.find('-') == string::npos)
            out << cnt;
        else
            out << "IMPOSSIBLE";
        out << "\n";
    }
    return 0;
}
