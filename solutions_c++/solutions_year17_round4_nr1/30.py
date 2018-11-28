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

const int maxn = 105;

struct Solver {
    int caseno;
    ostream& cout;

    Solver(int caseno, ostream& cout) : caseno(caseno), cout(cout) {}

    int n, k;
    vi a;
    int d[maxn][maxn][maxn];
    int cnt[4];

    void read() {
        cin >> n >> k;
        a.resize(n);
        forn(i, n) cin >> a[i];
    }

    void relax(int &x, int y) { x = max(x, y); }

    void solve() {
        memset(d, 0, sizeof d);
        forn(i, 4) cnt[i] = 0;
        int s = 0, res = 0;
        forn(i, n) {
            a[i] %= k;
            if (a[i] == 0) ++res;
            else {
                s += a[i];
                ++cnt[a[i]];
            }
        }
        fore(i, 0, cnt[1]) fore(j, 0, cnt[2]) fore(l, 0, cnt[3]) {
            int s = i*1 + j*2 + k*3;
            if (i < cnt[1]) {
                int ss = s + 1;
                relax(d[i+1][j][l], d[i][j][l] + (ss%k == 0));
            }
            if (j < cnt[2]) {
                int ss = s + 2;
                relax(d[i][j+1][l], d[i][j][l] + (ss%k == 0));
            }
            if (l < cnt[3]) {
                int ss = s + 3;
                relax(d[i][j][l+1], d[i][j][l] + (ss%k == 0));
            }
        }
        res += d[cnt[1]][cnt[2]][cnt[3]];
        if (s%k != 0) ++res;
//         cerr << d[cnt[1]][cnt[2]][cnt[3]] << endl;
        cout << "Case #" << caseno+1 << ": ";
        cout << res << "\n";
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
    freopen("a.in", "r", stdin);
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
        Solver *s = new Solver(i, cout);
        s->read();
        s->solve();
    }
#endif

#ifdef LOCAL
#if !PROD
    cerr << "Time elapsed: " << clock() / 1000 << " ms" << endl;
#endif
#endif
    return 0;
}
