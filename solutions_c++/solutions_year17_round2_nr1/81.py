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
const string official_input_name = "A-large.in";

const string download_folder = "/home/dario2994/Scaricati/";

void SolveProblem(ifstream& in, ofstream& out) {
    // Read input
    LL D;
    int N;
    in >> D >> N;
    vector<LL> K(N);
    vector<LL> S(N);
    for (int i = 0; i < N; i++) {
        in >> K[i] >> S[i];
    }

    // Solve problem
    double res = 1e20;
    for (int i = 0; i < N; i++) {
        LL num = D * S[i];
        LL den = D - K[i];
        double ris = ((double)num) / (double)den;
        MinPlace(res, ris);
    }
    
    // Write output
    out.precision(10);
    out << fixed << res << "\n";
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
