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
	tint a, b, n;
	string s;
	vector<tint> v;
	int ac, aj;
	cin>>ac>>aj;
	vector< pair<int,int> > act[2];
	bool hay[2][1443];
	forn(i,2){
		forn(j,1443){
			hay[i][j]=false;
		}
	}
	forn(i,ac){
		int ini, fi;
		cin>>ini>>fi;
		forsn(mt, ini, fi){
			hay[0][mt]=true;
		}
		act[0].pb(mp(ini,fi));
	}
	forn(i,aj){
		int ini, fi;
		cin>>ini>>fi;
		forsn(mt, ini, fi){
			hay[1][mt]=true;
		}
		act[1].pb(mp(ini,fi));
	}
	forn(_,2){
		sort(act[_].begin(), act[_].end());
	}
	int posta=1e9;
	forn(empieza, 2){
		vector<pair< int,int> > v[2];
		int pers=empieza;
		int tengo=0;
		bool b=false;
		int canti=0;
		int cambios=0;
		int minu[2];
		int dif[2];
		forn(qq,2){
			minu[qq]=0;
			dif[qq]=0;
		}
		forn(mt,1440){
			if(hay[pers][mt]){
				pers=1-pers;
				cambios++;
				if(tengo>0){
					dif[pers]+=tengo;
					//cout<<"en el minuto  "<<mt<<"  agrego  "<<tengo<<"  a difs de "<<pers<<endl;
				}
				tengo=0;
				canti=0;
			}else if(!hay[1-pers][mt]){
				tengo++;
			}else if(tengo>0){
				//cout<<"minuto "<<mt<<" , tengo="<<tengo<<endl;
				v[1-pers].pb(mp(tengo,2));
				tengo=0;
			}
			minu[pers]++;
		}
		//cout<<"--------------------------------------"<<endl;
		if(tengo>0){
			/*int pri=0;
			while(pri<=1440 && !hay[1-pers][pri]){
				pri++;
			}*/
			//cout<<"agrego  "<<tengo<<" a "<<1-pers<<endl;
			if(pers!=empieza)dif[1-pers]+=tengo;
			else v[1-pers].pb(mp(tengo,2));
		}
		forn(qq,2)sort(v[qq].begin(), v[qq].end());
		//cout<<empieza<<"  "<<cambios<<"  "<<minu[0]<<"  "<<minu[1]<<endl;
		//cout<<"difs  "<<dif[0]<<"  "<<dif[1]<<endl;
		
		if(pers!=empieza)cambios++;
		if(minu[0]>minu[1]){
			if(minu[1]+dif[1]>=720){
				//cout<<"listo rango 0"<<endl;
				posta=min(posta, cambios);
			}else{
				minu[1]+=dif[1];
				int agrego=v[1].size()-1;
				while(agrego>=0 && minu[1]<720){
					minu[1]+=v[1][agrego].first;
					cambios+=2;
					agrego--;
					//cout<<"sumo  "<<v[1][agrego].first<<endl;
				}
				if(minu[1]>=720)posta=min(posta,cambios);
			}
		} else {
			if(minu[0]+dif[0]>=720){
				//cout<<"listo rango 1"<<endl;
				posta=min(posta, cambios);
			}else{
				minu[0]+=dif[0];
				int agrego=v[0].size()-1;
				while(agrego>=0 && minu[0]<720){
					minu[0]+=v[0][agrego].first;
					//cout<<"sumo22  "<<v[0][agrego].first<<endl;
					cambios+=2;
					agrego++;
				}
				if(minu[0]>=720)posta=min(posta,cambios);
			}
		}
	}
	cout<<"Case #"<<caso<<": "<<posta<<endl;
}




int main (){
	int T;
	cin>>T;
	forn(caso,T){
		solve(caso+1);
	}
}
