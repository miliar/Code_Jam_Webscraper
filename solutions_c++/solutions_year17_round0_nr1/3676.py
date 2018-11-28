#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
	ll t,k,c=0,flip;
	cin>>t;
	string s;
	while(t--){
		int flag=1;
		flip=0;
		c++;
		cin>>s>>k;
		ll arr[s.length()]={0};
		for(ll i=0;i<=s.length()-k;i++){
			if((arr[i]%2==0 && s[i]=='-') || (arr[i]%2==1 && s[i]=='+')){
				flip++;
				for(ll j=0;j<k;j++){
					arr[j+i]++;
				}
			}
		}
		for(ll i =s.length()-k+1;i<s.length();i++){
			if((arr[i]%2==0 && s[i]=='-') || (arr[i]%2==1 && s[i]=='+')){
				cout<<"Case #"<<c<<": IMPOSSIBLE"<<endl;
				flag=0;
				break;
			}
		}
		if(flag==1)
			cout<<"Case #"<<c<<": "<<flip<<endl;
	}
	return 0;
}