#include<iostream>
#include<string>
using namespace std;
int main(){	
	int T;
	cin>>T;
	int c=0;
	while(T--){
		string s;
		cin>>s;
		int steps=0;
		int K;
		cin>>K;
		for(int i=0;s[i+K]!='\0';i++){
			if(s[i]=='-'){
				for(int j=0;j<K;j++){
					if(s[j+i]=='-')
						s[j+i]='+';
					else
						s[j+i]='-';
				}
				steps++;
			}
		}
				
		c++;	
		int minuses=0;
		cout<<"Case #"<<c<<": ";
		for(int i=0;s[i]!='\0';i++)
			if(s[i]=='-')
				minuses++;
		if(minuses==0)
			cout<<steps;
		else if(minuses==K)
			cout<<steps+1;
		else
			cout<<"IMPOSSIBLE";
		cout<<endl;
	}
	return 0;
}
