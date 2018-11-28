#include <bits/stdc++.h>
#include <cstring>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

template <typename T1, typename T2>
string print_iterable(T1 begin_iter, T2 end_iter, int counter) {
    bool done_something = false;
    stringstream res;
    res << "[";
    for (; begin_iter != end_iter and counter; ++begin_iter) {
        done_something = true;
        counter--;
        res << *begin_iter << ", ";
    }
    string str = res.str();
    if (done_something) {
        str.pop_back();
        str.pop_back();
    }
    str += "]";
    return str;
}

vector<int> SortIndex(int size, std::function<bool(int, int)> compare) {
    vector<int> ord(size);
    for (int i = 0; i < size; i++) ord[i] = i;
    sort(ord.begin(), ord.end(), compare);
    return ord;
}

template <typename T>
bool MinPlace(T& a, const T& b) {
    if (a > b) {
        a = b;
        return true;
    }
    return false;
}

template <typename T>
bool MaxPlace(T& a, const T& b) {
    if (a < b) {
        a = b;
        return true;
    }
    return false;
}

#define INF 1<<30
#define eps 1e-9

#if DEBUG && !ONLINE_JUDGE
    #define dbg_var(x) clog << #x  << ": " << x << endl;
    #define dbg_vec(x) clog << #x << ": " << print_iterable(x.begin(), x.end(), -1) << endl;
    #define dbg_array(x, len) clog << #x << ": " << print_iterable(x, x+len, -1) << endl;
#else
    #define dbg_var(x) 
    #define dbg_vec(x)
    #define dbg_array(x, len)
#endif

///////////////////////////////////////////////////////////////////////////
//////////////////// DO NOT TOUCH BEFORE THIS LINE ////////////////////////
///////////////////////////////////////////////////////////////////////////

const bool SET_THIS_TO_TRUE_FOR_OFFICIAL_SUBMISSION = true;
const string official_input_name = "B-large.in";

const string download_folder = "/home/dario2994/Scaricati/";

string SolveProblem(string s) {
    for (int i = 0; i < (int)s.size()-1; i++) {
        if (s[i] <= s[i+1]) continue;
        int start = i;
        while (start > 0 and s[start-1] == s[i]) start--;
        string res = s.substr(0, start);
        if (start != 0 or s[start] != '1') {
            char new_char = s[start]-1;
            res += new_char;
        }
        for (int j = start+1; j < (int)s.size(); j++) res += "9";
        return res;
    }
    return s;
}

int main() {
    int t;
    ios::sync_with_stdio(false);
    string input_filename = "";
    string output_filename = "";
    if (SET_THIS_TO_TRUE_FOR_OFFICIAL_SUBMISSION) {
        cout << "Execution of official Input" << endl;
        input_filename = download_folder + official_input_name;
        output_filename = "output.txt";
    } else {
        cout << "Reading SAMPLE test cases" << endl;
        input_filename = "input.txt";
        output_filename = "unofficial_output.txt";
    }
    ifstream in(input_filename);
    ofstream out(output_filename);
    in >> t;
    for (int testcase = 1; testcase <= t; testcase++) {
        // ReadInput
        string s;
        in >> s;
        auto res = SolveProblem(s);
        out << "Case #" << testcase << ": " << res;
        if (testcase < t) out << "\n";
        cout << "Case #" << testcase << ": " << res << endl;
    }
}
