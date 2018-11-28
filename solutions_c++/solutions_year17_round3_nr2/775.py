#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

#define NMAX 1440

int A[NMAX];
int AC, AJ;
int F[NMAX];
int cnt[3];

int GetLeft(int i) {
    if (i == 0) {
        return NMAX - 1;
    }

    return i - 1;
}

int GetRight(int i) {
    if (i == NMAX - 1) {
        return 0;
    }

    return i + 1;
}

int cmp(pair<int, int> a, pair<int, int> b) {
    int l1 = a.second - a.first;
    int l2 = b.second - b.first;
    return l2 < l1;
}

void PrintDebug() {
    cout << endl;
    cout << cnt[1] << " " << cnt[2] << endl;
    for (int i = 0; i < NMAX; i++) {
        cout << A[i];
    }
    cout << endl;
}

void printSolution() {
    int sol = 0;
    for (int i = 0; i < NMAX; i++) {
        if (A[i] != A[GetLeft(i)]) {
            sol++;
        }
    }

    // PrintDebug();
    cout << sol << endl;
}

void solve() {
    cin >> AC >> AJ;

    for (int i = 0; i < NMAX; i++) {
        A[i] = 0;
        F[i] = 0;
    }

    cnt[0] = 0;
    cnt[1] = 0;
    cnt[2] = 0;
    for (int i = 0; i < AC; i++)
    {
        int x, y;
        cin >> x >> y;
        for (int j = x; j < y; j++) {
            F[j] = 2;
            A[j] = 2;
            cnt[2]++;
        }
    }

    for (int i = 0; i < AJ; i++)
    {
        int x, y;
        cin >> x >> y;
        for (int j = x; j < y; j++) {
            F[j] = 1;
            A[j] = 1;
            cnt[1]++;
        }
    }

    // PrintDebug();

    // occupy free space
    for (int i = 0; i < NMAX; i++) {
        int prev = GetLeft(i);
        if (A[i] == 0 && A[prev] != 0)
        {
            A[i] = A[prev];
            cnt[A[i]]++;
        }
    }

    for (int i = 0; i < NMAX; i++) {
        int prev = GetLeft(i);
        if (A[i] == 0 && A[prev] != 0)
        {
            A[i] = A[prev];
            cnt[A[i]]++;
        }
    }

    // PrintDebug();

    // Extend intervals
    while (cnt[1] != cnt[2]) {
        int toExtend = 1;
        if (cnt[1] > cnt[2]) {
            toExtend = 2;
        }

        bool found = false;
        for (int i = 0; i < NMAX; i++) {
            int prev = GetLeft(i), next = GetRight(i);
            if (A[i] != toExtend && (A[GetLeft(i)] == toExtend || A[GetRight(i)] == toExtend) 
                && (F[i] == 0))
            {
                A[i] = toExtend;
                cnt[toExtend]++;
                cnt[3 - toExtend]--;
                found = true;
                break;
            }
        }

        if (!found) {
            break;
        }
    }

    // PrintDebug();

    if (cnt[1] == cnt[2]) {
        printSolution();
        return;
    }

    // find free intervals
    int toExtend = 1;
    if (cnt[1] > cnt[2]) {
        toExtend = 2;
    }

    vector<pair<int, int>> intervals;
    pair<int, int> currentInterval;
    bool startedInterval = false;
    for (int i = 0; i < NMAX; i++) {
        if (A[i] != toExtend && F[i] == 0) {
            if (startedInterval) {
                currentInterval.second = i;
            } else {
                currentInterval = make_pair(i, i);
                startedInterval = true;
            }
        }

        if (F[i] != 0 && startedInterval)
        {
            intervals.push_back(currentInterval);
            startedInterval = false;
        }
    }

    if (startedInterval) {
        // unite first and last interval if needed
        pair<int, int> firstInterval = intervals[0];
        if (firstInterval.first == 0) {
            intervals.erase(intervals.begin());
            currentInterval.second = NMAX + firstInterval.second;
        } else {
            currentInterval.second = NMAX - 1;
        }

        intervals.push_back(currentInterval);
    }

    sort(intervals.begin(), intervals.end(), cmp);

    //for (int i = 0; i < intervals.size(); i++) {
    //    cout << intervals[i].first << " " << intervals[i].second << endl;
    //}

    for (int i = 0; i < intervals.size(); i++) {
        for (int j = intervals[i].first; j <= intervals[i].second; j++) {
            A[j % NMAX] = toExtend;
            cnt[toExtend]++;
            cnt[3 - toExtend]--;

            if (cnt[1] == cnt[2]) {
                break;
            }
        }

        if (cnt[1] == cnt[2]) {
            break;
        }
    }

    printSolution();
}

int main() {
    freopen("parenting.in", "r", stdin);
    freopen("parenting.out", "w", stdout);

    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}
