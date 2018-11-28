#include <cmath>
#include <cstdio>
#include <vector>
#include <set>
#include <list>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
    int T;
    cin>>T;
    for(int test_case = 0; test_case < T; test_case++) {
        int N;
        double D;
        cin>>D>>N;
        double slowest_time = 0;
        for(int i = 0; i < N; i++) {
            double K, S;
            cin>>K>>S;
            double horse_time = (D - K)/S;
            if(horse_time > slowest_time) {
                slowest_time = horse_time;
            }
        }
        cout<<"Case #"<<test_case+1<<": "<<setprecision(30)<<D/slowest_time<<"\n";
    }
    return 0;
}