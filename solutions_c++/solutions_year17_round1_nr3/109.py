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

    i64 hd, ad, hk, ak, b, d;

    void read() {
        cin >> hd >> ad >> hk >> ak >> b >> d;
    }

    i64 getNeedMoves() {
        if (b == 0) return (hk - 1) / ad + 1;
        i64 best = 1e18;
        i64 nb;
        for (nb = 0; ; ++nb) {
            i64 turns = nb + ((hk - 1) / (ad + b*nb) + 1);
            best = min(best, turns);
            if (turns > best) break;
        }

        i64 prev = 0;
        forn(i, 5) {
            i64 turns = nb + ((hk - 1) / (ad + b*nb) + 1);
            assert(turns >= prev);
            prev = turns;
            ++nb;
        }

        return best;
    }

    i64 needMoves;
    /*
    need 5 moves, can do 2: +..+..+.
    (5 - 1) / 2 + 1 = 3
    need 4 moves, can do 2: +..+..
    (4 - 1) / 2 + 1 = 2;
    */

    i64 timeToKill(i64 curHp, i64 ak) {
        if (ak * (needMoves - 1) < curHp) {
            return needMoves;
        }

        i64 spareTime = (hd - 1) / ak - 1;
        if (spareTime <= 0) return 2e18;

        i64 need = needMoves - 1;
        need -= (curHp - 1) / ak;
        assert(need > 0);
        return needMoves + (need - 1) / spareTime + 1;
    }

    void solve() {
        cout << "Case #" << caseno+1 << ": ";

        if (ad >= hk) {
            cout << 1 << "\n";
            return;
        }

        if (ak - d >= hd) {
            cout << "IMPOSSIBLE\n";
            return;
        }

        needMoves = getNeedMoves();

        i64 ak = this->ak;
        i64 hp = hd;
        i64 res = 2e18;
        forn(i, 50000) {
            if (ak < 0) break;
            res = min(res, i + timeToKill(hp, ak));
            if (hp <= ak - d) {
                hp = hd;
            } else {
                ak = max(0ll, ak - d);
            }
            hp -= ak;
            assert(hp > 0);
        }

        if (res == 2e18) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << res << "\n";
        }
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
    freopen("c.in", "r", stdin);
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
