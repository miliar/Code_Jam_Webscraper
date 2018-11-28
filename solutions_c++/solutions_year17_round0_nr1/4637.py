#include <iostream>
#include <string>

using namespace std;

bool all_done(string s){
	for(int i=0; i<s.size(); i++){
		if(s[i]=='-'){
			return false;
		}
	}
	return true;
}

int main(){
	int t;
	cin>>t;
	int iter=t;
	int* res= new int[t];
	while(t--){
		string s;
		cin>>s;
		int k;
		int len=s.size();
		cin>>k;
		int count=0;
		for(int i=0;i<len-k+1;i++){
			if(s[i]=='-'){
				count++;
				for(int j=i; j<i+k;j++){
					if(s[j]=='-'){
						s[j]='+';
					}
					else{
						s[j]='-';
					}
				}
			}
		}
		if(all_done(s)){
			res[t]=count;
		}
		else {
			res[t]=-1;
		}

	}
	int i=1;
	while (iter--){
		if(res[iter]>=0){
			cout<<"Case #"<<i<<": "<<res[iter]<<endl;
			i++;
		}
		else{
			cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
			i++;
		} 
	}
	delete[] res;
	return 0;
}