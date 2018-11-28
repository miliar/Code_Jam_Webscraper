#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define fore(i, b, e) for (int i = (int)(b); i <= (int)(e); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define pb push_back
#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;
typedef long long ll;
#define CLR(x) memset(x, 0, sizeof x)
#define cout _mycout_

#define PROD 1

struct Solver {
    int caseno;
    ostream& cout;

    Solver(int caseno, ostream& cout) : caseno(caseno), cout(cout) {}

    int n, p;
    vi r;
    vector<vi> q;
    vi it;

    void read() {
        cin >> n >> p;
        r.resize(n);
        forn(i, n) cin >> r[i];
        q.resize(n);
        forn(i, n) {
            q[i].resize(p);
            forn(j, p) cin >> q[i][j];
        }
    }

    void solve() {
        forn(i, n) {
            it.pb(0);
            sort(all(q[i]));
        }
        int res = 0;

        int cur = 1;
        while (true) {
            bool ok = true;
            bool done = false;
            forn(i, n) {
                if (it[i] == p) {
                    done = true;
                    break;
                }
                i64 need = cur * r[i];
                i64 have = q[i][it[i]];
                if (have * 10 < need * 9) {
                    ++it[i];
                    ok = false;
                    break;
                }
                if (have * 10 > need * 11) {
                    ++cur;
                    ok = false;
                    break;
                }
            }
            if (done) break;
            if (!ok) continue;
            ++res;
            forn(i, n) ++it[i];
        }

        cout << "Case #" << caseno+1 << ": " << res << endl;
    }
};

#undef cout

struct ThreadPool {
    int threadNo;
    int taskNo;
    int nextTask;
    int maxTime;
    std::vector<std::string> output;

    std::mutex mutex;
    std::chrono::time_point<std::chrono::steady_clock> start;

    static constexpr const char* GREEN = "\033[32;3m";
    static constexpr const char* YELLOW = "\033[33;3m";
    static constexpr const char* NONE = "\033[0;m";

    ThreadPool(int threadNo, int taskNo, int maxTime) :
            threadNo(threadNo),
            taskNo(taskNo),
            nextTask(0),
            maxTime(maxTime),
            output(taskNo)
    {
    }

    int duration() {
        return (std::chrono::steady_clock::now() - start).count() / 1000000;
    }

    void payload(int id) {
        while (true) {
            int start = duration();

            mutex.lock();

            if (nextTask >= taskNo) {
                mutex.unlock();
                return;
            }
            int taskId = nextTask++;
            std::ostringstream stream;
            Solver *s = new Solver(taskId, stream);
            s->read();

            std::cerr << YELLOW << "Running task " <<
                taskId+1 << "/" << taskNo <<
                " on thread " << id << NONE << std::endl;

            mutex.unlock();

            s->solve();
            delete s;
            output[taskId] = stream.str();

            mutex.lock();
            int dur = duration();
            std::cerr << GREEN <<  "Task " << taskId+1 << ": " <<
                dur - start << " ms, overall " <<
                dur/1000 << "." << std::setw(3) << std::setfill('0') <<
                dur%1000 << "/" << maxTime << " s" <<
                NONE << std::endl;
            std::cerr << stream.str();
            mutex.unlock();
        }
    }

    void run() {
        start = std::chrono::steady_clock::now();

        std::vector<std::thread> threads;
        for (int i = 0; i < threadNo; ++i) {
            threads.emplace_back([this, i]() { payload(i); });
        }
        for (auto& t: threads) {
            t.join();
        }

        int dur = duration();
        std::cerr << GREEN << "Run " << taskNo << " tasks in " <<
                dur/1000 << "." << std::setw(3) << std::setfill('0') <<
                dur%1000 << " seconds" <<
                NONE << std::endl;
        std::cerr << std::endl;

        for (const auto& s: output) {
            std::cout << s;
        }
    }
};

int main() {
#ifdef LOCAL
#if !PROD
    freopen("b.in", "r", stdin);
#endif
#endif

    const int THREADS = thread::hardware_concurrency();
    const int TIME = 60 * 6;
    (void)(THREADS + TIME);

    int n;
    cin >> n;
    string tmp;
    getline(cin, tmp);

#if PROD
    ThreadPool tp(THREADS, n, TIME);
    tp.run();
#else
    forn(i, n) {
        Solver s(i, cout);
        s.read();
        s.solve();
    }
#endif

#ifdef LOCAL
#if !PROD
    cerr << "Time elapsed: " << clock() / 1000 << " ms" << endl;
#endif
#endif
    return 0;
}
