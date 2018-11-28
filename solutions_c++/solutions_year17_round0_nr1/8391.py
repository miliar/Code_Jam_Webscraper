#include <iostream>
#include <string>
using namespace std;

const int N = 1001;

bool pk[N];
int solve(const string &s, const int k)
{
    int n = s.length();
    for (int i=0; i < n; ++i) {
        pk[i] = (s[i]=='+');
    }
    int res = 0;
    for (int i=0; i <= n-k; ++i) {
        if (pk[i] == false) {
            ++res;
            for (int j=0; j < k; ++j) {
                pk[i+j] = !pk[i+j];
            }
        }
    }
    for (int i=0; i < n; ++i) {
        if (pk[i] == false){
            res = -1;
        }
    }
    return res;
}

int main()
{
    int caseN;
    cin >> caseN;
    for (int ci=0; ci < caseN; ++ci) {
        string s;
        int n;
        cin >> s >> n;
        int res = solve(s, n);
        cout << "Case #" << ci+1 << ": ";
        if (res == -1) cout << "IMPOSSIBLE";
        else cout << res;
        cout << endl;
    }
}
