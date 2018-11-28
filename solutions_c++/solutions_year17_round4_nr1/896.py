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

int N,P;
const int maxn = 110;
int a[10],b;
int ans;

void run4(){
	ans = a[0];
	int c = min(a[1],a[3]);
	ans += c;
	a[1]-= c;
	a[3]-= c;
	int d = a[1]+a[3];
	int e = min(d/2,a[2]);
	ans += e;
	d -= 2*e;
	a[2]-= e;
	if(a[2]==0){
		ans+=(d+3)/4;
	}
	else{
		ans+=a[2]/2;
		if(a[2]%2) ans++;
		else if (d%2) ans++;
	}
	cout << ans << endl;
}
void run3(){
	ans = a[0];
	int c = min(a[1],a[2]);
	ans += c;
	a[1]-=c;
	a[2]-=c;
	int d = a[1]+a[2];
	ans += (d+2)/3;
	cout << ans << endl;
}

void run2(){
	ans = a[0]+(a[1]+1)/2;
	cout << ans << endl;
}

void run(){
	cin >> N >> P;
	mset(a,0);
	fori(i,0,N){
		cin >> b;
		a[b%P]++;
	}
	if (P==2) run2();
	if (P==3) run3();
	if (P==4) run4();
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
