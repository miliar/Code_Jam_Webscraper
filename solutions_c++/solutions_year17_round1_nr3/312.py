#include <bits/stdc++.h>
typedef long long ll;

using namespace std;
int Hd,Ad,Hk,Ak,B,D;
int dp[101][101][201][101];
ll f(int h1, int h2, int a1, int a2){
	// cout << h1 << " " << h2 << " " << a1 << " " << a2 << endl;
	if(h2<=0){
		return 0;
	}
	if(h1<=0){
		return 1000010;

	}
	if(dp[h1][h2][a1][a2]!=-1){
		return dp[h1][h2][a1][a2];
	}
	ll mn=1000010;
	// attack:
	int nh2=h2-a1;
	int nh1=h1-a2;
	mn=min(mn,1+f(nh1,nh2,a1,a2));
	// buff
	if(a1<h2 && B!=0){
		mn=min(mn,1+f(nh1,h2,a1+B,a2));
	}
	//cure
	if(h1!=Hd && h1!=Hd-a2){
		mn=min(mn,1+f(Hd-a2,h2,a1,a2));
	}
	//debuff
	if(a2>0 && D!=0){
		int na2=max(0,a2-D);
		mn=min(mn,1+f(h1-na2,h2,a1,na2));
	}
	return dp[h1][h2][a1][a2]=mn;
}
void main2(){
	memset(dp,-1,sizeof(dp));
	cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
	ll ans = f(Hd,Hk,Ad,Ak);
	if(ans < 100000){
		cout << ans;
	} else {
		cout << "IMPOSSIBLE";
	}
}

int main(int argc, char const *argv[]){
	int T;
	cin >> T;
	for(int t=0;t<T;t++){
		cout << "Case #" << t+1 << ": ";
		main2();
		cout << endl;
	}
	return 0;
}