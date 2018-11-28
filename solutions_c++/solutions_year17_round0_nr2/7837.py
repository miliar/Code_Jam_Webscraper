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
    freopen("B-large.in", "r", stdin);
    freopen("out-large.txt", "w", stdout);

	int n, T, i, j;
    string s, ans;
	cin>>T;
	for(int t = 1; t <= T; t++){
		cin>>s;
        int len = s.length();
        ans = s;
        for(i = len - 2; i >= 0; i--) {
            if(ans[i] - '0' > ans[i + 1] - '0') {
                ans[i] = (ans[i] - 1);
                for(j = len - 1; j >= i + 1; j--) {
                    ans[j] = '9';
                }
            }
        }
//        cout<<ans<<endl;

        long ans_num;
        stringstream ss(ans);
        ss >> ans_num;
        cout<<"Case #"<<t<<": ";
        cout<<ans_num<<endl;
	}
}


