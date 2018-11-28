#include <cstdio>
#include <cstring>
#include <ctime>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <iostream>
using namespace std;

const static int MAXT = 100;
const static int MAX = 19;

bool helper(const char *num, char prevLim, char *out)
{
    char curDigit = *num;

    for (char i = curDigit; i >= prevLim; --i) {
        bool tmp = helper(num + 1, i, out + 1);
        if (!tmp) {
            continue;
        }
        *out = i;
        return true;
    }
    return false;
}

void fill(string &num, int pos) {
    while (pos < num.size()) {
        num[pos++] = '9';
    }
}

const char *doCase(string &num)
{
    for (int i = 0; i != num.size() - 1; ++i) {
        if (num[i] > num[i+1]) {
            for (int j = i; j >= 0; --j) {
                if (j == 0 || num[j] > num[j-1]) {
                    num[j]--;
                    fill(num, j + 1);

                    auto ans = num.c_str();
                    if (*ans == '0') ans += 1;
                    return ans;
                }
            }
        }
    }
    return num.c_str();
}

int main()
{
#ifdef ACM_SUBMIT
    freopen("output.txt", "w", stdout);
#endif // ACM_SUBMIT
    freopen("input.txt", "r", stdin);

    int T;

    cin >> T;

    string num;
    for (int i = 0; i != T; ++i) {
        cin >> num;
        cout << "Case #" << i + 1 << ": " << doCase(num) << endl;
    }

#ifdef ACM_LOCAL
    printf("Used time: %lf\n", clock() / (double) CLOCKS_PER_SEC);
#endif // ACM_LOCAL
    return 0;
}
