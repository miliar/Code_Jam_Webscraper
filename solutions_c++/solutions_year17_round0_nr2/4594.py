#include <bits/stdc++.h>

#define F first
#define S second
#define pb push_back
#define INF (1 << 30)
#define SQR(a) ((a) * (a))

using namespace std;

const int N = 1111;

//bool check(int x) {
//    string s = to_string(x);
//    for (size_t i = 1; i < s.size(); i++) {
//        if (s[i] < s[i - 1])
//            return false;
//    }
//    return true;
//}

//string naive(string s) 
//{
//    int x;
//    sscanf(s.c_str(), "%d", &x);
//    while (!check(x)) {
//        x--;
//    }
//    return to_string(x);
//}

void solve()
{
    string s;
    cin >> s;

    for (size_t i = 1; i < s.size(); i++) {
        if (s[i] < s[i - 1]) {
            int j = i - 1;
            while (j >= 0 && s[j] == s[i - 1]) {
                j--;
            }
            if (j < 0) {
                if (s[0] == '1') {
                    // we must put all nines
                    s = string(s.size() - 1, '9');
                    break;
                }
            }
            j++;
            s[j]--;
            for (size_t k = j + 1; k < s.size(); k++)
                s[k] = '9';
            break;
        }
    }
    cout << s << endl;
}

int main()
{
    srand(time(NULL));

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
