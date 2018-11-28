

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

struct Board {
    int n;
    int score = 0;
    std::string s;
    std::vector<int> r;
    std::vector<int> c;
    std::vector<int> d1;
    std::vector<int> d2;

    Board add(int i, int j, char m) const {
        Board b = *this;
        int ij = i * n + j;
        if (s[ij] == m || (m != 'o' && s[ij] != '.'))
            throw 2;
        b.s[ij] = m;
        b.score++;
        if (m == 'o' && s[ij] == '.')
            b.score++;
        if (m == 'o' || m == '+') {
            int id1 = i + j;
            int id2 = i - j + n - 1;
            b.d1[id1] = 1;
            b.d2[id2] = 1;
        }
        if (m == 'o' || m == 'x') {
            b.r[i] = 1;
            b.c[j] = 1;
        }
        return b;
    }

    void update(int i, int j, char m)  {
        int ij = i * n + j;
        if (s[ij] == m || (m != 'o' && s[ij] != '.'))
            throw 2;
        score++;
        if (m == 'o' && s[ij] == '.')
            score++;
        if (m == 'o' || m == '+') {
            int id1 = i + j;
            int id2 = i - j + n - 1;
            d1[id1] = 1;
            d2[id2] = 1;
        }
        if (m == 'o' || m == 'x') {
            r[i] = 1;
            c[j] = 1;
        }
        s[ij] = m;
    }

    bool canUpdate(int i, int j, char m) const {
        int ij = i * n + j;
        int id1 = i + j;
        int id2 = i - j + n - 1;
        switch (m) {
            case '+' : return s[ij] == '.' && d1[id1] == 0 && d2[id2] == 0;
            case 'x' : return s[ij] == '.' && r[i] == 0 && c[j] == 0;
            case 'o' :
                if (s[ij] == '.')
                    return r[i] == 0 && c[j] == 0 && d1[id1] == 0 && d2[id2] == 0;
                if (s[ij] == '+')
                    return r[i] == 0 && c[j] == 0;
                if (s[ij] == 'x')
                    return d1[id1] == 0 && d2[id2] == 0;
                return false;
            default:
                throw 3;
        }
    }

    void print() const {
        for (int i = 0; i < n; ++i) {
            std::cerr << s.substr(i * n, n) << std::endl;
        }
        std::cerr << "score = " << score << std::endl << std::endl;
    }

    void diff(std::ostream &out, Board const & b) const {
        int m = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (s[i * n + j] != b.s[i * n + j])
                    m++;
            }
        }
        out << score << " " << m;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (s[i * n + j] != b.s[i * n + j])
                    out << std::endl << s[i * n + j] << " " << (i + 1) << " " << (j + 1);
            }
        }
    }
};

class Solver : public SolverBase {
    int m_;
    int n_;
    Board b_;
public:
    virtual void read(std::istream &in);
protected:
    virtual void saw(std::ostream &out);
private:
};


void Solver::read(std::istream &in) {
    in >> n_ >> m_;
    b_.n = n_;
    for (int k = 0; k < n_ * n_; ++k) {
        b_.s.append(".");
    }
    b_.r.resize(n_);
    b_.c.resize(n_);
    b_.d1.resize(n_ * 2 - 1);
    b_.d2.resize(n_ * 2 - 1);
    for (int j = 0; j < m_; ++j) {
        char m;
        int r;
        int c;
        in >> m >> r >> c;
        r--;
        c--;
        b_.s[r * n_ + c] = m;
        if (m == 'o' || m == 'x') {
            b_.r[r]++;
            b_.c[c]++;
            b_.score++;
        }
        if (m == 'o' || m == '+') {
            int id1 = r + c;
            int id2 = r - c + n_ - 1;
            b_.d1[id1]++;
            b_.d2[id2]++;
            b_.score++;
        }
    }
}

#if 1

static std::pair<int, int> unpackRim(int rloc, int n) {
    int m = n - 1;
    if (rloc < m)
        return mp(0, rloc);
    if (rloc < 2 * m)
        return mp(rloc - m, m);
    if (rloc < 3 * m)
        return mp(m, rloc - 2 * m);
    return mp(rloc - 3 * m, 0);
}

static Board greedyFill(Board const & bs) {
    Board b = bs;
    // max + on rim, greedy
    // max x, greedy
    // greedy o upgrades
    int i1, j1;
    for (int rloc1 = 0; rloc1 < 4 * b.n - 4; rloc1++) {
        std::tie(i1, j1) = unpackRim(rloc1, b.n);
        if (b.canUpdate(i1, j1, '+')) {
            b.update(i1, j1, '+');
        }
    }
    for (int i = 0; i < b.n; i++) {
        for (int j = 0; j < b.n; j++) {
            if (b.canUpdate(i, j, 'x')) {
                b.update(i, j, 'x');
                break;
            }
        }
    }
    for (int i = 0; i < b.n; i++) {
        for (int j = 0; j < b.n; j++) {
            if (b.canUpdate(i, j, 'o')) {
                b.update(i, j, 'o');
                break;
            }
        }
    }
    return b;
}

void Solver::saw(std::ostream &out) {
    // for each possible location of two o's on the rim, try a greedy fill
    Board best = greedyFill(b_);
#if 0
    int i1, i2, j1, j2;
    Board b;
    int n1 = n_ - 1;
    for (int rloc1 = 0; rloc1 < 4 * n1; rloc1++) {
        std::tie(i1, j1) = unpackRim(rloc1, n_);
        if (b_.canUpdate(i1, j1, 'o')) {
            Board b1 = b_.add(i1, j1, 'o');
            for (int rloc2 = (rloc1 + n1) / n1 * n1; rloc2 < 4 * n1; rloc2++) {
                std::tie(i2, j2) = unpackRim(rloc2, n_);
                if (b1.canUpdate(i2, j2, 'o')) {
                    Board b2 = b1.add(i2, j2, 'o');
                    b = greedyFill(b2);
                    if (b.score > best.score) {
//                        b.print();
                        best = b;
                    }
                }
            }
            b = greedyFill(b1);
            if (b.score > best.score) {
                best = b;
            }
        }
    }
    // 0-2 o on rim
#endif
//    best.print();
    best.diff(out, b_);
}
#else

void Solver::saw(std::ostream &out) {
    std::vector<Board> prev;
    prev.push_back(b_);
    for (int ij = 0; ij < n_ * n_; ++ij) {
        int i = ij / n_;
        int j = ij % n_;
        int id1 = i + j;
        int id2 = i - j + n_ - 1;
        std::vector<Board> next = prev;
        for (auto const & b : prev) {
//            b.print();
            if (b.s[ij] == '.') {
                if (b.r[i] == 0 && b.c[j] == 0) {
                    next.push_back(b.add(i, j, 'x'));
                }
                if (b.d1[id1] == 0 && b.d2[id2] == 0) {
                    next.push_back(b.add(i, j, '+'));
                }
                if (b.r[i] == 0 && b.c[j] == 0 && b.d1[id1] == 0 && b.d2[id2] == 0) {
                    next.push_back(b.add(i, j, 'o'));
                }
            }
            else if (b.s[ij] == '+') {
                if (b.r[i] == 0 && b.c[j] == 0) {
                    next.push_back(b.add(i, j, 'o'));
                }
            }
            else if (b.s[ij] == 'x') {
                if (b.d1[id1] == 0 && b.d2[id2] == 0) {
                    next.push_back(b.add(i, j, 'o'));
                }
            }
        }
        prev = next;
    }
    Board best = b_;
    for (auto const & b : prev) {
        if (b.score > best.score) {
            best = b;
        }
    }
    std::cerr << n_ << " " << prev.size() << std::endl << std::endl;
    best.print();
    best.diff(out, b_);
}
#endif

int main() {
    freopen("D.in.txt","r",stdin);
    freopen("D.out.txt","w",stdout);
    auto t00 = std::chrono::system_clock::now();

    int nTestCases;
    cin >> nTestCases;

    // number of processors
    const int nThreads = min(max(int(thread::hardware_concurrency()), 1), nTestCases);

    if (nThreads <= 1) {
        // sequential processing: less memory and useful for debugging
        for (int it = 0; it < nTestCases; ++it) {
            auto t0 = now();
            Solver s;
            s.read(cin);
            s.solve();
            cout << "Case #" << (it + 1) << ": " << s.str() << endl;
            double t = since(t0);
            if (t > 0.01)
                fprintf(stderr, "%3d = %.2f | %.2f\n", it + 1, t,
                        since(t00) / (it + 1) * nTestCases);
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

