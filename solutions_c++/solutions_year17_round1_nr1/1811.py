#include <bits/stdc++.h>
#define ll long long 
using namespace std;

int main() {
    int t, r, c, i, j;
    
    cin >> t;
    for(int z=1;z<=t;z++) {
        cin >> r >> c;
        char a[r][c];
        for(i=0;i<r;i++) 
            for(j=0;j<c;j++) 
                cin >> a[i][j];
        bool col[c];
        for(i=0;i<c;i++)
            col[i] = false;
        bool flag;
        int idx, firstCol = -1;
        for(j=0;j<c;j++) {
            flag = false;
            for(i=0;i<r;i++) {
                if(a[i][j] != '?') {
                    flag = true;
                    idx = i;
                    break;
                }
            }
            if(flag) {
                if(firstCol == -1)
                    firstCol = j;
                col[j] = true;
                for(i=0;i<idx;i++)
                    a[i][j] = a[idx][j];
                for(i=idx+1;i<r;i++) {
                    if(a[i][j] == '?')
                        a[i][j] = a[idx][j];
                    else
                        idx = i;
                }
            }
        }
        idx = firstCol;
        for(j=0;j<c;j++) {
            if(col[j]) {
                idx = j;
                continue;
            }
            for(i=0;i<r;i++) {
                a[i][j] = a[i][idx];
            }
        }
        cout << "Case #" << z << ":" << endl;
        for(i=0;i<r;i++) {
            for(j=0;j<c;j++)
                cout << a[i][j];
            cout << endl;
        }
    }
    return 0;
}