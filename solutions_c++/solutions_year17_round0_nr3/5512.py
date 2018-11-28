#include <bits/stdc++.h>
#include "../prettyprint.hpp"
using namespace std;
typedef long long int		num;
typedef vector<num>		vn;
typedef list<num>		ln;
typedef bitset<16>		bs16;
template <typename K,typename V> using ump = unordered_map<K,V>;
//using li=list<int>;
/* Streams */
string	BUF;
#define ssb					getline(cin,BUF);stringstream(BUF)
/* discard chain of chr *if* it's present */
//#define eat(ism,chr)	while(ism.peek()==chr){ism.get();}
#define eat(ism,chr)	while(ism.peek()==chr){ism.ignore();}
/* Misc */
#define fst		first
#define snd		second
#define NLM		numeric_limits<num>::max()
#define NLS		numeric_limits<streamsize>::max()
#define I3F		0x3f3f3f3f
#define EPS		1e-8
/* Containers */
#define Range(itr,Cnt)		const_iterator itr=Cnt.begin();itr!=Cnt.end();++itr
#define foreach(itr,Cnt)	for(typeof((Cnt).begin())itr=(Cnt).begin();itr!=(Cnt).end();++itr)
#define all(Cnt)			(Cnt).begin(), (Cnt).end()
#define in(elm,Cnt)			((Cnt).find(elm)!=(Cnt).end())
#define sz(Cnt)				((int)(Cnt.size()))
/* gcc-built-in */
#define gcd				__gcd
/* Debugging */
// -D DEBUG_BUILD
//#define DEBUG_BUILD
#ifdef DEBUG_BUILD
#define DEBUG(x)	do{if(1){cerr<<x<<endl;}}while(0)
#define DBG(x)		do{cerr<<#x<<":\t["<<x<<"]"<<endl;}while(0)
#else
#define DBG(x)		;
#endif
/* Problem specific */
#define MAXN		1000000000000000123

num lev(num x){
	return log2(x);
}
num pop(num levx){
	return (1 << (levx));
}

num fL(num N,num K){
	return  (N-K)/(pop(lev(K)+1));
}
num fR(num N,num K){
	return ((N-K)/(pop(lev(K)))+1)/2;
}

num ans1,ans2;
void fcl(num N,num K){
	num dl,dr;
	
	dl=fL(N,K);
	dr=fR(N,K);
	
	ans2=min(dl,dr);
	ans1=max(dl,dr);
}

int main(){ios::sync_with_stdio(false);
	int CT,ct;
	
	num N,K;
	
	cin>>CT;
	for(ct=1;ct<=CT;++ct){
		cin>>N>>K;
		//brt(N,K);
		fcl(N,K);
		cout<<"Case #"<<ct<<": "<<ans1<<" "<<ans2<<endl;
	}
	
	return 0;
}

