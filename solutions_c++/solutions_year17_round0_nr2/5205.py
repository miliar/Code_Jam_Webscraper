#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <deque>

#define For(i,a,b) for(int i = a; i < b; i++)
#define rep(i,x) For(i,0,x)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define TWO(x) (1LL<<(x))

using namespace std;

int main() {
    int np; cin>>np;
    rep(i, np){
        int64_t num; cin>>num;
        int64_t num2 = num;
        deque<int> dig;
        while(num != 0) {
            dig.push_front(num % 10);
            num /= 10;
        }
        int n = dig.size();

        vector<int> big(n);
        big[n-1] = dig[n-1];
        for(int i=n-2;i>=0;i--) {
            if(dig[i] <= big[i+1]) {
                big[i] = dig[i];
            } else {
                big[i] = dig[i] - 1;
            }
        }

        deque<int> res_dig;
        bool broke = false;
        rep(i, n) {
            if(broke) {
                res_dig.push_back(9);
            } else {
                res_dig.push_back(big[i]);
                if(big[i] < dig[i]) {
                    broke = true;
                }
            }
        }

        int64_t res=0;
        for(int x : res_dig) {
            res *= 10;
            res += x;
        }

        //cout << res << " " << num2 << endl;
        assert(res <= num2);

        cout << "Case #"<<(i+1)<<": "<<res<<endl;
    }
}
