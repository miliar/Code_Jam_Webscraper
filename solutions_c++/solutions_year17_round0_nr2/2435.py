#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

long long a, num[20], l;

int main() {
    int T;
    freopen("B-large.in", "rb", stdin);
    freopen("out.txt", "wb", stdout);
    cin>>T;
    l = 0;
    memset(num, 0, sizeof num);
    for (int cas = 1; cas <= T; ++ cas) {
        cout<<"Case #"<<cas<<": ";
        cin>>a;
        while (a) {
            num[l ++] = a % 10;
            a /= 10;
        }
        for (int i = 0; i < l - 1; ++ i) {
            bool res = true;
            for (int j = i + 1; j < l; ++ j) {
                if (num[j] > num[i]) {
                    res = false;
                    break;
                }
            }
            if (!res) {
                num[i] = 9;
                num[i + 1] --;
                for (int j = i - 1; j >= 0; -- j) num[j] = 9;
            }
            for (int j = i + 1; j < l - 1; ++ j) {
                if (num[j] < 0) {
                    num[j] = 9;
                    num[j + 1] --;
                }
            }

        }
        while (l) {
            -- l;
            if (num[l] <= 0) continue;
            cout<<num[l];
        }
        cout<<endl;
    }
    return 0;
}
