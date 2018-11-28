#include <bits/stdc++.h>
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie
using namespace std;
typedef long long int Long;
typedef vector<Long> Lista;
const Long INF = 1000000000000000000LL;

Lista pots(20);
Long DP[22][12][3];

Long Busca(int pos,int last,int flag,vector<int> &N){
	
	Long ret = -INF;

	if(pos == N.size()) return 0;

	if(flag){
		for(int i = last ; i <= N[pos]; i++)
			ret = max(ret,Busca(pos+1,i,i==N[pos],N)+i*pots[pos]);		
	} else {
		for(int i = last ; i <= 9 ; i ++)
			ret = max(ret,Busca(pos+1,i,0,N)+i*pots[pos]);		
	}	

	return DP[pos][last][flag] = ret;
}

int main(){

	int T;
	string N;	
	vector<int>n;

	cin >> T ; 

	for(int caso = 1 ; caso <= T; caso++){
		cin >> N ;

		for(int i = 0 ; i <= 20 ; i ++)
			for(int j = 0 ; j <= 10 ; j ++)
				for(int k = 0 ; k <= 2 ; k++)
					DP[i][j][k] = -1;

		n = vector<int>();
		for(int i = 0 ; i < N.size() ; i ++)
			n.push_back(N[i]-'0');

		pots[N.size()-1] = 1;
		for(int i = N.size()-2 ;i >= 0 ; i--)
			pots[i] = pots[i+1]*10;

		cout << "Case #" << caso << ": " << Busca(0,0,1,n) << '\n';

	}

	return 0;
}