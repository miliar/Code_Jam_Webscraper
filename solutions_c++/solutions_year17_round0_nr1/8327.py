#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm> 

using namespace std;
string input = 1? "A-small-attempt3.in": "Input";
string output = 1?  "A-small-attempt3.out" : "Output";

int flip_x_isolated(vector<bool> &f, int k, int x);
bool adjust(vector<bool>& f, int k);

string pancake(string s) {
    vector<bool> f;
    int k = stoi(s.substr(s.find(' ')));
    for (auto x : s)
        if (x == '+' || x == '-') f.push_back(x == '+');

    int r = 0, or, t, x;
    while (find(f.begin(), f.end(), false) != f.end() && f.size() >= k) {
        or = r;
        t = 0;
        x = k;
        while (!(t = flip_x_isolated(f, k, x)) && --x);
        r += t;
        while (adjust(f, k));
        if (r == or) return "IMPOSSIBLE";
    }

    return find(f.begin(), f.end(), false) != f.end()? "IMPOSSIBLE" : to_string(r);
}

int flip_x_isolated(vector<bool>& f, int k, int x) {
    if (x == 0 || k == 0 || f.size() < k) return 0;
    int r = 0, c;
    for (int i = 0; i+k <= f.size(); i += c + 1) {
        c = 0;
        while (c < x && i + c < f.size() && !f[i + c]) c++;
        if (c == x) {
            for (int j = i; j < k + i; j++) f[j] = !f[j];
            r++;
            c--;
        }
    }
    return r;
}

bool adjust(vector<bool>& f, int k) {
    if (k == 0 || f.size() < k) return false;
    int i = 0;
    for (; i + k <= f.size() && f[i] == f[0] && i<k; i++);
    if (i == k) {
        f.erase(f.begin(), f.begin() + k);
        return true;
    }
    return false;
}

int WinMain() {
    ifstream in;
    ofstream out;
    in.open(input);
    out.open(output);
    string s, r;
    getline(in, s);
    int n = stoi(s), i = 0;
    while (getline(in, s) && ++i<=n) {
        r = pancake(s);
        out << "Case #" << i <<": "<< r << endl;
    }
    in.close();
    out.close();
    return 0;
}


