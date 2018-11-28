#include <bits/stdc++.h>
using namespace std;

void solve() {
    int N,M;
    cin >> N >> M;
    string inp[26],init[26];
    char ans[26][26];
    for (int i=0;i<N;++i) for (int j=0;j<M;++j) ans[i][j]='-';
    
    for (int i=0;i<N;++i) {
        cin >> inp[i];
        init[i] = inp[i];
    }
    for (int i=0;i<N;++i) {
        for (int j=0;j<M;++j){
            for (int k=N-1;k>=i;--k){
                for (int l=M-1;l>=j;--l){
                    if (inp[i][j]=='-') continue;
                    set<char> myset;
                    bool ok=1;
                    for (int m=i;m<=k;++m){
                        for (int n=j;n<=l;++n){
                            if (inp[m][n]=='?') continue;
                            myset.insert(inp[m][n]);
                        }
                    }
                    if (myset.size()>1 || myset.size()==0) ok=0;
                    if (ok) {
//                        cout << i << " " << j << " " << k << " " << l << endl;
                        for (int m=i;m<=k;++m)
                            for (int n=j;n<=l;++n) {
                                ans[m][n]=(*myset.begin());
                                inp[m][n]='-';
                            }
                            
//                        for (int m=0;m<N;++m){
//                            for (int n=0;n<M;++n) {
//                                cout << ans[m][n];
//                            }
//                            cout << endl;
//                        }
                            
                    }
                }
            }
        }
    }
    for (int i=0;i<N;++i){
        for (int j=0;j<M;++j) cout << ans[i][j];
        cout << endl;
    }
}

int main() {
    int ntest;
    scanf("%d",&ntest);
    for (int test=1;test<=ntest;++test){
        cout << "Case #" << test << ":" << endl;
        solve();
    }
    return 0;
}
