#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <climits>
using namespace std;

string solve(string S, int K){
    int ans = 0;
    int N = S.size();
    vector<int> A(N, 0);
    for(int i=0; i<N; i++)
        if(S[i]=='-') A[i] = 1;

    for(int i=0; i<=N-K; i++){
        if(A[i] % 2){
            ans++;
            for(int j=i; j<i+K; j++)
                A[j]++;
        }
    }
    for(int i=N-K; i<N; i++)
        if(A[i] % 2) return "IMPOSSIBLE";

    return to_string(ans);
}

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        string S;
        int K;
        cin >> S >> K;
        cout << "Case #" << i+1 << ": ";
        cout << solve(S, K) << endl;
    }

    return 0;
}
