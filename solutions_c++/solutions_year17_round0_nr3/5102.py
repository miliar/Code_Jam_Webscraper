#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <set>

using namespace std;

vector<pair<int, pair<int, int>>> queue;
set<pair<int, pair<int, int>>> heap;

int getBest(int x, int y)
{
    return (x + y) / 2;
}

pair<int, pair<int, int>> make_tuple(int x, int y, int z) {
    return make_pair(x, make_pair(y, z));
}

int dist(int x, int y)
{
    return x > y ? x - y - 1 : y - x - 1;
}

bool evaluate(int p1, int l1, int r1, int p2, int l2, int r2)
{
    int dl1 = dist(p1, l1);
    int dr1 = dist(r1, l1);

    int dl2 = dist(p2, l2);
    int dr2 = dist(r2, p2);

    if (min(dl1, dr1) == min(dl2, dr2)) {
        return max(dl1, dr1) >= max(dl2, dr2);
    }

    return min(dl1, dr1) > min(dl2, dr2);
}

void solve()
{
    int N, K;
    cin >> N >> K;
    
    heap.clear();
    queue.clear();

    heap.insert(make_tuple(-N, 0, N + 1));

    for (int i = 0; i < K; i++) {        
        int d = -(*heap.begin()).first;
        int lpos = (*heap.begin()).second.first;
        int rpos = (*heap.begin()).second.second;

        heap.erase(heap.begin());

        int pos = getBest(lpos, rpos);
        queue.push_back(make_tuple(pos, lpos, rpos));
        
        int dl = dist(pos, lpos);
        int dr = dist(rpos, pos);

        heap.insert(make_tuple(-dl, lpos, pos));
        heap.insert(make_tuple(-dr, pos, rpos));
    }

    int dl = dist(queue[K - 1].first, queue[K - 1].second.first);
    int dr = dist(queue[K - 1].second.second, queue[K - 1].first); 
    cout << max(dl, dr) << " " << min(dl, dr) << endl;
}

int main()
{
    freopen("stalls3.in", "r", stdin);
    freopen("stalls.out", "w", stdout);

    int T;
    scanf("%d ", &T);
    for (int i = 0; i < T; i++) {
        cout << "CASE #" << i + 1 << ": ";
        solve();
        cerr << "CASE " << i << endl;
    }

    return 0;
}
