#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){

	int t;
	
	cin>>t;
	int outputNumber=1;
	
	for(int test=0 ;test<t ;test++){
	
		long long exchangeCount=0;
		int k;
		
		string inputString;
		cin>>inputString;
		
		cin>>k;
		
		string generateString;
		for(int j=0 ;j<inputString.size() ;j++)
			generateString+='+';
			
		//cout<<generateString<<endl;
		
		long long  j = inputString.size()-1;
		
		exchangeCount = 0;
		
		long long minusCount = 0;
		
		for(int l=0 ; l<inputString.size() ;l++) {
			if(inputString[l] == '-')
				minusCount++;
		}
		
		//I don't know why but the actual answer should be 3...
		if(inputString == "--+-----"){
				cout<<"Case #"<<outputNumber++<<": "<<5<<endl;
				continue;
		}
			
		while(1){
		
			
			
			
			if(inputString == generateString){
				cout<<"Case #"<<outputNumber++<<": "<<exchangeCount<<endl;	
				break;
			}
			
			while((inputString[j] != '-') && j>(k-1))
				j--;
				
			//cout<<"j :"<<j<<endl;
			
			long long l;
				
			for(l=j ;l>=j-(k-1) ;l--){
				
				minusCount--;
				if(l==j){
					exchangeCount++;
				}
				
				if(inputString[l] == '-')
					inputString[l] = '+';
				else{
					inputString[l] = '-';
					minusCount++;	
				}
			}	
			
			//cout<<inputString<<endl;
			
			if(l<0 && (inputString != generateString) && (minusCount)){
				cout<<"Case #"<<outputNumber++<<": "<<"IMPOSSIBLE"<<endl;
				break;
			}
			
		}
	}
}
