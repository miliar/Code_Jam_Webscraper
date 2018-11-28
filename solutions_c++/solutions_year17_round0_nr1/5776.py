#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void flipK(string& s, int start, int k) {
    for (int i = start; i < start + k; i++) {
        if (s[i] == '+') {
            s[i] = '-';
        } else {
            s[i] = '+';
        }
    }
}

int main()
{
    int t;
    string s;
    ifstream fin("in.txt");
    ofstream f("out.txt");

    fin >> t;
    for (int i = 0; i < t; i++) {
        int k;
        fin >> s >> k;
        f << "Case #"<< i+1 << ": ";
        int count = 0;
        for (int j = 0; j <= s.length() - k; j++) {
            if (s[j] == '-') {
                flipK(s, j, k);
                count++;
            }
        }
        bool imp = false;
        for (int j = s.length() - k + 1; j < s.length(); j++) {
            if (s[j] == '-') {
                f << "IMPOSSIBLE";
                imp = true;
                break;
            }
        }
        if (!imp) {
            f << count;
        }
        f << "\n";
    }

    f.close();
    return 0;
}
