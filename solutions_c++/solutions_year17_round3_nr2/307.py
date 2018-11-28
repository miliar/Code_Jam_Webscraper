

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
#include <numeric>

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
    std::vector<int> c;
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

struct Shift {
    int parent = 0;
    int begin = 0;
    int end = 0;
    int length = 0;
};

class Solver : public SolverBase {
    vector<Shift> s;
public:
    virtual void read(std::istream &in);

protected:
    virtual void saw(std::ostream &out);
};


void Solver::read(std::istream &in) {
    int c, j;
    in >> c >> j;
    s.resize(c + j);
    for (int i = 0; i < c + j; ++i) {
        s[i].parent = int(i >= c);
        in >> s[i].begin >> s[i].end;
        s[i].length = s[i].end - s[i].begin;
    }
}

void Solver::saw(std::ostream &out) {
    int day = 60 * 24;
    int halfday = 60 * 12;
    int n = int(s.size());
    std::sort(s.begin(), s.end(), [this](Shift const & a, Shift const & b)->bool { return a.begin < b.begin;});
    int nc = 0;
    vector<int> shiftSum(2, 0);
    vector<int> gapSum(2, 0);
    vector<vector<int>> gap(2);
    for (int i = 0; i < n; ++i) {
        shiftSum[s[i].parent] += s[i].length;
        if (s[i].parent != s[(i-1+n)%n].parent) {
            nc++;
        }
        else {
            int pend = i == 0 ? s[n-1].end - day : s[i - 1].end;
            int delta = s[i].begin - pend;
            if (delta > 0) {
                int pp = s[i].parent;
                gap[pp].push_back(delta);
                gapSum[pp] += gap[pp].back();
            }
        }
    }
    for (int p = 0; p < 2; ++p) {
        int extra = gapSum[p] + shiftSum[p] - halfday;
        if (extra > 0) {
            std::sort(gap[p].begin(), gap[p].end(), std::greater<int>());
            for (auto g : gap[p]) {
                extra -= g;
                nc += 2;
                if (extra <= 0)
                    break;
            }
            break;
        }
    }
    out << nc;
}


int main() {
    freopen("B.in.txt","r",stdin);
    freopen("B.out.txt","w",stdout);
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