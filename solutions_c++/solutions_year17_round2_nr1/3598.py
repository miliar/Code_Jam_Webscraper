#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iomanip>

using namespace std;

long double n[1000][2];

long double best;

int main( int argc, char** argv){


ofstream output;
ifstream input;
cout<< " start "<<endl;
input.open(argv[1]);
output.open("ans.txt");


if(input.fail()){
  cout<<" error opening file"<<endl;
  return -1;
}


int cases;
input >> cases;

long double temp =0;

long double D;
long double N;


for(int i=0; i< cases ; i++){


input >> D >> N;

cout<<"case "<<i+1<<" "<<D<<" "<<N<<endl;


for( int j=0 ; j<N; j++){
	input >> n[j][0] >> n[j][1];
	cout<< n[j][0] << " "<<  n[j][1] <<endl;
}


best = LONG_MAX ;
temp =0;
for( int j=0 ; j<N; j++){
	temp = (D-n[j][0])/n[j][1];
//	cout<<temp<<endl;
	temp = D/temp;	
	if ( temp < best )
	       best = temp;	
}

long double speed=0;
long double dis=0;

for( int j=0 ; j<N; j++){
	speed = best-n[j][1];
	if( speed < 0 )
		continue;
	dis = (n[j][0]/speed)*best;	
	if ( dis < D )
		cout<<" !!!!! oh oh "<<D<<" "<<dis<<endl;
}

output<<"Case #"<<i+1<<": "<<fixed<<setprecision(6)<<best<<endl;  
cout<<"Case #"<<i+1<<": "<<fixed<<setprecision(6)<<best<<endl;  

}

input.close();
output.close();
return 0;
}
