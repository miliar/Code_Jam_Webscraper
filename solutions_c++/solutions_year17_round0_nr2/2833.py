#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <cctype>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <complex>
#include <numeric>
#include <valarray>
#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;

#define inf 1061109567
#define pb push_back
#define mp make_pair
#define all(a) a.begin(),a.end()
#define mem(x,a) memset(x,a,sizeof(x))
#define rep(i,n) for(int i(0),_n(n);i<_n;++i)
#define repi(i,a,b) for(int i(a),_b(b);i<=_b;++i)
#define repr(i,a,b) for(int i(a),_b(b);i>=_b;--i)
#define repe(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define len(x) ((int)(x.size()))
#define DEBUG 1 
#if DEBUG && !ONLINE_JUDGE 
	#define debug(args...) (Debugger()) , args
	class Debugger { public: Debugger(const std::string& _separator = ", ") : first(true), separator(_separator){} template<typename ObjectType> Debugger& operator , (const ObjectType& v) { if(!first) std::cerr << separator; std::cerr << v; first = false; return *this; } ~Debugger() { std::cerr << endl;} private: bool first; std::string separator; }; template <typename T1, typename T2> inline std::ostream& operator << (std::ostream& os, const std::pair<T1, T2>& p) { return os << "(" << p.first << ", " << p.second << ")"; } template<typename T> inline std::ostream &operator << (std::ostream & os,const std::vector<T>& v) { bool first = true; os << "["; for(unsigned int i = 0; i < v.size(); i++) { if(!first) os << ", "; os << v[i]; first = false; } return os << "]"; } template<typename T> inline std::ostream &operator << (std::ostream & os,const std::set<T>& v) { bool first = true; os << "["; for (typename std::set<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii) { if(!first) os << ", "; os << *ii; first = false; } return os << "]"; } template<typename T1, typename T2> inline std::ostream &operator << (std::ostream & os,const std::map<T1, T2>& v) { bool first = true; os << "["; for (typename std::map<T1, T2>::const_iterator ii = v.begin(); ii != v.end(); ++ii) { if(!first) os << ", "; os << *ii ; first = false; } return os << "]"; } 
#else 
		#define debug(args...) 
#endif









int main(){
	ios_base::sync_with_stdio(0);
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		cout<<"Case #"<<t+1<<": ";
		string s;
		int k;
		cin>>s;
		string ss=s;
		int ans=0;
		k=len(s);
		int fs=inf;
		for(int i=len(s)-1;i>0;i--){
			if(s[i]<='0'){
				s[i]='9';
				s[i-1]--;
				if(fs==inf){
					fs=i+1;
				}
			}
		}


		if(s[0]<='0')ans=inf;
		if(ans==inf){
			for(int i=0;i<k-1;i++){
				cout<<'9';
			}
			cout<<endl;
			continue;
		}

		// if(fs!=inf){
		// 	for(int i=fs;i<len(s);i++){
		// 		s[i]='9';
		// 	}
		// 	cout<<s<<endl;
		// 	continue;
		// }
		s=ss;

		string tem="";

		for(int i=0;i<len(s)-1;i++){

			if(ans==inf){
				tem+='9';
			}

			else if(s[i]>s[i+1]){
				ans=inf;
				int f=inf;
				if(len(tem)){
					int pos=len(tem)-1;
					while(pos>=0&&tem[pos]==s[i]){
						tem[pos]--;
						f=pos;
						pos--;
					}
					for(int j=f+1;j<len(tem);j++)tem[j]='9';
				}

				if(f==inf)tem+=char(s[i]-1);
				else{
					tem+='9';
				}
			}
			else{
				tem+=s[i];
			}
		}
		if(ans==inf){
			tem+='9';
		}
		else{
			tem+=s[len(s)-1];
		}

		cout<<tem;

		cout<<endl;


	}
	
}









