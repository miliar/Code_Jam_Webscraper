#include<bits/stdc++.h>

using namespace std;

int main(){

    freopen("gcj_in.txt","r",stdin);
    freopen("gcj_out.txt","w",stdout);

    int t;
    cin >> t;
    for(int it=1;it<=t;it++) {
        int r,c,i,j,cnt=0,k;
        char a[30][30];
        cin >> r >> c;
        for(i=0;i<r;i++) {
            cin >> a[i];
        }
        for(i=0;i<r;i++) {
            for(j=0;j<c;j++) {
                if(a[i][j] == '?') {
                    continue;
                }
                else {
                    for(k=j-1;k>=0;k--) {
                        if(a[i][k] != '?') break;
                        a[i][k] = a[i][k + 1];
                    }
                    for(k=j+1;k<c;k++) {
                        if(a[i][k] != '?') break;
                        a[i][k] = a[i][k - 1];
                    }
                }
            }
        }
        while(1) {
            bool found = true;
            for(i=0;i<r;i++) {
                if(a[i][0] == '?') found = false;
            }
            if(found) break;
            for(i=0;i<r;i++) {
                if(a[i][0] != '?' && ((i - 1 >= 0 && a[i - 1][0] == '?') || (i + 1 < r && a[i + 1][0] == '?'))) break;
            }
          //  if(cnt == 0)break;
            for(j=0;j<c;j++) {
                if(i - 1 >= 0 && a[i - 1][j] == '?') a[i - 1][j] = a[i][j],cnt = cnt - 1;
            }
            //if(cnt == 0)break;
            for(j=0;j<c;j++) {
                if(i + 1 < r && a[i + 1][j] == '?') a[i + 1][j] = a[i][j],cnt = cnt - 1;
            }
            //if(cnt == 0)break;
        }
        cout << "Case #" << it << ":\n";
        for(i=0;i<r;i++) {
            for(j=0;j<c;j++) {
                cout << a[i][j];
            }
            cout << "\n";
        }
    }
    return 0;


}

