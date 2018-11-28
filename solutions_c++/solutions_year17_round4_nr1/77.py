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
    int totcasnum;
    scanf("%d", &totcasnum);
    forn(casnum,0,totcasnum) {
        printf("Case #%d: ", casnum+1);
        int n,p;
        scanf("%d %d", &n, &p);
        vi cnt(p,0);
        forn(i,0,n) {
            int x;
            scanf("%d", &x);
            cnt[x%p]++;
        }
        int ans = cnt[0];
        cnt[0] = 0;
        if (p==2) {
            ans += cnt[1]/2;
            if (cnt[1] % 2 == 1) ans++;
        }
        else if(p==3) {
            int k = min(cnt[1],cnt[2]);
            ans += k;
            cnt[1]-=k;
            cnt[2]-=k;
            ans += cnt[1]/3;
            ans += cnt[2]/3;
            cnt[1] = cnt[1]%3;
            cnt[2] = cnt[2]%3;
            if(cnt[1]+cnt[2] > 0) ans++;
        }
        else if(p==4) {
            int k = min(cnt[1],cnt[3]);
            ans+=k;
            cnt[1]-=k;
            cnt[3]-=k;
            ans += cnt[2]/2;
            cnt[2] = cnt[2]%2;
            if(cnt[2] == 1) {
                if(cnt[1] > 1) {
                    ans++;
                    cnt[2]--;
                    cnt[1]-=2;
                }
                else if(cnt[3] > 1) {
                    ans++;
                    cnt[2]--;
                    cnt[3]-=2;
                }
            }
            ans+=cnt[1]/4;
            ans+=cnt[3]/4;
            cnt[1] = cnt[1]%4;
            cnt[3] = cnt[3]%4;
            if(cnt[1]+cnt[2]+cnt[3]>0) ans++;
        }
        printf("%d\n", ans);
//        printf("\n");
    }
    
    
}


