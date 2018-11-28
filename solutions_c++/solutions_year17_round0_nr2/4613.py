#include <iostream>
#include <string>
using namespace std;

bool not_tidy(string str){
	for (int i=0; i<str.size()-1;i++){
		if(str[i]>str[i+1]) 
			return true;
	}
	return false;
}



int main(){
	int t;
	cin>>t;
	int iter=t;
	string res[t];
	while(t--){
		string s;
		cin>>s;
		if(s.size()==1){
			res[t]=s;
		}
		else {
			while(not_tidy(s)){
				for(int i=0; i<s.size()-1; i++){
					if(s[i]>s[i+1]){
						s[i]=s[i]-1;
						for(int j=i+1;j<s.size();j++){
							s[j]='9';
						}
					}
					//break;
				}
			}
		}
		int temp=0;
		for(int i=0; i<s.size();i++){
			if(s[i]!='0') {
				temp=i;
				break; 
			}
		}
		res[t]=s.substr(temp);

	}
	int i=1;
	while (iter--){
		cout<<"Case #"<<i<<": "<<res[iter]<<endl;
		i++;
	}
	return 0;
}

