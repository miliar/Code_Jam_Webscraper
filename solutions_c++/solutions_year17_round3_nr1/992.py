
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
using namespace std;
#define MOD 1000000007

 long double testcase() {
    int n, k;
    cin>>n>>k;
    vector<long long> r(n+1), h(n+1);
    vector<pair<long long, long long> > data;
    for (int i =1; i<=n; i++) {
        cin>>r[i]>>h[i];
        data.push_back(make_pair(r[i], h[i]));
    }
    sort(data.begin(), data.end());
    for (int i =1; i<=n; i++) {
        r[i] = data[i-1].first;
        h[i] = data[i-1].second;
    }

    vector<vector< long double > > best(n+1, vector< long double>(k+1));
     long double maximum = 0;
    
    for (int choose = 0; choose<=k; choose++) {
        best[0][choose] = 0;
    }
    for (int total =1; total<=n; total++) {
        for (int choose = 0; choose<=min(total,k); choose++) {
            if (choose == 0) {
                best[total][choose] = 0;
                continue;
            }

            long double first;
            if (total -1 < choose) {
                first = 0;
            } else {
                first = best[total-1][choose];
            }
            long double second = best[total-1][choose-1] + M_PI*2.0*((long double)r[total])*h[total];
            if (choose == k) {
                second += M_PI*(( long double)r[total])*r[total];
            }
            //cout<<first<<' '<<second<<endl;
            best[total][choose] = max(first, second);
            maximum = max(maximum, best[total][choose]);

        }
    }
    //printf("%0.8f\n", M_PI);
    //cout<<M_PI<<endl;
    return maximum;
    
}

int main() {
    //init();
    int t;
    cin>>t;
    for (int i = 1; i<=t; i++) {
        auto result = testcase();
        //cout<<"Case #"<<i<<": "<<result<<endl;
        printf("Case #%d: %0.8Lf\n", i, result);
    }
    return 0;
}

