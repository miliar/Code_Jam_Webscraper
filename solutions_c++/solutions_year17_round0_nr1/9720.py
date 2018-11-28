#include<iostream>
#include<string.h>
using namespace std;
int main(){
	int t,k,g;
	string s;
	cin>>t;
	for(int i=1;i<=t;i++){
		g=0;
		cin>>s>>k;
		for(int h=0;h<s.size();h++){
			if(s[h]=='-'){
				if(h+k-1<s.size()){
					g++;
					for(int f=0;f<k;f++){
						if(s[h+f]=='-')
							s[h+f]='+';
						else
							s[h+f]='-';
					}
				}
			}
		}
		bool ok=true;
		for(int h=0;h<s.size();h++)
			if(s[h]=='-')
				ok=false;
		if(ok){
			cout<<"Case #"<<i<<": "<<g<<endl;
		}
		else{
			cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
		}
	}
}
