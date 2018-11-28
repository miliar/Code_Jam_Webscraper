#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main(){

    int t, k;
    freopen("A-large.in", "r", stdin);
    freopen("oneA.txt", "w", stdout);
    cin >> t;
    for(int z = 1; z <= t; ++z){

        string x;
        cin >> x >> k;
        int ans = 0;

        for(int i = 0; i <= x.length()-k; ++i){

            if(x[i] == '-'){
                ++ans;
                //cout << k;
                for(int j = 0; j < k; ++j){
                    x[i+j] = (x[i+j] == '-' ? '+' : '-');
                }
            }

        }


        int solved = 1;
        for(int i = 0;solved && i < x.length(); ++i){
            if(x[i] == '-')solved = 0;
        }

        if(solved)printf("Case #%d: %d\n", z, ans);
        else printf("Case #%d: IMPOSSIBLE\n", z);





    }


}

