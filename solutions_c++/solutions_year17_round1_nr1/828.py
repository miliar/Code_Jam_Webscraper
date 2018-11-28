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


int T,R,C;
const int maxn = 30;
char g[maxn][maxn], exist[maxn];

int main(void){
    
    //freopen("*.in", "r", stdin);
    //freopen("*.out", "w", stdout);
    cin.sync_with_stdio(false);
    cin >> T;
    forie(t,1,T){
        cin >> R >> C;
        fori(i,0,R){
            cin >> g[i];
        }
        fori(i,0,R){
            exist[i] = 0;
            fori(j,0,C){
                if(g[i][j]!='?'){
                    exist[i] = 1;
                    int k = j-1;
                    char cur = g[i][j];
                    while(k>=0 && g[i][k]=='?'){
                        g[i][k] = cur;
                        k--;
                    }
                    k = j+1;
                    while(k<C && g[i][k]=='?'){
                        g[i][k] = cur;
                        k++;
                    }
                }
            }
        }
        fori(i,0,R){
            if(!exist[i]) continue;
            int k = i-1;
            while(k>=0 && !exist[k]){
                exist[k] = 1;
                fori(j,0,C){
                    g[k][j] = g[i][j];
                }
                k--;
            }
            k = i+1;
            while(k<R && !exist[k]){
                exist[k] = 1;
                fori(j,0,C){
                    g[k][j] = g[i][j];
                }
                k++;
            }
        }
        cout << "Case #" << t << ":\n";
        fori(i,0,R){
            fori(j,0,C){
                cout << g[i][j];
            }
            cout << endl;
        }



    }
    return 0;
}

