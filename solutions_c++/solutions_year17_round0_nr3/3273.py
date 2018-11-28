#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
#include <string>
using namespace std;
#define MAX 510

struct Result {
    long long min;
    long long max;
    Result(long long a, long long b){
        min = a;
        max = b;
    }
};

Result solve(long long N, long long K){
    long long t = log(K)/log(2);
    N = N - pow(2, t) + 1;
    long long minus=N % (long long)pow(2, t);
    long long m=N/pow(2, t);
    if(K<minus + (long long)pow(2, t))m++;
    long long min, max;
    if(m%2==1) {
        min = max = m/2;
    } else {
        max=m/2;
        min=max-1;
    }
    return Result(min, max);
}

int main() {
    //freopen("/Users/d/Documents/C-small-2-attempt0.in", "rt", stdin);
    //freopen("/Users/d/Documents/INPUT.TXT", "rt", stdin);
    int n;
    cin >> n;
    for(int i=1;i<=n;i++){
        long long N, K;
        cin >> N >> K;
        cout << "Case #" << i << ": ";
        Result r=solve(N, K);
        cout << r.max << " " << r.min << endl;
    }
    return 0;
}
