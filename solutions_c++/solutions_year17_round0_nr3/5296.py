#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<ctime>
#include<cmath>

#include<algorithm>
#include<bitset>
#include<complex>
#include<deque>
#include<iostream>
#include<map>
#include<numeric>
#include<queue>
#include<stack>
#include<string>
#include<set>
#include<vector>
using namespace std;
struct inter{
    int sp, len;
    inter(){}
    inter(int a, int b){sp = a, len = b;}
    int FirstCon() const {
        return (len - 1) / 2;
    }
    int SecCon() const {
        return len /2;
    }
    int Position() {
        return sp + FirstCon();
    }
    bool operator<(const inter &now) const{
        if(FirstCon() != now.FirstCon()) return FirstCon() < now.FirstCon();
        if(SecCon() != now.SecCon()) return SecCon() < now.SecCon();
        return sp < now.sp;
    }
};

int main(int argc, const char *argv[])
{
    int tn;
    int ansA, ansB;
    int n, k;
    cin >> tn;
    for (int z = 1; z <= tn; z++) {
        cin >> n >> k;
        priority_queue<inter, vector<inter>, less<inter> > Q;
        Q.push(inter(0, n));
        while(k--){
            inter now = Q.top();
            Q.pop();
            ansA = now.FirstCon();
            ansB = now.SecCon();
            /* printf("now sp %d len %d ansA %d ansB %d\n", now.sp, now.len, ansA, ansB); */
            if(now.len != 1){
                if(now.len == 2) Q.push(inter(now.sp+1, 1));
                else{
                    int mid = now.Position();
                    Q.push(inter(now.sp, mid - now.sp));
                    Q.push(inter(mid+1, now.sp + now.len - mid -1));
                }
            }
        }
        printf("Case #%d: %d %d\n", z, ansB, ansA);
    }
    return 0;
}
