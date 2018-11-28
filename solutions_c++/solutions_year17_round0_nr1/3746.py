#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long LL;
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)

int ft[1010];

void put(int p) {
    for (;p>=1; p-=p&-p) {
        ft[p] += 1;
    }
}

int get(int p) {
    int y = 0;
    for (;p<=1001; p+=p&-p) {
        y += ft[p];
    }
    return y;
}

int solve(string s, int k) {

    int res = 0;
    for (int i=0; i<(int)s.length()-k+1; i++) {
        if (s[i]=='-') {
            for (int j=0; j<k; j++) {
                s[i+j] = s[i+j]=='-'?'+':'-';
            }
            res++;
        }
    }

    //cout<<s<<endl;

    bool good = true;
    for (int i=s.length()-k+1; i<s.length(); i++) {
        if (s[i]!='+') {
            good = false;
        }
    }

    return good?res:-1;

}

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;
    for (int cas=1; cas<=t; cas++) {

        string s;
        int k;
        cin>>s>>k;

        int base = solve(s, k);

        for (int i=0; i<1010; i++) ft[i] = 0;

        int res = 0;
        for (int i=0; i<(int)s.length()-k+1; i++) {
            int sum = get(i+1);

            //cout<<i<<" "<<sum<<endl;

            if (sum%2==0 && s[i]=='-') {
                s[i] = '+';
                put(i+k);
                res++;
            }
            else if (sum%2!=0 && s[i]=='+') {
                put(i+k);
                res++;
            }
        }

        bool good = true;
        for (int i=(int)s.length()-k+1; i<s.length(); i++) {

           int sum = get(i+1);

           //cout<<i<<" "<<sum<<endl;

            if (sum%2==0 && s[i]=='-') {
                good = false;
            }
            else if (sum%2!=0 && s[i]=='+') {
                good = false;
            }

        }

        if (good) {
            printf("Case #%d: %d\n", cas, res);
            if (res != base) {
                cout<<"ERROR: "<<res<<" "<<base<<endl;
            }
        }
        else {
            printf("Case #%d: IMPOSSIBLE\n", cas);
            if (-1 != base) {
                cout<<"ERROR"<<endl;
            }
        }
    }

    return 0;

}
