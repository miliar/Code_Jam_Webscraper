
#include<bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O2")
#define eb emplace_back
#define pb push_back
#define pw(x) ((1LL)<<(x))
#define buli(x) (__builtin_popcountll(x))
typedef long long ll;
typedef double db;
inline void rd(long long &x){
	int sign=1;char c;while(((c=getchar())<'0'||c>'9')&&c!='-');c=='-'?(sign=-1,x=0):(x=c-'0');
	while((c=getchar())>='0'&&c<='9')x=x*10+c-'0';x*=sign;
}
inline void rd(double&x){scanf("%lf",&x);}
inline void rd(int &x){ll y=0;rd(y);x=y;}


const int inf=1e9;
const int md=1e9+7;
const int maxn=1e5+10;
const db eps=1e-6;

void task(){
	long long n,nk;
	rd(n);rd(nk);
	priority_queue<long long> qu;
	map<long long, long long> ma;
	qu.push(n);
	ma[n] = 1;
//	cout<<n<<endl;
	while(nk){
		long long x ,y;
		x = qu.top();
		qu.pop();
		if(ma.find(x) != ma.end()) {
			y = ma[x];
		}else  
			y = 0;
	//	cout << x << " "<< y << " "<< nk<< endl;
		if(nk <= y){
			
			cout<< x/2 << " " << (x-1)/2 <<endl;	
			break;
		}else{
			nk -= y;
			long long x1 = (x-1)/2, x2 = x/2;
			if(ma.find(x1) == ma.end()) qu.push(x1); 
			ma[x1] += y; 
			if(ma.find(x2) == ma.end()) qu.push(x2);
			ma[x2] += y;
		}
	}
	
}
int main(){
	#ifdef GJY
		freopen("t.in","r",stdin);
		freopen("t.out","w",stdout);
	#endif
	int T;
	rd(T);
	for(int ti = 1; ti <= T; ++ti){
		printf("Case #%d: ",ti);
		task();
	
	}
}





