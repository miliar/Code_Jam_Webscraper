#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#define LL long long
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define sc(x) scanf("%d", &x)
#define scl(x) scanf("%lld", &x)
#define M 1000000007
#define MAXN 112345
using namespace std;

int main(){

    freopen("A-large.in", "r", stdin);
    freopen("out-large.txt", "w", stdout);
	int n, T, i, j, k;
    const char HAPPY = '+';
    const char BLANK = '-';
    string s;
	cin>>T;
	for(int t = 1; t <= T; t++){
        cin>>s>>k;
        int len = s.length();
        int ans = 0;
        for(i = 0; i < len - k + 1; i++) {
            if(s[i] == BLANK) {
                for(j = i; j <= i + k - 1; j++) {
                    if(s[j] == BLANK)
                        s[j] = HAPPY;
                    else
                        s[j] = BLANK;
                }
                ans++;
            }
        }

        for(i = 0; i < len; i++) {
            if(s[i] == BLANK) {
                ans = -1;
            }
        }
        cout<<"Case #"<<t<<": ";
        if(ans == -1)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<ans<<endl;
	}
}

