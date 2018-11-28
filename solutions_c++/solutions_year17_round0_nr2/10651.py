#include<bits/stdc++.h>
using namespace std;
bool checkfunc(int x){
	while(x>0){
		if((((x%100)-(x%10))/10)>(x%10))
			return false;
		x/=10;
	}
	return true;
}
int main(){
	//freopen("input","r",stdin);
	//freopen("output","w",stdin);
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t,x;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>x;
		while(!checkfunc(x))
			x--;
		cout<<"Case #"<<i<<": "<<x<<"\n";
	}
	return 0;
}
