/*
 *    
 */
#include <fstream>
#include <iostream>
#include <cstdlib>
#include <cmath> 
#include <algorithm>
#include <vector>
#include <list>
#include <cstring>
#include <stack>
#include <map>
#include <set>
#include <utility>
#include <queue>
#include <deque>
#include <ctime>
#include <complex>
#include <bitset>
#include <time.h>
#include <iomanip>
#include <cassert>

using namespace std;
#define PB push_back
#define LL long long
#define MP make_pair
#define fi first
#define se second
typedef unsigned long long ULL;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define DBG 0

#define fori(i,a,b) for(int i = (a); i < (b); i++)
#define forie(i,a,b) for(int i = (a); i <= (b); i++)
#define ford(i,a,b) for(int i = (a); i > (b); i--)
#define forde(i,a,b) for(int i = (a); i >= (b); i--)
#define forls(i,a,b,n) for(int i = (a); i != (b); i = n[i])
#define mset(a,v) memset(a, v, sizeof(a))
#define mcpy(a,b) memcpy(a, b, sizeof(a))

#define MIN_LD -2147483648
#define MAX_LD  2147483647
#define MIN_LLD -9223372036854775808
#define MAX_LLD  9223372036854775807
#define MAX_INF 18446744073709551615
const int INF = 0x7fffffff;
typedef set<int> Set;
#define ALL(x) x.begin(),x.end()
#define INS(x) inserter(x,x.begin())
//set_union(ALL(x1),ALL(x2),INS(x)),set_intersection


int N,P,T;
const int maxn = 60;
LL rr[maxn],s[maxn],q[maxn][maxn];

int main(void){
    
    //freopen("*.in", "r", stdin);
    //freopen("*.out", "w", stdout);
    cin.sync_with_stdio(false);
    cin >> T;
    forie(t,1,T){
        cout << "Case #" << t << ": ";
        cin >> N >> P;
        vector<pair<LL,LL> > v[N];
        fori(i,0,N) {
            cin >> rr[i];
            s[i] = rr[i];
            rr[i]*=10;
        }
        int M = 0;
        fori(i,0,N) {
            fori(j,0,P) {
                cin >> q[i][j];
                q[i][j]*=10;
                LL l = q[i][j]/(rr[i]+s[i]);
                if(1ll*(rr[i]+s[i])*l<q[i][j])l++;
                LL r = q[i][j]/(rr[i]-s[i]);
                if(l<=r) {
                    v[i].PB(MP(l,r));
                    M++;
                }
            }
            sort(v[i].begin(),v[i].end());
        }
        int ans = 0;
        while(M>0){
            LL l,r;int idx;
            int finish = 0;
            fori(i,0,N){
                if (v[i].size()==0){
                    finish = 1;
                    break;
                }
                if (i==0) {
                    l = v[i][0].fi;
                    idx = 0;
                }
                else{
                    if(v[i][0].fi>l){
                        idx = i;
                        l = v[i][0].fi;
                    }
                }
            }
            if(finish) break;
            r = v[idx][0].se;
            int empty = 0;
            int idx_j[N];
            idx_j[idx] = 0;
            fori(i,0,N){
                if(i==idx) continue;
                idx_j[i]=-1;LL curr;
                for(int j=0;j<v[i].size();j++){
                    while(j<v[i].size() && v[i][j].se<l) v[i].erase(v[i].begin()+j);
                    if(j<v[i].size() && v[i][j].fi<=l && v[i][j].se>=l){
                        if(idx_j[i]==-1 || curr > v[i][j].se) {
                            idx_j[i]=j;
                            curr = v[i][j].se;
                        }
                    }
                }
                if(idx_j[i]==-1){empty = 1;}
            }
            if(!empty){
                ans++;
                fori(i,0,N){
                    v[i].erase(v[i].begin()+idx_j[i]);
                }
            }
            
        }
        cout << ans << endl;
    }
            
            
        
    return 0;
}
