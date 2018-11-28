#include<bits/stdc++.h>

using namespace std;

const int N = 1e3 * 2;

int n,a[N],q,k,curr,ans,res,m;
string s;

main(){
    freopen("B-large.in","r",stdin);
    freopen("1.txt","w",stdout);

    cin >> q;

    for(int test = 1; test <= q; ++test){
        cin >> s;

        int n = s.size();

        for(int i = 1; i <= n; ++i){
            a[i] = s[i - 1] - '0';
        }

        while(true){
            bool ok = true;

            for(int i = n - 1; i >= 1; --i){
                if(a[i] > a[i + 1]){
                    a[i]--;

                    for(int j = i + 1; j <= n; ++j){
                        a[j] = 9;
                    }
                }
            }

            for(int i = n - 1; i >= 1; --i){
                if(a[i] > a[i + 1]) ok = false;
            }

            if(ok) break;
        }

        for(int i = n; i >= 1; --i) if(a[i]) k = i;

        cout << "Case #" << test << ": ";
        for(int i = k; i <= n; ++i) cout << a[i];
        cout << "\n";
    }
}
