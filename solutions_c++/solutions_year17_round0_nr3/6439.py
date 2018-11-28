#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>
using namespace std;
typedef long long int intLL;
list<intLL> numList;
list<intLL> :: iterator p,q;
void display(){
	for(q=numList.begin();q!=numList.end();q++){
		cout<<*q<<" ";
	}
	cout<<endl;
}
int main() {
	intLL n,k;
	int test;
	int total;
	intLL max,min;
	
	cin>>test;
	total=test;
	while(test--){

		cin>>n;
		cin>>k;
	
		numList.push_back(n);
	
		for(intLL i=0;i<k;i++)
		{
			intLL TempMax=*numList.begin();
			if(TempMax%2==1){
				min=TempMax/2;
				max=TempMax/2;
			}
			else{
				max=(TempMax+1)/2;
				min=(TempMax-1)/2;
			}
		//	display();
			for(p=numList.begin();p!=numList.end();p++){
				if(*p==TempMax){
					break;
					
				}
			}
			numList.erase(p);
		//	display();
		
			numList.push_back(min);
			numList.push_back(max);
			numList.sort();
			numList.reverse();
			
		}
		cout <<"Case #"<<total-test<<": ";
		cout<<max<<" "<<min;
		cout<<endl;
		numList.clear();
	}
	return 0;
}


