

#include <iostream>
#include <set> 
#include <iterator>
using namespace std;
int tidy(int k){
	int res=1;
	int temp=k;
	while (k>0 && res==1){
		if (k%10<(k/10)%10) res=0;
		k=k/10;
	//	cout << k<<endl;
		}
	return res;
	}


int main()
{ int k,T;
string q;
//cout << "enter";
 cin >> T;
 for (int i=0;i<T;i++){
 	cin >> k; 
 	while (tidy(k)==0) k=k-1;
	cout << "Case #"<<i+1<<": "<<k<<endl;

 }



  return 0 ;}
  
  
