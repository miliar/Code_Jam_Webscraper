#include <bits/stdc++.h>

using namespace std;
#define pb push_back
typedef long long LL;
#define INF 10000000
int dp[110][210][110][110];
int oHd,B,D;

int f(int Hd,int Ad, int Hk, int Ak){	
	if(Hk <= 0) return 0;
	if(Hd <= 0)  return INF;
	
	int &res = dp[Hd][Ad][Hk][Ak];
	if(res!=-1) return res;
	res = INF;	
		
	//Attack	
	res = min(res, 1 + f( Hd-Ak, Ad, Hk-Ad, Ak) );
	//Buff
	if(Ad < Hk)
		res = min(res, 1 + f( Hd-Ak, Ad+B, Hk, Ak) );		
	
	//Cure
	res = min(res, 1 + f( oHd-Ak, Ad, Hk, Ak) );
	//DeBuff
	res = min(res, 1 + f( Hd-max(0,Ak-D), Ad, Hk, max(0,Ak-D) ) );
//	cout << Hd << " " << Ad << " " << Hk << " " << Ak <<  " " << res << endl;
	return res;
}


int Hd, Ad, Hk, Ak;

void solve(int test){
	cout << "Case #" << test + 1 << ": ";	
	cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
	oHd = Hd;
	memset(dp,-1,sizeof dp);
	int res = f(Hd,Ad,Hk,Ak);
	if( res < INF){
		cout << res << endl;
	}else{
		cout << "IMPOSSIBLE" << endl;
	}
}

int ntest;
int main(){
	//freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt2.in","r",stdin);
	freopen("test.out","w",stdout);
	cin >> ntest;	
	for(int test=0; test<ntest; test++){
		solve(test);
	}
	return 0;
}
