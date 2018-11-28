
#include <iostream>
#include <string>
using namespace std;


bool checkIt(long long x){
	string s=to_string(x);
	bool result=true;
	for(int i=0;i<s.length()-1;i++){
		if(s[i]>s[i+1]){ result=false;}
	}
	return result;
}

int main(){
	int t;cin>>t;
	for(int z=1;z<=t;z++){
		long long num;cin>>num;
		string s=to_string(num);
		int tries=0;			
		if(s.length()>1){
			bool done = false;
			while(!done){
				bool nice=true;
				int i=0;
				for(;i<s.length()-1;i++){
					if(s[i]>s[i+1]){ nice=false;break; }
				}
				if(!nice) {
					long long subtract=stoll(s.substr(i+1));
					if(checkIt(num))
					{
						done=true;
					}
					else{
						num=num-(subtract+1);
						s=to_string(num);
					}
				}
				else {done=true;}
			}
		}
		
		tries++;
		
		cout<<"Case #"<<z<<": "<<num<<endl; 	
	}
	return 0;
}