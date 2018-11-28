#include <cassert>// c
#include <iostream>// io
#include <iomanip>
#include <fstream>
#include <sstream>
#include <vector>// container
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <stack>
#include <algorithm>// other
#include <complex>
#include <numeric>
#include <functional>
#include <random>
#include <regex>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define ALL(c) c.begin(),c.end()
#define REP(i,n) FOR(i,0,n)
#define REPr(i,n) FORr(i,0,n)
#define FOR(i,l,r) for(int i=(int)(l);i<(int)(r);++i)
#define FORr(i,l,r) for(int i=(int)(r)-1;i>=(int)(l);--i)
#define EACH(it,o) for(auto it = (o).begin(); it != (o).end(); ++it)
#define IN(l,v,r) ((l)<=(v) && (v)<(r))
#define UNIQUE(v) v.erase(unique(ALL(v)),v.end())
//debug
#define DUMP(x)  cerr << #x << " = " << (x)
#define LINE()    cerr<< " (L" << __LINE__ << ")"

class range {
private:
	struct Iter{
		int v;
		int operator*(){return v;}
		bool operator!=(Iter& itr) {return v < itr.v;}
		void operator++() {++v;}
	};
	Iter i, n;
public:
	range(int n) : i({0}), n({n}) {}
	range(int i, int n) : i({i}), n({n}) {}
	Iter& begin() {return i;}
	Iter& end() {return n;}
};
struct rrange{
	struct Iter{
		int v,step;
		Iter& operator++(){v-=step;return *this;}
		bool operator!=(Iter& itr){return v>itr.v;}
		int& operator*(){return v;}
	};
	Iter i, n;
	rrange(int i, int n,int step):i({i-1,step}), n({n-1,step}){}
	rrange(int i, int n):rrange(i,n,1){}
	rrange(int n) :rrange(0,n){}
	Iter& begin(){return n;}
	Iter& end(){return i;}
};
//input
template<typename T1,typename T2> istream& operator >> (istream& is,pair<T1,T2>& p){return is>>p.first>>p.second;}
template<typename T1> istream& operator >> (istream& is,tuple<T1>& t){return is >> get<0>(t);}
template<typename T1,typename T2> istream& operator >> (istream& is,tuple<T1,T2>& t){return is >> get<0>(t) >> get<1>(t);}
template<typename T1,typename T2,typename T3> istream& operator >> (istream& is,tuple<T1,T2,T3>& t){return is >>get<0>(t)>>get<1>(t)>>get<2>(t);}
template<typename T1,typename T2,typename T3,typename T4> istream& operator >> (istream& is,tuple<T1,T2,T3,T4>& t){return is >> get<0>(t)>>get<1>(t)>>get<2>(t)>>get<3>(t);}
template<typename T1,typename T2,typename T3,typename T4,typename T5> istream& operator >> (istream& is, const tuple<T1,T2,T3,T4,T5>& t){return is >> get<0>(t) >> get<1>(t) >> get<2>(t) >> get<3>(t) >> get<4>(t);}
template<typename T1,typename T2,typename T3,typename T4,typename T5,typename T6> istream& operator >> (istream& is, const tuple<T1,T2,T3,T4,T5,T6>& t){return is >> get<0>(t) >> get<1>(t) >> get<2>(t) >> get<3>(t) >> get<4>(t) >> get<5>(t);}
template<typename T1,typename T2,typename T3,typename T4,typename T5,typename T6,typename T7> istream& operator >> (istream& is, const tuple<T1,T2,T3,T4,T5,T6,T7>& t){return is >> get<0>(t) >> get<1>(t) >> get<2>(t) >> get<3>(t) >> get<4>(t) >> get<5>(t) >> get<6>(t);}
template<typename T> istream& operator >> (istream& is,vector<T>& as){for(int i:range(as.size()))is >>as[i];return is;}

//output
template<typename T> ostream& operator << (ostream& os, const set<T>& ss){for(auto a:ss){if(a!=ss.begin())os<<" "; os<<a;}return os;}
template<typename T1,typename T2> ostream& operator << (ostream& os, const pair<T1,T2>& p){return os<<p.first<<" "<<p.second;}
template<typename K,typename V> ostream& operator << (ostream& os, const map<K,V>& m){bool isF=true;for(auto& p:m){if(!isF)os<<endl;os<<p;isF=false;}return os;}
template<typename T1> ostream& operator << (ostream& os, const tuple<T1>& t){return os << get<0>(t);}
template<typename T1,typename T2> ostream& operator << (ostream& os, const tuple<T1,T2>& t){return os << get<0>(t)<<" "<<get<1>(t);}
template<typename T1,typename T2,typename T3> ostream& operator << (ostream& os, const tuple<T1,T2,T3>& t){return os << get<0>(t)<<" "<<get<1>(t)<<" "<<get<2>(t);}
template<typename T1,typename T2,typename T3,typename T4> ostream& operator << (ostream& os, const tuple<T1,T2,T3,T4>& t){return os << get<0>(t)<<" "<<get<1>(t)<<" "<<get<2>(t)<<" "<<get<3>(t);}
template<typename T1,typename T2,typename T3,typename T4,typename T5> ostream& operator << (ostream& os, const tuple<T1,T2,T3,T4,T5>& t){return os << get<0>(t)<<" "<<get<1>(t)<<" "<<get<2>(t)<<" "<<get<3>(t)<<" "<<get<4>(t);}
template<typename T1,typename T2,typename T3,typename T4,typename T5,typename T6> ostream& operator << (ostream& os, const tuple<T1,T2,T3,T4,T5,T6>& t){return os << get<0>(t)<<" "<<get<1>(t)<<" "<<get<2>(t)<<" "<<get<3>(t)<<" "<<get<4>(t)<<" "<<get<5>(t);}
template<typename T1,typename T2,typename T3,typename T4,typename T5,typename T6,typename T7> ostream& operator << (ostream& os, const tuple<T1,T2,T3,T4,T5,T6,T7>& t){return os << get<0>(t)<<" "<<get<1>(t)<<" "<<get<2>(t)<<" "<<get<3>(t)<<" "<<get<4>(t)<<" "<<get<5>(t)<<" "<<get<6>(t);}
template<typename T> ostream& operator << (ostream& os, const vector<T>& as){for(int i:range(as.size())){if(i!=0)os<<" "; os<<as[i];}return os;}
template<typename T> ostream& operator << (ostream& os, const vector<vector<T>>& as){for(int i:range(as.size())){if(i!=0)os<<endl; os<<as[i];}return os;}

// values
template<typename T> inline T INF(){assert(false);};
template<> inline int INF<int>(){return 1<<28;};
template<> inline ll INF<ll>(){return 1LL<<58;};
template<> inline double INF<double>(){return 1e16;};
template<> inline long double INF<long double>(){return 1e16;};

template<class T> inline T EPS(){assert(false);};
template<> inline int EPS<int>(){return 1;};
template<> inline ll EPS<ll>(){return 1LL;};
template<> inline double EPS<double>(){return 1e-8;};
template<> inline long double EPS<long double>(){return 1e-8;};

// min{2^r | n < 2^r}
template<typename T> T upper_pow2(T n){
	T res=1;while(res<n)res<<=1;return res;
}
// max{d | 2^d  <= n}
template<typename T> T msb(T n){
	int d=30;while((1<<d)>n)d--;return d;
}

template<typename T,typename U> T pmod(T v,U M){return (v%M+M)%M;}

class Main{
	public:

	void cas(int q){
		int N;cin >> N;
		vector<int> cs(6);cin >> cs;
		vector<char> cm(6);
		cm[0] = 'R';cm[1] = 'O';cm[2] = 'Y';cm[3]='G';cm[4] = 'B';cm[5] ='V';
		int Csum = 0,C1 = 0,C2 = 0;
		for(int i:range(6)) Csum +=cs[i];
		for(int i:range(3)) C1 +=cs[i*2];
		for(int i:range(3)) C2 +=cs[i*2+1];
		
		// if(Csum == 1){
		// 	string res = "";
		// 	for(int i:range(6))if(cs[i] == 1) res += cm[i];
		// 	cout << make_tuple("Case","#"+to_string(q+1)+":",res)<<endl;
		// 	continue;
		// }
		if(C1 == 0){
			cerr << 1 << endl;
			cout << make_tuple("Case","#"+to_string(q+1)+":","IMPOSSIBLE")<<endl;
			return;
		}
		// C1 > 0

		for(int c:range(3)){
			bool ok = true;
			for(int i:range(6))if(i != 2*c && i != (2*c+3)%6){
				ok &= cs[i] == 0;
			}
			if(ok && cs[2*c] == cs[(2*c+3)%6]){
				string res = "";
				for(int i:range(cs[2*c])){
					res += cm[2*c];
					res += cm[(2*c+3)%6];
				}
				cout << make_tuple("Case","#"+to_string(q+1)+":",res)<<endl;
				return;
			}
		}

		{
			bool ok = true;
			for(int c:range(3)){
				ok &= (cs[2*c]- cs[(2*c+3)%6] > 0 || cs[(2*c+3)%6] == 0);
			}
			if(!ok){
				cerr << 2 << endl;
				cout << make_tuple("Case","#"+to_string(q+1)+":","IMPOSSIBLE")<<endl;
				return;
			}
		}

		vector<int> tmp(3);
		for(int c:range(3)){
			tmp[c] = cs[2*c] - cs[(2*c+3)%6];
		}

		string res = "";
		while(tmp[0] + tmp[1] + tmp[2] > 0){
			int mc = -1,M = -1;
			for(int c:range(3))if(res.size() == 0 || cm[2*c] != res[res.size()-1]){
				if(M < tmp[c]){
					mc = c;
					M = tmp[c];
				}else if(M <= tmp[c] && res.size() > 0 && cm[2*c] == res[0]){
					mc = c;
					M = tmp[c];
				}
			}
			if(M <= 0){
				cerr << res << endl;
				cerr << tmp << endl;
				cerr << 3 << endl;
				cout << make_tuple("Case","#"+to_string(q+1)+":","IMPOSSIBLE")<<endl;
				return;
			}
			res += cm[2*mc];
			tmp[mc]--;
		}
		if(res.size() > 0 && res[0] == res[res.size()-1]){
			cerr << 4 << endl;
			cout << make_tuple("Case","#"+to_string(q+1)+":","IMPOSSIBLE")<<endl;
			return;
		}

		cerr << res << endl;
		for(int c:range(3)){
			if(cs[(2*c+3)%6] > 0){
				string v = "";
				for(int i:range(cs[(2*c+3)%6])){
					v += cm[2*c];
					v += cm[(2*c+3)%6];
				}
				int i = -1;
				for(int j:range(res.size()))if(res[j] == cm[2*c]){
					i = j;break;
				}
				res = res.substr(0,i) + v + res.substr(i);
			}
		}
		cout << make_tuple("Case","#"+to_string(q+1)+":",res)<<endl;
	}
	void run(){
		int T;cin >> T;
		for(int q:range(T)){
			cas(q);
		}
	}
};

int main(){
	cout <<fixed<<setprecision(20);
	cin.tie(0);
	ios::sync_with_stdio(false);
	Main().run();
	return 0;
}
