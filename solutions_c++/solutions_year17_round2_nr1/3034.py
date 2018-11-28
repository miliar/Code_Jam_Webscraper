#include <iostream>
#include <string>
#include <sstream>

using namespace std;

//Global variables
const int SIZE=1000;
int horses[SIZE][5];
double D;
int N;

//Function declarations
double annie();

//////////////////////////////////////////////////
int main()
{
	int i,temp,t,T;
	string NasStr;
	stringstream ss;
	
	getline(cin,NasStr);
	ss<<NasStr;
	ss>>T;
	ss.str(""); //clear the stringstream
	ss.clear();
	
  for (t=1; t<=T; t++){
  	getline(cin,NasStr,' ');
  	ss<<NasStr;
		ss>>D;
		ss.str(""); //clear the stringstream
		ss.clear();
		getline(cin,NasStr);
		ss<<NasStr;
		ss>>N;
		ss.str(""); //clear the stringstream
		ss.clear();
  	
  	for(i=0; i<N; i++) {
	  	cin>>temp;
	  	horses[i][0]=temp;
	  	cin>>temp;
	  	horses[i][1]=temp;
		}
		
		cout.precision(9);
		cout << "Case #" << t << ": " << annie() <<endl;
		
  }
  return 0;
}//end main
//////////////////////////////////////////////////


double annie(){
	int i;
	double temp, result;
	result=0;
	for(i=0; i<N; i++) {
  	temp=(D-horses[i][0])/horses[i][1];
  	if (temp>result) result = temp;
	}
	return D/result;
}








