#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm> 

using namespace std;
string input = 0 ? "B-small-attempt0.in" : "B-large.in";
string output = 0 ? "B-small-attempt0.out" : "B-large.out";


string tidy(string& s) {
    auto next = [&](int i) {
        s[i - 1]--;
        for (int j = i; j < s.size(); j++) s[j] = '9';
        return true;
    };
    int i;
    do {
        for (i = 1; i < s.size() && s[i-1] <= s[i]; i++);
    } while (i != s.size() && next(i));
    return  to_string(stoull(s));
}


int WinMain() {
    ifstream in;
    ofstream out;
    in.open(input);
    out.open(output);
    string s, r;
    getline(in, s);
    int n = stoi(s), i = 0;
    while (getline(in, s) && ++i <= n) {
        r = tidy(s);
        out << "Case #" << i << ": " << r << endl;
    }
    in.close();
    out.close();
    return 0;
}


