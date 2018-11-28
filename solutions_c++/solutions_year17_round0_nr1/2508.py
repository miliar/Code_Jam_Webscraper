#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void solveTaskA(string infile, string outfile) {
    ifstream in;
    in.exceptions(std::ifstream::failbit);
    in.open(infile);
    ofstream out;
    out.open(outfile);
    int ncases = 0;
    in >> ncases;
    for (int c = 1; c <= ncases; c++) {
        string s;
        int k;
        in >> s >> k;
        int res = 0;
        for (int i = 0; i + k <= s.length(); i++) {
            if (s[i] == '+') continue;
            res++;
            for (int j = i; j < i + k; j++)
                s[j] = s[j] == '-' ? '+' : '-';
        }
        bool ok = true;
        for (int i = 0; i < s.length(); i++)
            if (s[i] == '-') ok = false;
        out << "Case #" << c << ": ";
        if (ok) out << res; else out << "IMPOSSIBLE";
        out << endl;
    }
    in.close();
    out.close();
}

int main()
{
    solveTaskA("C:/work/tmp/A-large.in", "C:/work/tmp/output.txt");
    return 0;
}
