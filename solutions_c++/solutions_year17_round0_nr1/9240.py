#include <bits/stdc++.h>
 
using namespace std;
int T, K; string str;
bitset<1100> v;

int solve(bitset<1100> v, int size) {
    int ans = 0;
    for (int i = 0; i < size - K + 1; ++i) {
        if(!v[i]) {
            ans++;
            for (int j = i; j < i+K; ++j) 
                v[j] = !v[j];
        }
    }
    for (int i = size - K + 1; i < size; ++i) 
        if(v[i] == 0)
            return -1;

    return ans;    
}

int main() {
    cin >> T;
    for (int caseC = 0; caseC < T; ++caseC) {
        cin >> str >> K;
        v.reset();

        for (int i = 0; i < str.size(); ++i) 
            if(str[i] == '+')
                v[i] = 1;
        
        int res = solve(v, str.size() );
        if( res == -1 )
            printf("Case #%d: IMPOSSIBLE\n", caseC+1);
        else
            printf("Case #%d: %d\n", caseC+1, res);
    }
return 0;
}