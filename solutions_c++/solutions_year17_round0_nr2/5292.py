#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int	num;
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
#define MAXN		1000000000000000008

/*bool is_tidy(num n){
	num r=n%10;
	num nr;
	for(;n>0;){
		nr=n%10;
		if(r<nr)return false;
		r=nr;
		n/=10;
	}
	return true;
}

num f(num n){
	num i;
	for(i=n;i>0;--i){
		if(is_tidy(i))break;
	}
	return i;
}*/

int N[30];
int D;

bool is_tidy(){
	int i=0;
	for(i=0;i<D-1;++i){
		//DBG(N[i]);
		if(N[i]>N[i+1])return false;
	}
	return true;
}

void sing(){
	int i=0;
	for(i=0;i<D-1;++i){
		if(N[i]>N[i+1]){
			N[i]--;
			for(i=i+1;i<D;++i){
				N[i]=9;
			}
		}
	}
}

void solve(){
	
	for(;;){
		if(is_tidy()){return;}
		sing();
	}
	
}

int main(){ios::sync_with_stdio(false);
	int ct;
	int t;
	//num x;
	//num ans;
	cin>>ct;
	for(t=1;t<=ct;++t){
		//DBG(ct);
		eat(cin,'\n');
		for(D=0;;){
			if(cin.peek()=='\n'){break;}
			N[D++]=cin.get()-'0';
		}
		//DBG(D);
		//for(int d=0;d<D;++d){cout<<N[d]<<"]";}cout<<endl;
		solve();
		
		//cin>>x;
		//ans=f(x);
		cout<<"Case #"<<t<<": ";//<<ans<<endl;
		bool np=true;
		for(int i=0;i<D;++i){
			if(N[i]!=0){np=false;}
			if(!np){
				cout<<N[i];
			}
		}
		cout<<endl;
	}
	/*for(num x=1;x<MAXN;++x){
		M_is_tidy[x]=
	}*/
	return 0;
}
/* Terminal *//*
g++ -std=c++11 X.cpp -W -Wall -g -o exc
./exc > out.txt < in.X.txt
diff -ys --color out.txt 
time ./exc < in.X.txt		*/
