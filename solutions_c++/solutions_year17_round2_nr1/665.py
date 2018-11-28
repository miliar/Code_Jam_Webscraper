#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <complex>
#include <iomanip>  
// #include <gmpxx.h>
//g++ mycxxprog.cc -lgmpxx -lgmp

using namespace std;


int main(){
	int nb;
	cin >>nb;
	for(int cases=0; cases<nb; cases++){
    cout << "Case #"<<cases+1<<": ";
    double N, D;
    cin>> D>>N;
    double t=0;
    for(int i=0;i<N;i++){
      double K,S;
      cin >> K>>S;
      t = max(t, (D-K)/S);
    }
    ;
  cout <<fixed<<setprecision(6)<< D/t<<endl;
  }
	return 0;
}
