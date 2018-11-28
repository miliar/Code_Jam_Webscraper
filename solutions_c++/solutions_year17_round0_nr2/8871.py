#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <sstream>
#include <set>
#include <cstring>
#include <vector>
#include <map>
#include <cassert>
#include <cmath>
using namespace std;
string s;

typedef long long lli;
int t;
const int MAXN = 20;
const int MAXM = 2;
lli pot10[21];
lli memo[20][2][20];
 
lli dp(int pos,bool menor,int minimo){
	if( pos == -1 ) return 0ll;
	if( memo[pos][menor][minimo] != -1ll )return memo[pos][menor][minimo];

	long long dev=-1LL<<60;
	//cout << pos << " " << menor << " " << minimo << endl;
	if(menor){
		for(int i=minimo;i<=9;i++)
			dev = max(dev, i*pot10[pos] +  dp(pos-1, menor , i));
	}else{
		//Si pongo un digito menor al digito  en analisis entonces ya estare formando un numero menor bool menor=1
		for(int i = minimo; i < (s[pos]-'0') ; i++)
			dev = max( dev, i*pot10[pos] +  dp(pos-1 , 1, i) );
		//colocamos el mismo digito que el de analisis S  bool menor=0 se mantiene.
		if( (s[pos]-'0') >= minimo )
			dev = max( dev, (s[pos]-'0')*pot10[pos] + dp(pos-1, menor , s[pos]-'0'));
	}
 
	memo[pos][menor][minimo] = dev;
	return dev;
}

void limpia(){
	for( int i = 0; i < MAXN; i++ )
		for( int j = 0; j < MAXM; j++ )
			for( int k = 0; k < MAXN; k++ )
				memo[i][j][k] = -1;
}
 
int main(){
	cin.tie(0);
	ios_base::sync_with_stdio(0);

	int T;
	pot10[0]=1;
	for(int i=1; i<=20 ; i++) pot10[i] = pot10[i-1]*10;
 
	cin >> T;
	for( int casos = 1; casos <= T; casos++ ){
		cout << "Case #"<< casos <<": ";
		cin >> s;
		reverse( s.begin(), s.end() );
		t = s.size();
 
		limpia();

		cout << dp( t-1, false, 0 ) << '\n';
	}
 
	return 0;
}