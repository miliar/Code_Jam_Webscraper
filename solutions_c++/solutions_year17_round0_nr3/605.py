#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int t = 0;
    cin >> t;
    for(int i=1; i<=t; i++){
        long long n, k;
        cin >> n >> k;
        map<long long, long long> hist;
        hist[0]++;
        long long a, b;
        while(k>0){
            long long x = n-(*hist.begin()).first;
            long long c = hist[n-x];
            if(x%2==1){
                b = x/2;
                a = b;
            }else{
                b = x/2;
                a = b-1;
            }
            k -= c;
            if(a>0) hist[n-a] += c;
            if(b>0) hist[n-b] += c;
            hist.erase(n-x);
        }
        cout << "Case #" << i << ": " << b << " " << a << endl;
    }
    return 0;
}
