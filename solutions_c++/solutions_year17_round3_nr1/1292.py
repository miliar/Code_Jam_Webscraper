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

double PI = 3.1415926535897932384626433832795028841;

void solve(int caso){
	tint a, b, n, k;
	string s;
	vector< pair<tint, pair<tint,tint> > > v;
	cin>>n>>k;
	forn(i,n){
		cin>>a>>b;
		v.pb(mp(a, mp(b,a*b)));
	}
	sort(v.begin(), v.end());
	double best=0.00000;
	if(k==1){
		forn(i,n){
			best=max(best, PI*(double)(v[i].first*v[i].first+2*v[i].second.second));
		}
		printf("Case #%d: %.8f\n", caso, best);
		return;
	}
	forn(i, n){
		forsn(j, i+k-1, n){
			if(abs(j-i)+1>=k){
				//cout<<"miro posi  "<<i<<" , "<<j<<endl;
				double mians=0.00000;
				vector< tint > vec;
				forsn(q, i+1, j){
					vec.pb(v[q].second.second);
				}
				sort(vec.begin(), vec.end());
				int ind=vec.size()-1;
				int canti=0;
				while(canti<k-2){
					mians+=2.0000*vec[ind];
					ind--;
					canti++;
				}
				//printf("alturas medio  %.8f\n", mians);
				mians+=(double)(v[j].first*v[j].first);
				//printf("resta cuads  %.8f\n", mians);
				mians+=(double)(2.0000*v[i].second.second);
				mians+=(double)(2.0000*v[j].second.second);
				//printf("mians  %.8f\n", mians);
				best=max(best, PI*mians);
			}
		}
	}
	printf("Case #%d: %.8f\n", caso, best);
}




int main (){
	int T;
	cin>>T;
	forn(caso,T){
		solve(caso+1);
	}
}
