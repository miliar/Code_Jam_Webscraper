#include<bits/stdc++.h>
using namespace std;
#define sl(n) scanf("%lld",&n)
#define debug(n) printf("%lld\n",n)
typedef long long int ll;
//#define INPUT
ll l;
string s;
bool check(){
	ll i;
	for(i=(l-2);i>=0;i--){
		if(s[i]>s[i+1]){
			return false;
		}
	}
	return true;
}
void correct(){
	ll i,j; 
	for(i=(l-2);i>=0;i--){
		if(s[i]>s[i+1]){
			s[i]--;
			for(j=i+1;j<l;j++)
			s[j]='9';
		}
	}
}
int main(){
	#ifdef INPUT
       freopen("input.cpp", "r", stdin);
       freopen("output.cpp", "w", stdout);
   	#endif
   	ll z;sl(z);
   	for(ll t=1;t<=z;t++){
   		cin>>s;
   		l = s.length();
   		while(!check()){
   			correct();
   		}
   		ll p,i;
   		for(i=0;i<l;i++){
   			if(s[i]!='0'){
   				p=i;
   				break;
   			}
   		}
   		cout<<"Case #"<<t<<": "<<s.substr(p)<<endl;
   	}
}
