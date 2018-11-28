#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm> 

using namespace std;
string input = 1 ? "C-small-1-attempt2.in" : "Input";//"C-large.in";
string output = 1 ? "C-small-1-attempt2.out" : "Output"; //"C-large.out";

typedef pair<int, int> pai;
typedef vector<pai> vec;
typedef vec::iterator ite;
typedef unsigned long long ull;

void update(vec& stalls, ull mi);
ull maxmin_or_max(vec stalls);

string bathroom(string& s) {
    ull v = s.find(' ');
    ull n = stoull(s.substr(0, v)), 
        k = stoull(s.substr(v + 1));
    vec stalls;
    for (int i = 0; i < n; i++) stalls.push_back(make_pair(i, n - i - 1));

    pai old;
    ull mi = 0;
    do {
        mi = maxmin_or_max(stalls);
        old = stalls[mi];
        update(stalls, mi);
    } while (--k && stalls.size() > 0);

    return to_string(max(old.first, old.second)) + " " +
                     to_string(min(old.first, old.second));
}

void update(vec& stalls, ull mi) {
    ite x = stalls.begin() + mi;
    (*x).first = 0;
    (*x).second = 0;
    ull i = 0;
    for (++x; x != stalls.end() && (*x).first != 0; ++x) (*x).first = i++;
    if (mi > 0) {
        x = stalls.begin() + mi;
        i = 0;
        for (--x; x > stalls.begin() && (*x).second != 0; --x) (*x).second = i++;
        if (x == stalls.begin()) (*x).second = i;
    }
}

ull maxmin_or_max(vec stalls) {
    ull m = 0;
    for (ull i = 0; i < stalls.size(); i++) {
        ull t = min(stalls[i].first, stalls[i].second);
        if (t > m) m = t;
    }

    vector<ull> mi;
    for (ull i = 0; i < stalls.size(); i++) if (min(stalls[i].first, stalls[i].second) == m) mi.push_back(i);
    ull r = mi[0];
    if (mi.size() > 0) {
        for (auto i : mi) {
            ull t = max(stalls[i].first, stalls[i].second);
            if ( t > m) {
                m = t;
                r = i;
            }
        }
    }
    return r;
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
        r = bathroom(s);
        out << "Case #" << i << ": " << r << endl;
    }
    in.close();
    out.close();
    return 0;
}


