#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
using namespace std;


int main() {
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T;
    ios_base::sync_with_stdio(false);
    cin >> T;
    for(int r=0;r<T;r++){
        long long n,k;
        cin >> n >> k;

        long long binar = 1;
        while(binar * 2 < k+1) binar *= 2;
        long long highnumcount = (n - binar + 1) - ((n - binar + 1) / binar) * binar;
        long long rest = k - binar + 1;
        long long stall = (n - (binar - 1)) / binar ;
        if(rest <= highnumcount) stall ++;
        
        
        if(stall % 2 == 0) cout << "Case #" << r+1 << ": " << stall/2 << " " << (stall - 1)/2 << endl;
        else cout << "Case #" << r+1 << ": " << stall/2 << " " << stall/2 << endl;
    }
    return 0;
}
