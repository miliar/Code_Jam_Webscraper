#include <bits/stdc++.h>

using namespace std;

int ans[22];

bool bt (int i, int v, bool  smaller, bool zerolead, string& x){
    if (i == x.size ()){
        return true;
    }
    int xi = x[i] - '0';
    int maxj = smaller ? 9 : xi;
    if (maxj < v){
        return false;
    }

    for (int j = maxj; j >= v; j--){
        ans[i] = j;
        if (!smaller && j > xi) continue;
        if (bt (i + 1, j, (j < xi) || smaller, j != 0 || zerolead,  x)){
            return true;
        }
    }
    return false;
}

int check (int n){
    int ans = 0;
    for (int i = 1; i <= n; i++){
        string tmp = to_string (i);
        bool fine = true;
        for (int j = 1; j < tmp.size (); j++){
            if (tmp[j] < tmp[j-1]){
                fine = false;
            }
        }
        if (fine)
            ans = i;
    }
    return ans;
}

int main(){
    freopen("a.inp", "r", stdin);
    freopen("a.out", "w", stdout);

    int T;
    cin >> T;
    long long n;

    for (int t = 1; t <= T; t++){
        cin >> n;
        memset (ans, 0, sizeof(ans));
        string tmp = to_string(n);
        bool found = bt (0,0,0, 1, tmp);
        int len = 0;
        long long llans = 0;
        for (int i = 0; i < 22; i++){
            if (i == 0){
                while (ans[i] == 0){
                    i++;
                }
            }
            if (ans[i] == 0){
                break;
            }
            len++;
            llans = llans * 10 + ans[i];
        }
        cout << "Case #" << t << ": ";
        if (len < tmp.size () || !found)
            for (int j = 0; j < tmp.size() - 1; j++)
                cout << 9;
        else cout << llans;
        cout << endl;
    }
}
