

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
double since(const std::chrono::time_point<std::chrono::system_clock> &t0)
    { return std::chrono::duration<double>(std::chrono::system_clock::now() - t0).count(); }

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
    int64 n_;
    int64 p_;
    std::vector<int64> r_;
    std::vector<std::vector<int64>> q_;
public:
    virtual void read(std::istream &in);

protected:
    virtual void saw(std::ostream &out);

    int64 countKits(vector<int> pos, int m);

    bool hasInteger(double lo, double hi) const;

    bool has99(int64 all, int64 hiAll);
};


void Solver::read(std::istream &in) {
    in >> n_ >> p_;
    r_ = readVector<int64>(in, n_);
    q_.resize(n_);
    for (int i = 0; i < n_; ++i) {
        q_[i] = readVector<int64>(in, p_);
    }
}

#if 1

void Solver::saw(std::ostream &out) {
    int64 nk = 0;
    for (auto & v : q_)
        std::sort(all(v));
    std::vector<int> pos(n_);
    std::vector<int64> lo(n_);
    std::vector<int64> hi(n_);
    while (true) {
        for (int i = 0; i < n_; ++i) {
            hi[i] = q_[i][pos[i]] * 110 / r_[i];    // * 99
            lo[i] = q_[i][pos[i]] * 90 / r_[i];
        }
        int64 loAll = *std::max_element(all(lo));
        int64 hiAll = *std::min_element(all(hi));
        if (has99(loAll, hiAll)) {
            nk++;
//            cerr << loAll/99.0 << "..." << hiAll/99.0 << endl;
            for (int i = 0; i < n_; ++i) {
                pos[i]++;
            }
            if (*std::max_element(all(pos)) == p_) {
                break;
            }
        }
        else {
            int ilo = (int) (std::min_element(all(lo)) - std::begin(lo));
            pos[ilo]++;
            if (pos[ilo] == p_)
                break;
        }
    }
//    nk = countKits(pos, 0);
    out << nk;
}

#else
void Solver::saw(std::ostream &out) {
    int64 nk = 0;
    for (auto & v : q_)
        std::sort(all(v));
    std::vector<int> pos(n_);
    std::vector<double> lo(n_);
    std::vector<double> hi(n_);
    while (true) {
        for (int i = 0; i < n_; ++i) {
            hi[i] = q_[i][pos[i]] / 0.9 / r_[i];
            lo[i] = q_[i][pos[i]] / 1.1 / r_[i];
        }
        auto loIt = std::max_element(all(lo));
        double loAll = *loIt;
        double hiAll = *std::min_element(all(hi));
        if (hasInteger(loAll, hiAll)) {
            nk++;
//            cerr << loAll/99.0 << "..." << hiAll/99.0 << endl;
            for (int i = 0; i < n_; ++i) {
                pos[i]++;
            }
            if (*std::max_element(all(pos)) == p_) {
                break;
            }
        }
        else {
            int ilo = (int) (std::min_element(all(lo)) - std::begin(lo));
            pos[ilo]++;
            if (pos[ilo] == p_)
                break;
        }
    }
//    nk = countKits(pos, 0);
    out << nk;
}
#endif

bool Solver::hasInteger(double lo, double hi) const {
    hi = floor(hi*(1+1e-10));
    lo = ceil(lo*(1-1e-10));
    return lo <= hi || abs(hi - lo) < 1e-10;
}

int64 Solver::countKits(vector<int> pos, int m) {
    return 0;
}

bool Solver::has99(int64 lo, int64 hi) {
    return lo <= hi / 99 * 99;
}


int main() {
    freopen("B.in.txt","r",stdin);
    freopen("B.out.txt","w",stdout);
    auto t00 = std::chrono::system_clock::now();

    int nTestCases;
    cin >> nTestCases;

    // number of processors
    const int nThreads = min(max(int(thread::hardware_concurrency()), 1), nTestCases);

    if (nThreads <= 100) {
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