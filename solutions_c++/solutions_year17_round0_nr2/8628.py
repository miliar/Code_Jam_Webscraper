#include <iostream>
#include <fstream>
using namespace std;

bool checkTidy(int n){
	int a,b;
	while (n>0){
		a = n%10;
		n = n/10;
		b = n%10;
		if (a<b) 
			return false;
	}
	return true;
}

int main(){
	ofstream myfile;
  	myfile.open ("out1.txt");
  	int n,m;
  	cin >> n;
  	for (int i=0; i<n; i++){
  		cin >> m;
  		while ((!checkTidy(m))&&(m>0))
  			m--;
  		myfile << "Case #" << i+1 << ": " << m << endl;
  	}
  	myfile.close();
  	return 0;
}