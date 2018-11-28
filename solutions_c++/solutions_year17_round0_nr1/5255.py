#include <bits/stdc++.h>
using namespace std;

int main(){
    int T,I;
    cin>>T;
    for(I=0;I<T;I++){
    	string input;
    	int K;
    	cin>>input>>K;
    	int i,j,answer=0;
    	for(i=0;i<=input.size()-K;i++){
    		if(input.at(i)=='-'){
    			answer++;
    			for(j=i;j<i+K;j++){
    				if(input.at(j)=='-'){
    					input.at(j)='+';
    				}else{
    					input.at(j)='-';
    				}
    			}
    		}
    	}
    	bool checker=true;
    	for(i=input.size()-K+1;i<input.size();i++){
    		if(input.at(i)=='-'){
    			checker=false;
    			break;
    		}
    	}
    	cout<<"Case #"<<I+1<<": ";
    	if(checker==true){
    		cout<<answer<<endl;
    	}else{
    		cout<<"IMPOSSIBLE"<<endl;
    	}
    }
    return 0;
}
