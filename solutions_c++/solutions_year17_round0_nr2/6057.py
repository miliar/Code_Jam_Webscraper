#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using P = pair<int, int>;
const ll MOD = 1000000007;


int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        string S;
        cin >> S;
        int n = S.size();
        vector<int> N(n);
        for(int i=0;i<n;i++){
            N[i] = S[i] - '0';
        }
        bool ok = (S.size() == 1);
        while(!ok){
            for(int i=1;i<n;i++){
                if(N[i] < N[i-1]){
                    N[i-1]--;
                    for(int j=i;j<n;j++){
                        N[j] = 9;
                    }
                    break;
                }
                if(i == n-1){
                    ok = true;
                }
            }
        }
        printf("Case #%d: ", t);
        for(int i=0;i<n;i++){
            if(N[i]!=0){
                cout << N[i];
            }
        }
        cout << endl;
    }
    return 0;
}