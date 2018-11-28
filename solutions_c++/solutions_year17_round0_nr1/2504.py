#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<map>
#include<vector>
#include<algorithm>
#define FOR(i,l,n) for(int i=l;i<n;i++)
using namespace std;
void flip(char *a, int start, int len) {
    FOR(i, start, start+len) {
        if (a[i] == '-')
            a[i] = '+';
        else
            a[i] = '-';
    }
}
int main() {
    int t;
    scanf("%d", &t);
    FOR(i, 0, t) {
        char a[1002];
        cin >> a;
        int k;
        int flip_count = 0;
        scanf("%d", &k);
        //cout << a << endl;
        FOR(j, 0 ,strlen(a) - k + 1) {
            if (a[j] == '-') {
                flip(a, j, k);
                flip_count++;
            }
            //cout << a << endl;
        }
        int impossible = 0;
        FOR(j, 0, strlen(a)) {
            if (a[j] == '-') {
                impossible = 1;
                break;
            }
        }
        if (impossible)
            cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << i+1 << ": " << flip_count << endl;
    }
    return 0;
}
