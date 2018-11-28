#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <queue> 
#define ll long long

using namespace std;

int main() {
    int t; scanf("%d",&t);
    for(int tc=1; tc<=t; tc++) {
        string ans = "";
        ll n,t; scanf("%lld",&n);
        while(1) {
            t = n;
            int b = 10;
            while(t) {
                int c = t%10;
                if(c > b) {
                    n--;
                    break;
                } else {
                    b = c;
                    if(c == 9) {
                        ans = to_string(c) + ans;
                        n /= 10;
                    }
                    t /= 10;
                }
            }
            if(!t) break;
        }
        //printf("Case #%d: %lld\n",tc,n);
        printf("Case #%d: ",tc);
        string pre = (!n)? "":to_string(n);
        cout << pre + ans << endl;
    }
}
