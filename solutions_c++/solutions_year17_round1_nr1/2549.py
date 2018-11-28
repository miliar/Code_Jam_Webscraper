#include<bits/stdc++.h>
#include <string>
using namespace std;

int main(){
	
	ifstream input("A-large.in");
	ofstream output;
	output.open("output_sampleALarge.out");
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
		int r;
		int c;
		stringstream ss;
     	ss<<line;
     	ss>>r;
     	ss>>c;
     	output<<"Case #";
     	output<<m;
		output<<": ";
		output<<"\n";
     	char grid[r][c];
     	for(int i=0;i<r;i++){
     		getline( input, line );
     		for(int j=0;j<c;j++){
     			grid[i][j]=line[j];
			 }
		 }	
		 char ch='-';
		 for(int i=0;i<r;i++){
     		for(int j=0;j<c;j++){
     			if(grid[i][j]>=65&&grid[i][j]<=90){
     				ch=grid[i][j];
					 for(int u=j-1;u>=0&&grid[i][u]=='?';u--){
					 	grid[i][u]=ch;
					 }	
				}
     			else if(ch!='-'){
     				grid[i][j]=ch;
				 }
			 }
			 ch='-';
		 }
		 int last=-1;
		 int count=1;
		 for(int i=0;i<r;i++){
		 	if(grid[i][0]=='?'){
		 		count++;
		 		continue;
			 }
			 else{
			 	last=i;
			 	for(int k=0;k<count;k++){
			 	for(int j=0;j<c;j++){
     				output<<grid[i][j];
				}
				output<<"\n";
				}
				count=1;
			 }
		 }
		 if(count>1){
		 	cout<<"count is "<<count<<endl;
		 for(int k=0;k<count-1;k++){
			for(int j=0;j<c;j++)
     			output<<grid[last][j];
     		output<<"\n";
		}
		}
	}				
	input.close();
	output.close();
	return 0;
}
