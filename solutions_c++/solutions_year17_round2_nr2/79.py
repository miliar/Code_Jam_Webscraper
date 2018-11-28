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

void SolveProblem(ifstream& in, ofstream& out) {
    // Read input
    int  N, R, O, Y, G, B, V;
    in >> N >> R >> O >> Y >> G >> B >> V;
    // O -> B
    // G -> R
    // V -> Y
    // Solve problem
    int B2 = B-O;
    int R2 = R-G;
    int Y2 = Y-V;
    if (B2 == 0 and B > 0) {
        if (N > B + O) {
            out << "IMPOSSIBLE" << "\n";
            return;
        } else {
            string s = "";
            for (int i = 0; 2*i < N; i++) {
                s += "BO";
            }
            out << s << "\n";
            return;
        }
    }
    if (R2 == 0 and R > 0) {
        if (N > R + G) {
            out << "IMPOSSIBLE" << "\n";
            return;
        } else {
            string s = "";
            for (int i = 0; 2*i < N; i++) {
                s += "RG";
            }
            out << s << "\n";
            return;
        }
    }
    if (Y2 == 0 and Y > 0) {
        if (N > Y+V) {
            out << "IMPOSSIBLE" << "\n";
            return;
        } else {
            string s = "";
            for (int i = 0; 2*i < N; i++) {
                s += "YV";
            }
            out << s << "\n";
            return;
        }
    }
    
    if (B2 < 0 or R2 < 0 or Y2 < 0) {
        out << "IMPOSSIBLE" << "\n";
        return;
    }
    if (B2 > R2 + Y2 or R2 > B2 + Y2 or Y2 > R2 + B2) {
        out << "IMPOSSIBLE" << "\n";
        return;
    }
    // doable!

    pair<int, char> ord[3] = {{R2, 'R'}, {B2, 'B'}, {Y2, 'Y'}};
    sort(ord, ord+3);
    string preris;
    for (int i = 0; i < R2+B2+Y2; i++) {
        if (i%2 == 0 and ord[2].first > 0) {
            preris += ord[2].second;
            ord[2].first--;
        } else {
            if (ord[0].first > ord[1].first) {
                preris += ord[0].second;
                ord[0].first--;
            } else {
                preris += ord[1].second;
                ord[1].first--;
            }
        }
    }
    assert(ord[0].first == 0);
    assert(ord[1].first == 0);
    assert(ord[2].first == 0);

    string res = "";
    bool ODone = false;
    bool GDone = false;
    bool VDone = false;
    // O -> B
    // G -> R
    // V -> Y
    for (int i = 0; i < (int)preris.size(); i++) {
        res += preris[i];
        if (preris[i] == 'B' and !ODone) {
            for (int j = 0; j < O; j++) res += "OB";
            ODone = true;
        }
        if (preris[i] == 'R' and !GDone) {
            for (int j = 0; j < G; j++) res += "GR";
            GDone = true;
        }
        if (preris[i] == 'Y' and !VDone) {
            for (int j = 0; j < V; j++) res += "VY";
            VDone = true;
        }
    }
    assert((int)res.size() == N);
    out << res << "\n";
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
        out << "Case #" << testcase << ": ";  // Consider adding a new line.
        cout << "Case #" << testcase << endl; // Idea of the status.
        SolveProblem(in, out);
    }
    in.close();
    out.close();

    // Print output on screen.
    cout << endl;   
    ifstream generated_output(output_filename);
    cout << generated_output.rdbuf();
}
