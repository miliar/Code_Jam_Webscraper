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
		string s;
		cin>>s;
		cout<<"Case #"<<caso+1<<": ";
		if(s.size()<0){
			int n = toNumber(s);
			while(n){
				if(n<10){
					cout<<n<<endl;
					break;
				}
				if(isT(n)){
					cout<<n<<endl;
					break;
				}
				n--;
			}
		}else{
			solve(s);
		}
	}
}
