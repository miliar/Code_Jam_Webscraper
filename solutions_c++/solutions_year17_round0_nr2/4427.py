#include<bits/stdc++.h>
using namespace std;
bool isinc(string num){
	int i=0;
	while(num[i]=='0'){
		i++;
	}
	for(;i<num.size()-1;i++){
		if(num[i]>num[i+1])return false;
	}
	return true;
}
string makeright(string num){
	int i=0;
	while(num[i]=='0'){
		i++;
	}
	for(;i<num.size()-1;i++){
		if(num[i]>num[i+1]){
			num[i]=num[i]-1;
			for(int j=i+1;j<num.size();j++){
				num[j]='9';
			}
		}
	}
	return num;

}
int main(){
	int T;
	cin>>T;
	for(int index=0;index<T;index++){
		string N;
		cin>>N;
		while(!isinc(N)){
			N=makeright(N);
		}
		int i=0;
		while(N[i]=='0'){
			i++;
		}
		cout<<"Case #"<<index+1<<": ";

		for(;i<N.size();i++){
			cout<<N[i];
		}
		cout<<endl;
        
	}
	return 0;
}
