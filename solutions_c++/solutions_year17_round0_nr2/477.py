// CodeJam 2017
// Problem B
// zintrepid

#include <iostream>
#include <string>
#include <tuple>


using namespace std;

string StringDecrement(const string& in)
{
    bool borrowing = true;
    string result;
    for (auto i = in.rbegin(); i != in.rend(); ++i) {
        if (borrowing) {
            if (*i == '0') {
                result.insert(0, 1, '9');
            } else {
                result.insert(0, 1, *i - 1);
                borrowing = false;
            }
        } else {
            result.insert(0, 1, *i);
        }
    }
    return result;
}

tuple<string, unsigned int> DoComp(string s)
{
    char v = '0';
    string res;
    unsigned int i;
    for (i=0; i < s.size() && s[i] >= v; ++i) {
        v = s[i];
        res.push_back(s[i]);
    }
    unsigned int rem = s.size() - i;
    if (rem != 0)
        res = StringDecrement(res);
    return make_tuple(res, rem);
}

bool DoRun()
{
    string w;
    cin >> w;
    if (cin.fail()) return false;
    unsigned int r=0, newr=1;
    while (newr != 0) {
        tie(w,newr) = DoComp(w);
        r += newr;
    }
    if ( w != "0" )
        cout << w;
    cout << string(r, '9');
    return true;
}

int main()
{
    int runs;
    cin >> runs;
    for (int i=0; i < runs; ++i) {
        cout << "Case #" << i + 1 << ": ";
        if (!DoRun()) {
            cerr << "RUN FAILED\n";
            return 1;
        }
        cout << "\n";
    }
    cerr << "Success.\n";
    return 0;
}
