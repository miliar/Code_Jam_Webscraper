#include<bits/stdc++.h>
#include <string>
using namespace std;

int main(){
	
	ifstream input("A-large.in");
	ofstream output;
	output.open("output_time_large.out");
	string line;
	getline( input, line );
	long long int t,m=0;
	stringstream ss;
    ss<<line;
    ss>>t; 
    //cout<<t<<endl;
	while( getline( input, line ))
	{
		m++;
		cout<<line<<endl;
		double d;
		int n;
		stringstream ss;
     	ss<<line;
     	ss>>d;
     	ss>>n;
     	getline( input, line );
     		stringstream sss;
     		double p1,s1;
     		double t1;
     		sss<<line;
     		sss>>p1;
     		sss>>s1;
     		t1=(d-p1)/s1;
     	for(int i=1;i<n;i++){
     		getline( input, line );
     		stringstream ssss;
     		double p,s;
     		double t;
     		ssss<<line;
     		ssss>>p;
     		ssss>>s;
     		t=(d-p)/s;
     		if(t>t1){
     			t1=t;
			 }
		 }
		double speed=d/t1;
		output<<"Case #";
		output<<m;
		output<<": ";
		output<< std::fixed;
		output<<setprecision(6)<<speed;
		output<<"\n";
	
	}				
	input.close();
	output.close();
	return 0;
}
