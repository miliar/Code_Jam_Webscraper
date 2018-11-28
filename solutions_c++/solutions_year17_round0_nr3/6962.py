#include <iostream>
#include <vector>
using namespace std;

int main () {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n, k;
        cin >> n >> k;
        vector<int> l;
        l.push_back(0);
        l.push_back(n + 1);
        for (int j = 0; j < k - 1; j++) {
            int m = 0;
            int index;
            for (int x = 0; x < l.size() - 1; x++) {
                if (m < l[x + 1] - l[x]) {
                    m = l[x + 1] - l[x];
                    index = x;
                }
            }
            l.insert(l.begin() + index + 1, (l[index + 1] + l[index]) / 2);
        }
        int M = 0, Index;
        for (int j = 0; j < l.size() - 1; j++) {
            if (M < l[j + 1] - l[j]) {
                M = l[j + 1] - l[j];
                Index = j;
            }
        }
        cout << "Case #" << i + 1 << ": " << max(l[Index + 1] - (l[Index + 1] + l[Index]) / 2 - 1, (l[Index + 1] + l[Index]) / 2 - l[Index] - 1) << " " << min(l[Index + 1] - (l[Index + 1] + l[Index]) / 2 - 1, (l[Index + 1] + l[Index]) / 2 - l[Index] - 1) << endl;
    }
}
