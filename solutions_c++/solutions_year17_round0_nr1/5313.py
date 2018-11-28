#include <bits/stdc++.h>
#include "../prettyprint.hpp"
using namespace std;
typedef long int		num;
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
#define MAXN		10123

num V[MAXN];
string S;
num N;
num K;

void ppk(){
	for(num i=0;i<N;++i){
		cout<<((V[i]==1)?"+":"-");
	}cout<<endl;
}

num cn_hap(const string &s){
	num ret=0;
	for(auto const &c:s)
		if(c=='+')++ret;
	return ret;
}

bool v_flp(string &s,num pos){
	return (pos+K<=(num)s.size());
}
// ret= delta_hap
num cn_hap(string &s,num pos){
	num ret=0;
	for(num i=pos; (i<pos+K) && (i<(num)s.size()) ;++i){
		if(s[i]=='-'){++ret;s[i]='+';}
		else         {--ret;s[i]='-';}
	}
	return ret;
}

unordered_map<string,bool> Mb;
unordered_map<string,num> Mn;

typedef enum component{dst=0,hap=1,str=2}component;
typedef std::tuple<num,num,string>cell;
using std::get;

class lessDR{
		public: bool operator() (const cell& lhs,const cell&rhs)const{
			return	
					get<dst>(lhs)!=get<dst>(rhs)?
					get<dst>(lhs) >get<dst>(rhs):
					get<hap>(lhs)!=get<hap>(rhs)?
					get<hap>(lhs) >get<hap>(rhs):
					0;
			}
		};

num res_n;
bool res_b;
void s(){
	
	Mb.clear();
	Mn.clear();
	priority_queue<cell,std::vector<cell>,lessDR> Q;
	
	Q.push(make_tuple(0,cn_hap(S),S));
	
	res_b=false;
	
	for(;!Q.empty();){//DBG(Q.size());
		
		cell x = Q.top();Q.pop();
		//DBG(get<str>(x));
		
		if(get<hap>(x)==(num)S.size()){
			res_b=true;
			res_n=get<dst>(x);
			//DBG(get<hap>(x));
			break;
		}
		//mem
		//string 
		if(Mb[get<str>(x)]){
			
			if( Mn[get<str>(x)] <= get<dst>(x) ){continue;}
			
			Mn[get<str>(x)] = get<dst>(x) ;
		}
		Mb[get<str>(x)]=true;
		
		//cout<<"branch"<<endl;
		//branch
		for(num i=0; i<=(num)S.size()-K ;++i){
			if(!v_flp(get<str>(x),i)){
				//DBG(i);
				continue;
			}
			//DBG(i);
			string n_str=get<str>(x);
			num n_dst=get<dst>(x)+1;
			num n_hap=get<hap>(x)+cn_hap(n_str,i);
			Q.push( make_tuple(n_dst,n_hap,n_str) );
		}
		
		
	}
	
}

int main(){ios::sync_with_stdio(false);
	int CT,ct;
	
	//num i;
	cin>>CT;
	for(ct=1;ct<=CT;++ct){
		cin>>S;
		/*cin.get();for(N=0;;){
			if(cin.peek()==' '){break;}
			//V[N++]=((cin.get()=='+')?1:-1);
		}cin.get();*/
		cin>>K;
		
		//DBG(K);
		//DBG(S);
		//ppk();
		
		s();
		
		if(res_b){
			cout<<"Case #"<<ct<<": "<<res_n<<endl;
		}
		else{
			cout<<"Case #"<<ct<<": "<<"IMPOSSIBLE"<<endl;
		}
	}
	
	return 0;
}

