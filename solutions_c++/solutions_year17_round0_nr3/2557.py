#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <deque>

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

void solveTaskB(string infile, string outfile) {
    ifstream in;
    in.exceptions(std::ifstream::failbit);
    in.open(infile);
    ofstream out;
    out.open(outfile);
    int ncases = 0;
    in >> ncases;
    for (int c = 1; c <= ncases; c++) {
        string s;
        in >> s;
        int pos = 1;
        while (pos < s.length() && s[pos - 1] <= s[pos]) pos++;
        out << "Case #" << c << ": ";
        if (pos < s.length()) {
            do {
                pos--;
            } while (s[pos] - 1 < s[pos - 1]);
            s[pos]--;
            for (int i = pos + 1; i < s.length(); i++) s[i] = '9';
        }
        if (s[0] == '0') s = s.substr(1);
        out << s;
        out << endl;
    }
    in.close();
    out.close();
}

void solveTaskC(string infile, string outfile) {
    ifstream in;
    in.exceptions(std::ifstream::failbit);
    in.open(infile);
    ofstream out;
    out.open(outfile);
    int ncases = 0;
    in >> ncases;
    for (int c = 1; c <= ncases; c++) {
        uint64_t n, k, x, y, z;
        in >> n >> k;
        deque<uint64_t> s;
        s.push_back(n);
        map<uint64_t, uint64_t> d;
        d[n] = 1;
        uint64_t p = 0;
        while (!s.empty()) {
            x = s.front();
            s.pop_front();
            p += d[x];
            z = (x - 1) / 2;
            y = x - 1 - z;
            if (y > 0) {
                if (d.find(y) == d.end()) {
                    s.push_back(y);
                    d[y] = 0;
                }
                d[y] += d[x];
            }
            if (z > 0) {
                if (d.find(z) == d.end()) {
                    s.push_back(z);
                    d[z] = 0;
                }
                d[z] += d[x];
            }
            if (p >= k) break;
        }
        out << "Case #" << c << ": ";
        out << y << " " << z;
        out << endl;
    }
    in.close();
    out.close();
}


int main()
{
    solveTaskC("C-large.in", "output.txt");
    return 0;
}
