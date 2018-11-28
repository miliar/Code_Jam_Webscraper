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
num U;
vector<num>V;
//out
bool keep;
num res;

bool AreEq(num a,num b){
	return fabs(a-b)<EPS;
}

int get_lev(){
	int i=0;
	for(i=0;i<N-1;++i){
		if( !AreEq(V[i], V[i+1]) ){break;}
	}
	return i+1;
}

num agg_sum(int l){
	num ret=0;
	for(int i=0;i<l;++i)ret+=V[i];
	return ret;
}

bool bal(){
	bool ret;
	int l=get_lev();
	
	if(l==N){keep=false;}
	
	num tg=V[l];
	//num ags = agg_sum(l);
	num ags=V[0]*l;
	num v0=V[0];
	num nl= static_cast<num>(l) ;
	num Uol= U / nl;
	
	// vai encher
	if(  (Uol)+(v0)  >=  tg ){
		
		for(int i=0;i<l;++i) V[i] = tg;
		U -= (tg-v0)*nl;
		ret = true;
		
	}
	// vai faltar
	else{
		
		for(int i=0;i<l;++i) V[i] = v0 + (Uol);
		U=0;
		ret = false;
		keep=false;
	}
	
	return ret;
}

void solve(){
	
	sort(V.begin(),V.end() , std::less<num>() );
	//DBG(V);
	
	keep=true;
	//int saf=0;
	for(;keep;){
		
		//if(saf++ >8){break;}
		
		bal();
		
		//DBG(U);
		//DBG(V);
		
	}
	
	res=1;
	for(int n=0;n<N;++n){
		res*=V[n];
	}
	
}

int main(){ios::sync_with_stdio(false);
	
	int CT;
	cin>>CT;
	//DBG(CT);
	
	for(int ct=1;ct<=CT;++ct){
		
		cin>>N>>K;
		cin>>U;
		
		V.resize(N+1);
		
		for(int n=0;n<N;++n){
			num pi;
			cin>>pi;
			//V.push_back(pi);
			V[n]=(pi);
		}
		V[N] = 1.0;
		
		solve();
		
		cout<<"Case #"<<ct<<": "<< fixed << showpoint << std::setprecision(16) <<res<<endl;
	}
	
	return 0;
}
/* Terminal *//*
g++ -std=c++11 X.cpp -W -Wall -g -o exc
./exc > out.txt < in.X.txt
diff -ys --color out.txt 
time ./exc < in.X.txt		*/
