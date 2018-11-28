/*
 *    Google Code Jam R1B C
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
const LL INF = 1e15;//0x7fffffff;
typedef set<int> Set;
#define ALL(x) x.begin(),x.end()
#define INS(x) inserter(x,x.begin())
//set_union(ALL(x1),ALL(x2),INS(x)),set_intersection

const int maxn = 110;
LL d[maxn][maxn];
double t[maxn][maxn];
int T,N,Q;
LL E[maxn], S[maxn];
int main(void){
    
    //freopen("*.in", "r", stdin);
    //freopen("*.out", "w", stdout);
    cin.sync_with_stdio(false);
    cin >> T;
    cout << fixed << setprecision(9);
    forie(ttt,1,T){
        cout << "Case #" << ttt << ": ";
        cin >> N >> Q;
        forie(i,1,N){
            cin >> E[i] >> S[i];
        }
        forie(i,1,N){
            forie(j,1,N){
                cin >> d[i][j];
            }
            d[i][i] = 0;
        }
        //floyd
        forie (k,1,N){
            forie (i,1,N){
                forie (j,1,N){
                    if (k==i || k==j) continue;
                    if(d[i][k] !=-1 && d[k][j] !=-1)//d[i][j] = min(d[i][j], d[i][k]+d[k][j]);
                        if(d[i][j]==-1 || d[i][k]+d[k][j]<d[i][j]){
                            d[i][j] = d[i][k]+d[k][j];
                        }
                }
            }
        }
        forie(i,1,N){
            forie(j,1,N){
                if(i!=j)t[i][j] = INF;
            }
        }        
        forie(i,1,N){
            forie(j,1,N){
                if(i!=j){
                    if(d[i][j]!=-1 && d[i][j]<=E[i]){
                        t[i][j] = min((double)t[i][j],d[i][j]/(S[i]*1.0));
                    }
                }
            }
        }
        forie (k,1,N){
            forie (i,1,N){
                forie (j,1,N){
                    if (k==i || k==j) continue;
                    if(t[i][k] <INF && t[k][j] <INF)//d[i][j] = min(d[i][j], d[i][k]+d[k][j]);
                        if(t[i][k]+t[k][j]<t[i][j]){
                            t[i][j] = t[i][k]+t[k][j];
                        }
                }
            }
        }
        int U,V;
        fori(i,0,Q){
            cin >> U >> V;
            cout << t[U][V] << ' ';
        }
        cout << endl;
    }
    return 0;
}

