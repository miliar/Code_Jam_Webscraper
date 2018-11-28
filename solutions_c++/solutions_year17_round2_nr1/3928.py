#include <bits/stdc++.h>
using namespace std;
int main() {
    int testCase;
    cin >> testCase;
    for(int testCases = 0 ; testCases < testCase ; testCases++) {
        int kms, dis;
        cin >> dis >> kms;
        
        vector<double> tt(kms);
        
        for(int i=0;i < kms;i++) {
            int k, s;
            cin >> k >> s;
            
            tt[i] = (double)(dis - k) / s;
        }
        sort(tt.begin(),tt.end(), greater<__float128>());
        printf("Case #%d: %lf\n", testCases+1, (double)(dis/tt[0]));
    }
    
    
    return 0;
}
