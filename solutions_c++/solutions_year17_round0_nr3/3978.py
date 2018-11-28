#include<iostream>
#include<fstream>
#include<math.h>
#include<algorithm>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<sstream>
#include<set>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n); i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n); i++)
#define esta(x,v) (find((v).begin(),(v).end(),(x)) !=  (v).end())
#define index(x,v) (find((v).begin(),(v).end(),(x)) - (v).begin())
#define debug(x) cout << #x << " = "  << x << endl
#define pb push_back
#define mp make_pair

typedef long long tint;
typedef unsigned long long utint;
typedef long double ldouble;

typedef vector<int> vint;

int toNumber (string s)
{
	int Number;
	if ( ! (istringstream(s) >> Number) ) Number = 0; // el string vacio lo manda al cero
	return Number;
}

string toString (int number)
{
    ostringstream ostr;
    ostr << number;
    return  ostr.str();
}

bool isT(int a){
	string s=toString(a);
	forsn(i, 1, s.size()){
		if(s[i]<s[i-1])return false;
	}
	return true;
}

void solve(string s){
	int n=s.size();
	forn(_, 20){
		forn(i, n-1){
			if(s[i]>s[i+1]){
				s[i]--;
				forsn(j, i+1, n){
					s[j]='9';
				}
				break;
			}
		}
		//cout<<s<<endl;
	}
	if(s[0]=='0'){
		s=s.substr(1);
	}
	cout<<s<<endl;
}

int main (){
	int T;
	cin>>T;
	forn(caso, T){
		tint n, k;
		cin>>n>>k;
		set< pair<tint,tint> > s;
		set< pair<tint,tint> >::iterator it;
		s.insert(mp(n, -1));
		tint L, R;
		while(k--){
			it = s.end();
			it--;
			pair<tint,tint> saco = *it;
			tint tam=saco.first;
			tint pos=-saco.second;
			if(saco.first%2){
				s.erase(it);
				L=tam/2;
				R=tam/2;
				s.insert(mp(tam/2, -pos));
				s.insert(mp(tam/2, -(pos+tam/2+1)));
			}else{
				s.erase(it);
				L=tam/2-1;
				R=tam/2;
				s.insert(mp(tam/2-1, -pos));
				s.insert(mp(tam/2, -(pos+tam/2)));
			}
		}
		cout<<"Case #"<<caso+1<<": "<<max(L,R)<<" "<<min(L,R)<<endl;
	}
}
