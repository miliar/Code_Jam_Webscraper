#include<iostream>
#include <fstream>
using namespace std;
bool checkString(string s){
	for(int i=0;i<s.length()-1;i++){
		if(s[i]>s[i+1]){
			return false;
		}
	}
	return true;
}
string getTidy(string s){
	int a[50] = {0};
	while(!checkString(s)){
		for(int i=s.length()-1;i>0;i--){
			if(s[i]<s[i-1]){
				if(a[i]==0){
				s[i]='9';
				a[i]=1;	
				}
				
				if(a[i-1]==0){
					int k = s[i-1]-'0';
					k--;
					s[i-1]='0'+k;
						
				}
				
			}
		}
	}
	return s;
}

int main(){
ofstream myfile;
  myfile.open ("B-small.out");
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
  	string s;
  	cin>>s;
  	string res = getTidy(s);
  	int j=0;
  	while(res[j]=='0'){
  		j++;
  	}
  	myfile<<"Case #"<<i<<": ";
  	for(int u=j;u<res.length();u++){
  		myfile<<res[u];
  	}
  	myfile<<endl;
  	
  	
  	
  	
  }

	
	myfile.close();	
}
