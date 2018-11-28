
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
using namespace std;
#define MOD 1000000007

class Mylong {
    public:
    long long val;
    Mylong() {
        val = 0;
    }

    Mylong(long long x) {
        val = x;
    }

};

pair<long long, long long> split(long long val) {
    val--;
    return make_pair((val+1)/2, val/2);
}

long long testcase() {
    long long n, k;
    cin>>n>>k;
    map<long long, Mylong> hash; // gap => freq
    hash[n].val = 1;
    while (k > 1) {
        auto it = hash.rbegin();
        k -= it->second.val;
        if (k < 1)
            break;
        auto newvals = split(it->first);
        hash[newvals.first].val += it->second.val;
        hash[newvals.second].val += it->second.val;
        hash.erase(it->first);
    }
    return hash.rbegin()->first;
}

int main() {
    //init();
    int t;
    cin>>t;
    for (int i = 1; i<=t; i++) {
        auto result = testcase();
        auto vals = split(result);
        cout<<"Case #"<<i<<": "<<vals.first<<" "<<vals.second<<endl;
    }
    return 0;
}

