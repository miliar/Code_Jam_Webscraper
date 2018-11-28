#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <ctype.h>
#include <deque>
#include <queue>
#include <cstring>
#include <set>
#include <list>
#include <map>
#include <random>
#include <unordered_map>
#include <stdio.h>

using namespace std;

typedef long long ll;
typedef std::vector<int> vi;
typedef std::vector<bool> vb;
typedef std::vector<string> vs;
typedef std::vector<double> vd;
typedef std::vector<long long> vll;
typedef std::vector<std::vector<int> > vvi;
typedef vector<vvi> vvvi;
typedef vector<vll> vvll;
typedef std::vector<std::pair<int, int> > vpi;
typedef vector<vpi> vvpi;
typedef std::pair<int, int> pi;
typedef std::pair<ll, ll> pll;
typedef std::vector<pll> vpll;

const long long mod = 1000000007;

#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()
#define forn(i, a, b) for(int i = a; i < b; i++)

#define pb push_back
#define mp make_pair

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    int affu;
    scanf("%d", &affu);
    const int INF = 1e9;
    forn(rruq, 0, affu) {
        printf("Case #%d: ", rruq+1);
        int hd,ad,hk,ak,B,D;
        scanf("%d %d %d %d %d %d", &hd, &ad, &hk, &ak, &B, &D);
//        if(ad >= hk) {
//            printf("1\n");
//            continue;
//        }
//        else if(hd <= ak) {
//            printf("IMPOSSIBLE\n");
//            continue;
//        }
        int ans = INF;
        forn(d,0,101) forn(u,0,101) {
            int st = 0;
            int pd = ad;
            int cd = hd;
            int ck = hk;
            int pk = ak;
            forn(i,0,d) {
                if(st>1000) break;
                int npk = max(pk-D,0);
                if(npk >= cd) {
                    st++;
                    i--;
                    cd = hd-pk;
                }
                else {
                    st++;
                    pk = npk;
                    cd -= npk;
                }
            }
            forn(i,0,u) {
                if(st>1000) break;
                if(pk >= cd) {
                    st++;
                    i--;
                    cd = hd-pk;
                }
                else {
                    st++;
                    pd += B;
                    cd -= pk;
                }
            }
            while(1) {
                if(st>1000) break;
                if(pd >= ck) {
                    st++;
                    break;
                }
                else if(pk>=cd) {
                    st++;
                    cd=hd-pk;
                }
                else {
                    st++;
                    ck-=pd;
                    cd-=pk;
                }
            }
            if(st>1000) continue;
            ans = min(ans,st);
        }
        if(ans == INF) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
        
    }
    
    
}


