
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
using namespace std;
#define MOD 1000000007

double testcase() {
    int n,k;
    cin>>n>>k;
    double u;
    vector<pair<double, int> > p;
    cin>>u;
    for (int i =0; i<n; i++) {
        double x;
        cin>>x;
        p.push_back(make_pair(x, 1));
    }
    p.push_back(make_pair(1.0, 1));


    sort(p.begin(), p.end());
    int i = 0, firstElm = 0;
    while(1) {
        if (p[i].first * p[i].second + u <= p[i+1].first * p[i].second) {
            p[i].first += u/p[i].second;
            firstElm = i;
            // last turn and done
            break;
        }
        u -= (p[i+1].first - p[i].first) * p[i].second;
        p[i+1].second += p[i].second;
        firstElm = i+1;
        i++;
    }

    double prod = 1;
    for (int j = firstElm; j<p.size(); j++) {
        prod *= pow(p[j].first, p[j].second);
    }
    return prod;
}

int main() {
    //init();
    int t;
    cin>>t;
    for (int i = 1; i<=t; i++) {
        auto result = testcase();
        //cout<<"Case #"<<i<<": "<<result<<endl;
        printf("Case #%d: %0.8f\n", i, result);
    }
    return 0;
}

