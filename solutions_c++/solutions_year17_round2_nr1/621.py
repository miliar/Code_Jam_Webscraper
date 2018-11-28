#include <iostream>
#include <algorithm>
#include <iomanip> 

using namespace std;

int main(int argc, const char * argv[]) {
    freopen("/Users/vadimantiy/Developer/codejam17/task1/task1/input.txt", "r", stdin);
    freopen("/Users/vadimantiy/Developer/codejam17/task1/task1/output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int caseNumber;
    cin >> caseNumber;
    for (int casen = 0; casen < caseNumber; casen++) {
        cerr << casen << '\n';
        cout << "Case #" << casen + 1 << ": ";
        int d, n;
        cin >> d >> n;
        double tq = -1;
        while (n--) {
            int k, s;
            cin >> k >> s;
            tq = max(tq, double(d - k) / s);
        }
        cout << setprecision(10) << double(d)/tq << '\n';
    }
    return 0;
}
