/*
 *    Google Code Jam 2017 Qual B
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


int T;
LL N;

int main(void){
    
    //freopen("*.in", "r", stdin);
    //freopen("*.out", "w", stdout);
    cin.sync_with_stdio(false);
    cin >> T;
    forie(t,1,T){
        cin >> N;
        cout << "Case #" << t << ": ";
        vi v;
        LL M = N;
        while(N>0){
            v.PB(N%10);
            N/=10;
        }
        reverse(v.begin(),v.end());
        int n = v.size();
        if(n==1){cout << v[0] << endl;continue;}
        int idx = -1;
        fori(i,0,n-1){
            if(v[i]<=v[i+1]) continue;
            idx = i;break;
        }
        if (idx==-1) {
            cout << M << endl;
            continue;
        }
        int j = idx;
        while(j>=0 && v[j]==v[idx])j--;
        j++;
        v[j]--;
        fori(i,j+1,n){
            v[i] = 9;
        }
        LL ans = 0;
        fori(i,0,n){
            ans *=10;
            ans+=v[i];
        }
        cout << ans << endl;
    }
            
    return 0;
}


