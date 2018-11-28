#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    double d, n;
    double k, s;
    double max_time = 0;
    double distance;
    double hour;

    cin >> t;
    for(int i= 1; i <= t; i++){
        cin >> d >> n;

        for(int j = 0; j < n; j++){
            cin >> k >> s;
            if((d-k)/ s > max_time)
                max_time = (d-k) / s;

        }
        printf("Case #%d: %.6f\n", i, d / max_time);
        max_time = 0;
    }


    return 0;
}
