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

int hago(int hd,int ad,int hk,int ak,int b, int d, int i, int j){
	int cant=0;
	int miv=hd;
	int suv=hk;
	while(true){
		//if(i==0 && j==0)cout<<"turnos  "<<cant<<", vida="<<miv<<", suya="<<suv<<endl;
		if(ad>=suv){
			return cant+1;
		}
		if(j>0){
			ak-=d;
			j--;
			miv-=ak;
			cant++;
			if(miv<=0){
				miv=hd-ak-d-ak;
				cant++;
				if(miv<=0)return 1e9;
			}
		}else if(i>0){
			ad+=b;
			cant++;
			miv-=ak;
			i--;
			if(miv<=0){
				miv=hd-2*ak;
				cant++;
				if(miv<=0)return 1e9;
			}
		}else{
			suv-=ad;
			if(suv<=0)return cant+1;
			miv-=ak;
			cant++;
			if(miv<=0){
				miv=hd-2*ak;
				cant++;
				if(miv<=0)return 1e9;
			}
		}
	}
}

void solve(int caso){
	int hd, ad, hk, ak, b, d;
	cin>>hd>>ad>>hk>>ak>>b>>d;
	int ans=1e9;
	forn(i, 101){
		forn(j, 101){
			
			int temp=hago(hd, ad, hk, ak, b, d, i, j);
			if(temp<ans){
				//cout<<"debuff "<<j<<" , buff "<<i<<endl;
				ans=temp;
				//cout<<ans<<endl;
			}
		}
	}
	cout<<"Case #"<<caso+1<<": ";
	if(ans<1e9){
		cout<<ans<<endl;
	}else{
		cout<<"IMPOSSIBLE"<<endl;
	}
}




int main (){
	int T;
	cin>>T;
	forn(i, T){
		solve(i);
	}
}
