/*************************************************************************
	> File Name: Round1B_A.cpp
	> Author: BMan
	> Mail: luo-kai-jia@163.com
	> Created Time: Sun 23 Apr 2017 12:08:00 AM CST
 ************************************************************************/

#include <bits/stdc++.h>
using namespace std;


const int maxn = 20000;
double k[maxn];
double s[maxn];
double D;
int N;

int main() {
    int _T;
    cin >> _T;
    for (int _t = 1; _t <= _T; _t++) {
        cin >> D >> N;
        for ( int i = 0; i < N; i++ ) {
            cin >> k[i] >> s[i];
        }
        
        double t = 0;
        for (int i = 0; i < N; i++) {
            t = max(t, (D - k[i]) / s[i]);
        }

        printf("Case #%d: %.6f\n", _t, D / t);

    }
    return 0 ;
}
