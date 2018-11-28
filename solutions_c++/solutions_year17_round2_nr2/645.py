#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#include <ctime>
#include <unordered_map>
using namespace std;

clock_t begin_time, end_time;
void printtime() {
    end_time = clock();
    double elapsed_secs = double(end_time - begin_time) / CLOCKS_PER_SEC;
    cerr << "\nTime elapsed: " << elapsed_secs << endl;
}

const string BAD = "x";

string old[3] = {"R","Y","B"};

map< vector<int>, string > used;

string just_solve(int r, int y, int b) {
    vector< pair<int, string> > a = { {r, "R"}, {y, "Y"}, {b, "B"}};
    sort(a.begin(), a.end());
    if(a[2].first > a[1].first + a[0].first) {
        return "IMPOSSIBLE";
    }
    string res = "";
    for(int i=0;i<a[1].first;i++) {
        res += a[2].second + a[1].second;
    }
    for(int i=a[1].first;i<a[2].first;i++)
        res += a[2].second;
    reverse(res.begin(), res.end());
    string f = "";
    for(int i=0;i<a[0].first;i++) {
        f += a[0].second + res[i];
    }
    for(int i=a[0].first;i<res.size();i++)
        f += res[i];
    return f;
}

void solve() {
    int n;
    cin >> n;
    vector<int> a(6);
    for(int i=0;i<6;i++) {
        cin >> a[i];
    }
    // 0 2 4
    // R Y B
    cout << just_solve(a[0], a[2], a[4]) << endl;
}

int main() {
    begin_time = clock();

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int tests;
    scanf("%d", &tests);
    for(int i=0;i<tests;i++) {
        printf("Case #%d: ", i + 1);
        solve();
    }

    printtime();
    return 0;
}