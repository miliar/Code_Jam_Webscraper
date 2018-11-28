#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

const int max_n = 1005;

long long dist, N, k, s;
double tmp, inp_caled[max_n];
double ans;

int main(void){
    int kase;
    cin >> kase;
    for(int cs = 1; cs <= kase; cs++){
        for(int i = 0; i < max_n; i++) inp_caled[i] = 0;
        cin >> dist >> N;
        for(int i = 0; i < N; i++){
            cin >> k >> s;
            inp_caled[i] = (double)(dist - k) /((double) s);
        }
        tmp = -999999.999;
        for(int i = 0; i < N; i++) tmp = max(tmp, inp_caled[i]);
        ans = dist / tmp;
        printf("Case #%d: %.6f\n", cs, ans);
    }
    return 0;
}
