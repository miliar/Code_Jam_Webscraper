#include <iostream>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <utility>
using namespace std;

typedef long long ll;

double time(double x1, double s1, double x2, double s2) {
    if (s2 >= s1)
        return -1;
    return (x2-x1) / (s1 - s2);
}

int main() {
    int T;  cin>>T;
    for (int test = 1; test <= T; ++test) {
        double D;   cin>>D;
        int N;  cin>>N;
        vector<pair<double, double> > horses;
        for (int i = 0; i < N; ++i) {
            double X, S;    cin>>X>>S;
            horses.push_back({X, S});
        }
        sort(horses.begin(), horses.end());
        
        double t = 0;
        double cur = horses[0].first;
        double speed = horses[0].second;
        for (int i = 1; i < N; ++i) {
            double tt = time(cur, speed, horses[i].first, horses[i].second);
            double newpos = speed * tt;
            if (tt == -1)
                continue;
            if (cur + newpos > D)
                continue;
            t += tt;
            cur += newpos;
            speed = horses[i].second;
        }
        
        t += time(cur, speed, D, 0);
        //cout<<t<<" "<<cur<<" "<<speed<<endl;
        
        cout<<"Case #"<<test<<": "<<setprecision(9)<<fixed<<D/t<<"\n";
    }
    
    return 0;
}
