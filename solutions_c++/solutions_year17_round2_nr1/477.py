#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

void docase() {
    int d,n,k,v;
    cin >> d >> n;
    long double maxi = 0;
    for(int i = 0; i<n; i++) {
        cin >> k >> v;
        long double finish = (long double)(d-k)/((long double) v);
        maxi = max(maxi,finish);
    }
    long double result = (long double)(d)/maxi;
    printf("%.6Lf\n", result);
}

int main() {
    int T;
    cin >> T;
    for(int i = 0 ; i<T; i++) {
        cout << "Case #" << i+1 << ": ";
        docase();
    }
}
