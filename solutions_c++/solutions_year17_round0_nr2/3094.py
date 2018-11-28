#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int t;


void solve(int test){
    printf("Case #%d: ", test);
    int ans[19];
    long long n; cin >> n;
    vector<int> number;
    while (n > 0){
        number.push_back(n % 10);
        n /= 10;
    }
    reverse(number.begin(), number.end());
    bool flag = false;
    for (int i = 0; i < number.size(); i++){
        for (int j = 9; j >= 0; j--){
            bool bad = false;
            bool sub_flag = false;
            for (int k = i; k < number.size(); k++){
                ans[k] = j;
                if (ans[k] > number[k] && !flag && !sub_flag)
                    bad = true;
                if (ans[k] < number[k])
                    sub_flag = true;
            }
            if (!bad)
                break;
        }
        if (ans[i] < number[i])
            flag = true;
    }
    for (int i = 0; i < number.size(); i++){
        if (ans[i] == 0)
            continue;
        cout << ans[i];
    }
    cout << endl;
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large-out.txt", "w", stdout);
    cin >> t;
    for (int i = 0; i < t; i++){
        solve(i + 1);
    }
    return 0;
}
