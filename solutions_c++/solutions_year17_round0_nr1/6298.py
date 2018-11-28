#include<bits/stdc++.h>
using namespace std;

int getNumBits(int x){
	return __builtin_popcount(x);
}

int main(){

	

	ios_base::sync_with_stdio(false); cin.tie(NULL);
	int tc;
	cin>>tc;

	for(int i=1;i<=tc;i++){
		string s;
		int n;
		cin>>s>>n;
		int counter=0;
		int len = s.length();
		for(int j=0;j<len;j++){
			if(s[j]=='-'){
				int k;
				for(k=j;k<=j+n-1 && k<len;k++){
					if(s[k]=='-')s[k]='+';
					else s[k]='-';
				}
				if(j+n > len) s[0]='-';
				counter++;
			}
		}
		int x=0;
		
		for(int j=0;j<len;j++){
			if(s[j]=='+'){
				x++;
			}
		}
		cout<<"Case #"<<i<<": ";
		if(x==len) cout<<counter<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
