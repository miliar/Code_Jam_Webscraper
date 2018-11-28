#include<bits/stdc++.h>

using namespace std;

const int maxN = 1005;
int K[maxN], S[maxN];

double work(){
    int d, n;
    cin >> d >> n;
    double t = 0.0;
    for(int i = 0; i < n; i++){
        double k, s; 
        cin >> k >> s;
        t = max(t, (d-k)/s);
    }
    return d/t;
}

int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        printf("Case #%d: %.7lf\n", i, work());
    }
    return 0;
}
