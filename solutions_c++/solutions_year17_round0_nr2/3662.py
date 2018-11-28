#include<bits/stdc++.h>
using namespace std;
int main (){
	 freopen("test.in","r",stdin);
    freopen("count.txt","w",stdout);
	int t;
	cin>>t;
	for(int q=1;q<=t;q++){
		string str;
		cin>>str;
		for(int i=0;i<str.size()-1;i++){
			if(str[i]>str[i+1]){
			str[i]--;
			for(int j=i+1;j<str.size();j++){
				str[j]='9';
			}
			i-=2;
			}
		}
		if(str[0]=='0'){
			str.erase(0,1);
		}
		cout<<"Case #"<<q<<": "<<str<<endl;;
		
	}
}
