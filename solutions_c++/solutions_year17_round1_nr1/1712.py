#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb push_back
#define mp make_pair

string arr[26];
int row, col;
bool flag = false;
vector<int> v;

void solve(int i) {
    int j = 0;
    while (arr[i][j] == '?' && j < col) j++;
    if (j == col) {
        if (flag) {
            for (int k=0; k<col; k++) {
                arr[i][k] = arr[i-1][k];
            }
        } else v.pb(i);
    } else {
        for (int k=0; k<j; k++) arr[i][k] = arr[i][j];
        char last = arr[i][j];
        for (int k=j; k<col; k++) {
            if (arr[i][k] =='?') arr[i][k] = last;
            last = arr[i][k];
        }
        if (!flag) {
            for (int o=0; o<(int)v.size(); o++) {
                int l = v[o];
                for (int k=0; k<col; k++) arr[l][k] = arr[i][k];
            }

        } flag = true;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for (int r=0; r<T; r++) {
        flag = false;
        v.clear();
        cin >> row >> col;
        for (int i=0; i<row; i++) {
            cin >> arr[i];
            solve(i);
        }
        cout << "Case #" << r+1 << ": " << '\n';
        for (int i=0; i<row; i++) cout << arr[i] << '\n';
    }
    return 0;
}


/*
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb push_back
#define mp make_pair

int main()
{
    ios::sync_with_stdio(0);
    freopen("1.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for (int r=0; r<T; r++) {
        int  ans = 0;

        cout << "Case #" << r+1 << ": " << ans << '\n';
    }
    return 0;
}

*/
