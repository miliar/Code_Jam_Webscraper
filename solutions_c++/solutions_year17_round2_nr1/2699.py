#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	int numCases;
	int i, j, k, size;
	double vel[1000], s0[1000], dist, sol, last;
	
	cin>>numCases;
	
	for(i=0;i<numCases;i++){
		cin>> dist;
		cin>> size;
		
		cin>>s0[0];
		cin>>vel[0];
		sol = (vel[0]/(dist-s0[0]))*dist;
		for(j = 1; j<size; j++){
			cin>>s0[j];
			cin>>vel[j];
			last = (vel[j]/(dist-s0[j]))*dist;
			if(last<sol){
				sol = last;
			}
		}
		printf("Case #%d: ", i+1);
		std::cout << std::setprecision (18) << sol << std::endl;
	}
	
	return 0;
}
