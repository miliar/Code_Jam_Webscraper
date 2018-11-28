#include <queue>
#include <algorithm>
#include <iostream>
#include <set>

using namespace std;

long long f(long long N, long long K)
{
    // after 2^i - 1 steps, divided into 2^i parts.
    // 2^i - 1 <= K - 1.
    int i = 0;
    while ((2LL<<i) <= K)
        i++;
    long long rem = N - (1LL<<i) + 1;
    long long ext = rem % (1LL << i);
    K -= 1LL<<i;K++;
    if (K <= ext)
        return (rem >> i) + 1;
    return rem >> i;
}

class Tree {
private:
    const int H = 21;
    vector<vector<int>> levels;
public:
    Tree()
    {
        levels.clear();
        for (int i = 0;i < H; i++)
            levels.push_back(vector<int>(1<<i, 0));
    }

    void insert(int v, int f = 1)
    {
        for (int d = H - 1;d >= 0;d--) {
            int pos = v >> (H - 1 - d);
            levels[d][pos] += f;
        }
    }

    int get_max() {
        int ret = 0;
        for (int d = 1;d < H; d++) {
            if (levels[d][2 * ret + 1] > 0) {
                ret = 2 * ret + 1;
            } else {
                ret = 2 * ret;
            }
        }
        return ret;
    }
};

int main(int argc, char **argv)
{
    int T;
    cin >> T;
    for (int t = 1;t <= T; t++) {
        long long N, K;
        cin >> N >> K;
        /*Tree tree;
        tree.insert(N);
        while (K > 1) {
            K--;
            int largest = tree.get_max();
            long long a = (largest - 1) / 2 , b = largest / 2;
            tree.insert(largest, -1);
            if (a >= 1)
                tree.insert(a, 1);
            if (b >= 1)
                tree.insert(b, 1);
        }
        int L = tree.get_max();
        int A = (L - 1) / 2, B = L / 2;*/
        long long X = f(N, K);
        cout << "Case #" << t << ": " << X / 2 << " " << (X - 1) / 2 << endl;
    }

    return 0;
}
