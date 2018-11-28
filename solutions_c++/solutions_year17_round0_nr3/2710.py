#include <bits/stdc++.h>

using namespace std;

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    cin.rdbuf(in.rdbuf());
    cout.rdbuf(out.rdbuf());
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": ";
        long long n, k;
        cin >> n >> k;
        --k;
        map<long long, long long> section;
        section[n] = 1;
        while (k) {
            long long length = section.rbegin()->first, right = length / 2, left = length - 1 - right;
            long long cnt = min(k, section.rbegin()->second);
            if(right == left)
                section[right] += 2*cnt;
            else {
                section[right] += cnt;
                section[left] += cnt;
            }
            if (section.rbegin()->second > cnt)
                section.rbegin()->second -= cnt;
            else
                section.erase(section.rbegin()->first);
            k -= cnt;
        }
        long long length = section.rbegin()->first, right = length / 2, left = length - 1 - right;
        cout << right << " " << left << endl;
    }
    return 0;
}