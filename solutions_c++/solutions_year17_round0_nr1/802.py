#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
string s="";

int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	
	
	int caso,k;
	cin>>caso;
	
	for(int testcases=1;testcases<=caso;testcases++){
		cout<<"Case #"<<testcases<<": ";
		cin>>s;
		cin>>k;
		int cont=0;
		
		for(int i=0;i+k-1<s.size();i++){
			if(s[i]=='-'){
				cont++;
				for(int j=i;j<i+k;j++){
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}		
			}		
		}
		
		if(s==string(s.size(),'+')){
			cout<<cont<<endl;
		}else{
			cout<<"IMPOSSIBLE"<<endl;
		}
		
	}
	
	
	
	return 0;
}
