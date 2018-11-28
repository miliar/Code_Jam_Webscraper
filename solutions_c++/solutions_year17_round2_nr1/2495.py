

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
#include <fstream>
#include <future>
#include <thread>
#include <chrono>
#include <iomanip>
#include <thread>
#include <atomic>

using namespace std;
typedef int64_t int64;

typedef pair<int,int> pii;
typedef pair<double,double> pdd;
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define all(x) (x).begin(), (x).end()

template<typename T>
int nextValue(std::istream & in) {
    T i;
    in >> i;
    return i;
}

template<typename T>
std::vector<T> readVector(std::istream &in, int n) {
    std::vector<T> c;
    std::generate_n(std::back_inserter(c), n, [&in](){ return nextValue<T>(in); });
    return c;
}

std::chrono::time_point<std::chrono::system_clock> now() { return std::chrono::system_clock::now(); }
double since(const std::chrono::time_point<std::chrono::system_clock> &t0) { return std::chrono::duration<double>(std::chrono::system_clock::now() - t0).count(); }

static int64 gcd(int64 a, int64 b) {
    if (a < 0 || b < 0)
        return -1;
    while (b != 0) {
        int64 x = a % b;
        a = b;
        b = x;
    }
    return a;
}

class SolverBase {
    std::ostringstream out_;
public:
    virtual void read(std::istream & in) = 0;
    virtual void solve() { saw(out_); }
    virtual void write(std::ostream & out) { out << out_.str(); }
    string str() { return out_.str(); }
    operator string() { return out_.str(); }

protected:
    virtual void saw(std::ostream & out) = 0;	// solve and write
};

class Solver : public SolverBase {
    int64 d_;
    int n_;
    vector<int64> k_;
    vector<int> s_;
public:
    virtual void read(std::istream &in);

protected:
    virtual void saw(std::ostream &out);
};


void Solver::read(std::istream &in) {
    in >> d_ >> n_;
    k_.resize(n_);
    s_.resize(n_);
    for (int i = 0; i < n_; ++i) {
        in >> k_[i] >> s_[i];
    }
}

void Solver::saw(std::ostream &out) {
    double r;
    vector<double> arrival(n_);
    double last = 0;
    for (int i = 0; i < n_; ++i) {
        arrival[i] = double(d_ - k_[i]) / s_[i];
        last = max(last, arrival[i]);
    }
    r = d_ / last;
    out.precision(8);
    out << fixed;
    out.precision(6);
    out <<  r;
//    const long double pi = std::acos(-1.L);
//    out << "default precision (6): " << pi << '\n'
//              << "std::setprecision(10): " << std::setprecision(10) << pi << '\n'
//              << "max precision:         "
//              << std::setprecision(std::numeric_limits<long double>::digits10 + 1)
//              << pi << '\n';
}

int main() {
    freopen("A.in.txt","r",stdin);
//    freopen("/Users/xan/Downloads/A-large-practice.in","r",stdin);
    freopen("A.out.txt","w",stdout);

    auto t00 = std::chrono::system_clock::now();

    int nTestCases;
    cin >> nTestCases;

    // number of processors
    const int nThreads = min(max(int(thread::hardware_concurrency()), 1), nTestCases);

    if (nThreads <= 111) {
        // sequential processing: less memory and useful for debugging
        for (int it = 0; it < nTestCases; ++it) {
            Solver s;
            s.read(cin);
            s.solve();
            cout << "Case #" << (it + 1) << ": " << s.str() << endl;
        }
    }
    else {
        // parallel processing with simple thread pool
        vector<Solver> s(nTestCases);
        // read all input sequentially
        for (int it = 0; it < nTestCases; ++it) {
            s[it].read(cin);
        }

        atomic<int> next(0);    // the next case that needs a worker thread
        atomic<int> done(0);    // only used for progress reporting

        auto work = [&next, &done, &s, &nTestCases, t00](void) {
            while (true) {
                int i = next++; // this atomic operation is how the threads synchronize with each other
                if (i >= nTestCases)
                    return;
                //fprintf(stderr, "start %3d\n", i + 1);
                auto t0 = now();
                s[i].solve();
                double t = since(t0);
                done++;
                if (t > 0.01)
                    fprintf(stderr, "%3d : %3d / %d = %.2f | %.2f\n", i + 1, int(done), nTestCases, t,
                            since(t00) / done * nTestCases);
            }
        };
        vector<thread> workers;
        // start worker threads
        for (int i = 0; i < nThreads; ++i) {
            workers.push_back(thread(work));
        }
        // wait for all workers to complete
        for (int i = 0; i < nThreads; ++i) {
            workers[i].join();
        }
        // report results
        for (int it = 0; it < nTestCases; ++it) {
            cout << "Case #" << (it + 1) << ": " << s[it].str() << endl;
        }
    }
    fprintf(stderr, "%.2f\n", since(t00));
    return 0;
}