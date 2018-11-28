#include <bits/stdc++.h>
using namespace std;
void cal(int Case) {

    long long in, tmp;
    int num[30] = {0};
    cin >> in;
    int n = 0;
    tmp = in;
    while (tmp > 0) {
        tmp /= 10;
        n++;
    }
    for (int i = n; i > 0; i--) {
        num[i] = in%10;
        in /= 10;
    }

    for (int i = 2; i <= n; i++) {
        if (num[i] < num[i-1]) {
            for (int j = i; j > 0; j--) {
                if (num[j] >= num[j-1]) break;
                if (num[j-1] == 0) {
                    num[j] = 0;
                    break;
                }
                num[j] = 9;
                num[j-1]--;
            }
            for (int j = i+1; j <= n; j++) {
                num[j] = 9;
            }
        }
    }
    cout << "Case #" << (Case) <<": ";
    int i = 1;
    while(num[i] == 0) i++;
    for ( ; i <= n; i++) {
        cout << num[i];
    }
    cout << "\n";
}
int main(){
    int t;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    cin >> t;
    for (int i = 0; i < t; i++) {
        cal(i+1);
    }
}
