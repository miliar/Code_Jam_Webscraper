#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll n;
string S;
int u, t=1, l, i;
ll pow(int e){
	if(e==0)	return 1;
	ll res=pow(e/2);
	return res*res*((e%2==1)?10:1);
}
int main(){
	for(cin>>u; t<=u; t++){
		cin>>n;
		S=to_string(n);
		l=(int)S.size();
		for(i=l-1; i>0; i--)
			if(S[i]<S[i-1]){
				n-=n%pow(l-i)+1;
				S=to_string(n);
			}
		cout<<"Case #"<<t<<": "<<S<<endl;
	}
	return 0;
}
