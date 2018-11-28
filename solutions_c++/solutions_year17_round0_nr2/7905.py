#include<bits/stdc++.h>

using namespace std;

int main(){
	int t,i,j,l;
	string str;
	freopen("q1.in","r",stdin);
	freopen("q1.out","w",stdout);
	cin>>t;
	for(int x=1;x<=t;x++){
		cin>>str;
		l=str.length();
		for(i=l-1;i>0;i--){
			if(str[i-1]>str[i]){
				str[i-1]--;
				for(j=i;j<l;j++){
					str[j]='9';
				}
			}
		}
		i=0;
		while(str[i]=='0') i++;
		cout<<"Case #"<<x<<": "<<str.substr(i)<<endl;
	}
	return 0;
}