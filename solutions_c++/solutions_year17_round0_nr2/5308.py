#include<bits/stdc++.h>
#include <string>
using namespace std;


int main(){
	
	ifstream input("B-large.in");
	ofstream output;
	output.open("output_B_large.out");
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
		cout<<line<<" - ";
		string n=line;
		if(n.size()==1){
			cout<<n<<endl;
			output<<"Case #";
			output<<m;
			output<<": ";
			output<<n;
			output<<"\n";
			continue;
		}
		string ans="";
		int i=0;
		int index=0;
		for(;i<n.size()-1;i++){
			int a=n[i]-48;
			int b=n[i+1]-48;
			if(a>b){
				for(;i>0 && n[i]==n[i-1];i--){	
				}
				index=i;
				break;
			}
		}
		
		if(i==n.size()-1){
			cout<<n<<endl;
			output<<"Case #";
		output<<m;
		output<<": ";
		output<<n;
		output<<"\n";
		continue;
		}
		
		for(int j=0;j<index;j++)
			ans=ans+n[j];
		
		ans=ans+(char)(n[index]-1);
		
		for(i=index+1;i<n.size();i++)
			ans=ans+"9";
		
		stringstream s;
		s<<ans;
		long long int kk;
		s>>kk;
		
		cout<<kk<<endl;
     	
		output<<"Case #";
		output<<m;
		output<<": ";
		output<<kk;
		output<<"\n";
	
	}				
	input.close();
	output.close();
	return 0;
}
