#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

bool isTidy(vector<int> numbers){


	for(int i=0 ;i<numbers.size()-1 ;i++){
		//cout<<numbers[i]<<" "<<numbers[i+1]<<endl;
		if(!(numbers[i] >= numbers[i+1]))
			return false;
	}
	
return true;
}

int main() {

	long t;
	
	cin>>t;
	long caseNumber=1;
	
	for(int test = 0;test < t ;test++) {
	
		long long number;
		
		cin>>number;
		
		
		
		while(number>=0){
			
			vector<int> array;
			long long k = number;
			
			//cout<<k<<endl;
			while(k!=0){
				array.push_back(k%10);
				k/=10;
			}
		
			if(isTidy(array)){
				cout<<"Case #"<<caseNumber++<<": "<<number<<endl;
				break;
			}	
			else{
				number--;
			}
		}
	}

}
