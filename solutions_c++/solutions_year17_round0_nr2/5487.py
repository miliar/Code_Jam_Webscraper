#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>
#define FOR(i,a,b) for(i=a; i<=b; i++)
#define FOR2(i,n) FOR(i,0,n-1)
#define TFOR(i,a,b) for(i=a; i>=b; i--)
#define f first
#define s second
#define all(x) x.begin(),x.end() 
#define MAXN 
using namespace std;
typedef pair < int , int > pii;
int read(){ int res(0),sign(1); char c;
	while(1){ c = getchar(); if('0' <= c && c <= '9') { res = c - '0'; break; } else if(c == '-') { sign = -1; break; } }
	while(1){ c = getchar(); if('0' <= c && c <= '9') res = res*10 + c - '0'; else break; }
	return res * sign;
}
vector < int > V, res;
bool rec(int x, int pre, int flag){

	if(x == V.size()) return true;

	int i;
	int start = flag ? V[x] : 9;
	TFOR(i,start,pre){
		res.push_back(i);
		if( rec(x+1,i,flag&&(i==V[x])) )
			return true;
		res.resize( res.size() - 1 );
	}

	return false;

}
void solve(long long n) {

	V.clear();
	res.clear();
	long long x = n;
	while(x){
		V.push_back(x%10);
		x /= 10;
	}
	reverse(all(V));
	if( rec(0,0,true) ){
		bool flag = true;
		for(vector < int > :: iterator it = res.begin(); it != res.end(); ++it) {
			if(flag && !(*it))
				continue;
			flag = false;
			printf("%d" , *it);
		}
	}
}
int main()
{
	long long a;
	int T = read(), i;
	FOR(i,1,T) {
		printf("Case #%d: " , i);
		scanf("%lld" , &a);
		solve(a);
		printf("\n");
	}
	return 0;
}
