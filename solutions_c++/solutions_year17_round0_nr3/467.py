

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

// overkill to go for exact probabilities since problem only requires 1e-6 precision...
//#include <gmp.h>
#include <gmpxx.h>


using namespace std;
typedef int64_t int64;

typedef pair<int, int> pii;
typedef pair<double, double> pdd;
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define all(x) (x).begin(), (x).end()

template<typename T>
int nextValue(std::istream &in) {
    T i;
    in >> i;
    return i;
}

template<typename T>
std::vector<T> readVector(std::istream &in, int n) {
    std::vector<T> c;
    std::generate_n(std::back_inserter(c), n, [&in]() { return nextValue<T>(in); });
    return c;
}

std::chrono::time_point<std::chrono::system_clock> now() { return std::chrono::system_clock::now(); }

double since(const std::chrono::time_point<std::chrono::system_clock> &t0) {
    return std::chrono::duration<double>(std::chrono::system_clock::now() - t0).count();
}

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
    virtual void read(std::istream &in) = 0;

    virtual void solve() { saw(out_); }

    virtual void write(std::ostream &out) { out << out_.str(); }

    string str() { return out_.str(); }

    operator string() { return out_.str(); }

protected:
    virtual void saw(std::ostream &out) = 0;    // solve and write
};

class Solver : public SolverBase {
    int64 n_;
    int64 k_;

public:
    virtual void read(std::istream &in);

protected:
    virtual void saw(std::ostream &out);
};


void Solver::read(std::istream &in) {
    in >> n_ >> k_;
}


void Solver::saw(std::ostream &out) {
    std::map<int64, int64, std::greater<int64>> slots;
    slots[n_] = 1;
    for (int64 k = k_; k > 0;) {
        auto big = slots.begin()->first;
        auto nbig = slots.begin()->second;
        slots.erase(slots.begin());
        int64 lo = (big - 1) / 2;
        int64 hi = big - 1 - lo;
        if (nbig >= k) {
            out << hi << " " << lo;
            return;
        }
        //std::cerr << hi << " " << lo << std::endl;
        k -= nbig;
        slots[lo] = slots[lo] + nbig;
        slots[hi] = slots[hi] + nbig;
    }
    throw 1;
}




int main() {
    freopen("C.in.txt", "r", stdin);
    freopen("C.out.txt", "w", stdout);
    auto t00 = std::chrono::system_clock::now();

    int nTestCases;
    cin >> nTestCases;

    // number of processors
    const int nThreads = min(max(int(thread::hardware_concurrency()), 1), nTestCases);

    if (nThreads <= 1) {
        // sequential processing: less memory and useful for debugging
        for (int it = 0; it < nTestCases; ++it) {
            Solver s;
            s.read(cin);
            s.solve();
            cout << "Case #" << (it + 1) << ": " << s.str() << endl;
        }
    } else {
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