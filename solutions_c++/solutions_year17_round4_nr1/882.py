#include<bits/stdc++.h>
using namespace std;


#define li          long long int
#define rep(i,to)   for(li i=0;i<((li)(to));i++)
#define repp(i,start,to)    for(li i=(li)(start);i<((li)(to));i++)
#define pb          push_back
#define sz(v)       ((li)(v).size())
#define bgn(v)      ((v).begin())
#define eend(v)     ((v).end())
#define allof(v)    (v).begin(), (v).end()
#define dodp(v,n)       memset(v,(li)n,sizeof(v))
#define bit(n)      (1ll<<(li)(n))
#define mp(a,b)     make_pair(a,b)
#define rin rep(i,n)
#define EPS 1e-12
#define ETOL 1e-8
#define MOD 1000000007
typedef pair<li, li> PI;

#define INF bit(60)

#define DBGP 1


#define idp if(DBGP)
#define F first
#define S second
#define p2(a,b)     idp cout<<a<<"\t"<<b<<endl
#define p3(a,b,c)       idp cout<<a<<"\t"<<b<<"\t"<<c<<endl
#define p4(a,b,c,d)     idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<endl
#define p5(a,b,c,d,e)       idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<endl
#define p6(a,b,c,d,e,f)     idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<"\t"<<f<<endl
#define p7(a,b,c,d,e,f,g)       idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<"\t"<<f<<"\t"<<g<<endl
#define p8(a,b,c,d,e,f,g,h)     idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<"\t"<<f<<"\t"<<g<<"\t"<<h<<endl
#define p9(a,b,c,d,e,f,g,h,i)       idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<"\t"<<f<<"\t"<<g<<"\t"<<h<<"\t"<<i<<endl
#define p10(a,b,c,d,e,f,g,h,i,j)        idp cout<<a<<"\t"<<b<<"\t"<<c<<"\t"<<d<<"\t"<<e<<"\t"<<f<<"\t"<<g<<"\t"<<h<<"\t"<<i<<"\t"<<j<<endl
#define foreach(it,v)   for(__typeof((v).begin()) it=(v).begin(); it!=(v).end(); ++it)
#define p2p(x)      idp p2((x).F, (x).S)
#define dump(x,n)   idp{rep(i,n){cout<<x[i]<<" ";}puts("");}
#define dump2(x,n)  idp{rep(i,n){cout<<"["<<x[i].F<<" , "<<x[i].S<<"] ";}puts("");}
#define dumpi(x)    idp{foreach(it, x){cout<<(*it)<<" ";}puts("");}
#define dumpi2(x)   idp{foreach(it, x){cout<<"["<<(it)->F<<" , "<<(it)->S<<"] ";}puts("");}

#define read2d(a,w,h)   rep(i,h)rep(j,w)cin>>a[i][j]
#define dump2d(a,w,h)   rep(i,h){rep(j,w)cout<<a[i][j]<<" ";puts("");}

#define M_PI 3.1415926535897932384626

typedef pair<li, li> PI;

li g[111];

inline void solve() {
    li n, p;
    cin >> n >> p;
    rin{cin >> g[i];}

    li res = 0;
    if (p == 2) {
        li kisu = 0;
        rin{
            if (g[i] % 2 == 0) {
                ++res;
            } else {
                ++kisu;
            }
        }
        res += (kisu + 1) / 2;
    } else if (p == 3) {
        li nums[3] = {0};
        rin{
            ++nums[g[i] % 3];
        }
        res += nums[0];
        res += min(nums[1], nums[2]);
        li rest = abs(nums[1] - nums[2]);
        res += (rest + 2) / 3;
    } else {
        // p == 4
        li nums[4] = {0};
        li last[4] = {0};
        rin{
            ++nums[g[i] % 4];
        }
        res += nums[0];
        res += nums[2] / 2;
        last[2] = nums[2] % 2;
        li num13 = min(nums[1], nums[3]);
        res += num13;
        li rest = abs(nums[1] - nums[3]);
        if (last[2]) {
            if (rest > 2) {
                rest -= 2;
                last[2] = 0;
                ++res;
            }
        }
        res += rest / 4;
        if (last[2] > 0 || rest % 4 > 0) {
            ++res;
        }
    }
    cout << res << endl;
    return;
}

int main() {
    li t;
    cin >> t;
    rep(case_num, t) {
        cout << "Case #" << case_num + 1 << ": ";
        solve();
    }

    return 0;
}