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
//#include <unordered_map>
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
#define X first
#define Y second
typedef unsigned long long ULL;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<LL> vl;
typedef set<int> Set;

#define DBG 0

#define fori(i,a,b) for(int i = (a); i < (b); i++)
#define forie(i,a,b) for(int i = (a); i <= (b); i++)
#define ford(i,a,b) for(int i = (a); i > (b); i--)
#define forde(i,a,b) for(int i = (a); i >= (b); i--)
#define forls(i,a,b,n) for(int i = (a); i != (b); i = n[i])
#define mset(a,v) memset(a, v, sizeof(a))
#define mcpy(a,b) memcpy(a, b, sizeof(a))
#define sz(x) ((int)((x).size()))
#define ALL(x) x.begin(),x.end()
#define INS(x) inserter(x,x.begin())
//set_union(ALL(x1),ALL(x2),INS(x)),set_intersection

#define MIN_LD -2147483648
#define MAX_LD  2147483647
#define MIN_LLD -9223372036854775808
#define MAX_LLD  9223372036854775807
#define MAX_INF 18446744073709551615
const int INF = 0x7fffffff;
const LL MOD = 1000000007;
const int DX[] = { 1,  0, -1,  0,  1, -1,  1, -1};
const int DY[] = { 0,  1,  0, -1,  1, -1, -1,  1};

const int maxn = 1000+10;
int N,C,M;
int P,B;
int a[maxn][maxn],b[maxn][maxn];
int mask[maxn];

void run(){
	cin >> N >> C >> M;
	mset(a,0);
	mset(b,0);
	fori(i,0,M){
		cin >> P >> B;
		a[B][P]++;b[B][P]++;
	}
	int s = M;
	int ans1 = 0;
	while(s>0){
		ans1++;
		mset(mask,0);
		int empty = 0;
		forie(j,1,N){
			int occupy = 0;
			forie(i,1,C){
				if (mask[i]) continue;
				if(a[i][j]){
					if(!occupy){
						a[i][j]--;s--;
						mask[i] = 1;
						occupy = 1;
					}
					else if(empty > 0){
						a[i][j]--;s--;
						mask[i] = 1;
						empty--;
					}
				}
			}
			if(!occupy) empty++;
		}
	}
	int ans2 = 0;
	forde(j,N,1){
		int sum = 0;
		forie(i,1,C){
			sum+=b[i][j];
		}
		ans2+=max(0,(sum-ans1));
	}
	cout << ans1 << " " << ans2 << endl;
}

int main(void){
    
    //freopen("*.in", "r", stdin);
    //freopen("*.out", "w", stdout);
    cin.sync_with_stdio(false);
    int T; cin >> T;
    forie(t,1,T){
        cout << "Case #" << t << ": ";
        run();
    }
    return 0;
}
