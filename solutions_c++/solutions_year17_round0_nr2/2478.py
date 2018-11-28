#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<map>
#include<vector>
#include<algorithm>
#define FOR(i,l,n) for(int i=l;i<n;i++)
using namespace std;
int main() {
    int t;
    char a[20];
    scanf("%d", &t);
    FOR(i, 0, t) {
        cin >> a;
        char eq = a[0];
        int eq_start=0;
        FOR(j, 0, strlen(a)-1) {
            if (a[j] > a[j+1]) {
                int change_start;
                if (a[j] <= eq) {
                    a[eq_start]--;
                    change_start = eq_start + 1;
                } else {
                    a[j]--;
                    change_start = j + 1;
                }
                FOR(k, change_start, strlen(a)) {
                    a[k]='9';
                }
                break;
            }
            if (a[j] != eq) {
                eq = a[j];
                eq_start = j;
            }
        }
        if (a[0] == '0')
            cout << "Case #"<< i+1 << ": " << a+1 << endl;
        else
            cout << "Case #"<< i+1 << ": " << a << endl;
    }
    return 0;
}
