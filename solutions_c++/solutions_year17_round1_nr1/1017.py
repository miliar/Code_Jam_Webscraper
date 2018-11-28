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
typedef pair<int,int> pint;
typedef pair<tint,tint> ptint;
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

tint ele(tint a, tint b){
	if(b==0)return 1;
	if(b%2==0){
		return ele(a*a, b/2);
	}else{
		return a*ele(a*a, b/2);
	}
}

tint mcd(tint a, tint b){
	if(a==0)return b;
	return mcd(b%a, a);
}

double d_abs(long a, long b){
	if(a>b){
		return a-b;
	}
	return b-a;
}

void solve(int caso){
	int r, c;
	cin>>r>>c;
	char ta[r][c];
	forn(i, r){
		forn(j, c){
			cin>>ta[i][j];
		}
	}
	forn(i, r){
		forn(j, c){
			if(ta[i][j]!='?'){
				int fila=j-1;
				while(fila>=0 && ta[i][fila]=='?'){
					fila--;
				}
				forsn(q, fila+1, j){
					ta[i][q]=ta[i][j];
				}
				fila=j+1;
				while(fila<c && ta[i][fila]=='?'){
					fila++;
				}
				forsn(q, j+1, fila){
					ta[i][q]=ta[i][j];
				}
			}
		}
	}
	forn(i, r){
		forn(j, c){
			if(ta[i][j]!='?'){
				int fila=i-1;
				while(fila>=0 && ta[fila][j]=='?'){
					fila--;
				}
				forsn(q, fila+1, i){
					ta[q][j]=ta[i][j];
				}
				fila=i+1;
				while(fila<r && ta[fila][j]=='?'){
					fila++;
				}
				forsn(q, i+1, fila){
					ta[q][j]=ta[i][j];
				}
			}
		}
	}
	cout<<"Case #"<<caso+1<<":"<<endl;
	forn(i, r){
		forn(j, c){
			cout<<ta[i][j];
		}
		cout<<endl;
	}
	cout<<endl;
}




int main (){
	int T;
	cin>>T;
	forn(i, T){
		solve(i);
	}
}
