#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

double ep = 1e-9;

int main() {
    int T;  cin>>T;
    for (int t = 1; t <= T; ++t) {
        int N, K;   cin>>N>>K;
        double U;   cin>>U;
        double ar[N];
        double sum = U;
        double minP = 1.0;
        double maxP = 0.0;
        for (int i = 0; i < N; ++i) {
            cin>>ar[i];
            minP = min(minP, ar[i]);
            maxP = max(maxP, ar[i]);
            sum += ar[i];
        }
        
        //cout<<sum<<endl;
        double prod = 1;
        sort(ar, ar+N);
        for (int i = N-1; i >= 0; --i) {
            if (ar[i] > sum / N) {
                prod *= ar[i];
                sum -= ar[i];
                N--;
            } else 
                break;
        }
        for (int i = 0; i < N; ++i)
            prod *= sum / N;
        
        printf("Case #%d: %lf\n", t, prod);
    }
    
    return 0;
}
