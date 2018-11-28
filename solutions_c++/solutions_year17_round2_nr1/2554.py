#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip> 
#define forr(i,a,b) for(int i=(a);(i)<int(b);(i)++)
#define forn(i,n) forr(i,0,n)
#define pb push_back

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

int main(){
	std::ios::sync_with_stdio(false);
	cin.tie(NULL);
	freopen("input.in","r",stdin);
	freopen("outputA.out","w",stdout);
	
	int T;
	cin>>T;
	
	int D, N;
	
	forr(t,1,T+1){
		cin>>D>>N;
		vector <int> K,S;
		int aux;
		forn(i,N){
			cin>>aux;
			K.pb(aux);
			cin>>aux;
			S.pb(aux);
		}
		
		double Time=0;
		
		forn(i,N)
			Time = max(Time, double(D - K[i]) / double(S[i]));
		
		cout << setprecision(6) << fixed << "Case #" << t << ": " << double(D)/Time << '\n';
	}
	
	return 0;
}
