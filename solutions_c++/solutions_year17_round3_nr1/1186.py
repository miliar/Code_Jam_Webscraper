#include <bits/stdc++.h>
#include "prettyprint.hpp"
using namespace std;
typedef long double		num;
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
#define DEBUG_BUILD
#ifdef DEBUG_BUILD
#define DEBUG(x)	do{if(1){cerr<<x<<endl;}}while(0)
#define DBG(x)		do{cerr<<#x<<":\t["<<x<<"]"<<endl;}while(0)
#else
#define DBG(x)		;
#endif
/* Problem specific */
#define MAXN		1100

//in
int N,K;
vector<pair<num,num> >V;

num res;

num lat(num r,num h){
	return r*(2*M_PI)*h;
}
num are(num r){
	return r*r*(M_PI);
}

void solve1(){
	
	sort(V.begin(),V.end());
	DBG(V);
	
	int i=V.size()-1;
	
	res=0;
	res+=are(V[i].fst);
	res+=lat(V[i].fst,V[i].snd);
	
	int k=1;
	for(;k<K && i>=0;--i,++k){
		
		DBG(V[i].fst);
		
		res+=lat(V[i].fst,V[i].snd);
	}
	
}

map<pair<int,int>,num>M_v;
map<pair<int,int>,bool>M_b;

void rec(int p,int k	,/*,list<bool>&R_L ,int&R_us,*/num&R_v	){
	
	if(M_b[{p,k}]){
		R_v = M_v[{p,k}];
		return;
	}
	
	
	if(p>=N || k<=0){
		//R_L=list<bool>();
		//R_us=0;
		R_v=0;
		return;
	};
	
	//list<bool>R1_L;
	//list<bool>R2_L;
	//int R1_us;
	//int R2_us;
	num R1_v;
	num R2_v;
	
	rec(p+1,k  ,/*R1_L,R1_us,*/R1_v);
	
	rec(p+1,k-1,/*R1_L,R2_us,*/R2_v);
	R2_v += lat(V[p].fst,V[p].snd);
	if(k==K){
		R2_v += are(V[p].fst);
	}
	
	if(R1_v > R2_v){
		//R_us=R1_us;
		R_v =R1_v;
	}
	else{
		//R_us=R2_us;
		R_v =R2_v;
	}
	
	M_b[{p,k}] = true;
	M_v[{p,k}] = R_v;
	
	//DBG(R_v);
}

void solve(){
	
	sort(V.begin(),V.end() , std::greater<pair<num,num> >() );
	//DBG(V);
	
	//int R_us;
	num R_v;
	
	M_v.clear();
	M_b.clear();
	
	rec(0,K,R_v);
	res=R_v;
	
}

int main(){ios::sync_with_stdio(false);
	
	int CT;
	cin>>CT;
	//DBG(CT);
	
	for(int ct=1;ct<=CT;++ct){
		cin>>N>>K;
		
		V.clear();
		
		for(int n=0;n<N;++n){
			num r,h;
			cin>>r>>h;
			V.push_back({r,h});
		}
		
		solve();
		
		cout<<"Case #"<< std::setprecision(50) <<ct<<": "<<res<<endl;
	}
	
	return 0;
}
/* Terminal *//*
g++ -std=c++11 X.cpp -W -Wall -g -o exc
./exc > out.txt < in.X.txt
diff -ys --color out.txt 
time ./exc < in.X.txt		*/
