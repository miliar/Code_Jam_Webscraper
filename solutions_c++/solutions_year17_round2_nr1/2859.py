#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int main(){
    int ts;
    cin>>ts;
    for (int t = 1; t <= ts; t++) {
        double d, n;
        cin >> d >> n;
        double maxtime = 0;
        for (int i = 0; i < n; i++) {
            double s, k;
            cin >> s >> k;
            double temp = (d-s)/k;
            if (maxtime < temp)maxtime = temp;
        }
        double ans = d/maxtime;
        cout<<"Case #"<<t<<": ";
        printf("%.6lf\n", ans);
    }
}
