#include<bits/stdc++.h>
#include <string>
using namespace std;

int main(){
	
	ifstream input("A-large.in");
	ofstream output;
	output.open("output_A_large.out");
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
		string a;
		int k;
		stringstream ss;
     	ss<<line;
     	ss>>a;
     	ss>>k;
     	int ans=0;
     	int flag=0;
     	for(int i=0;i<a.size();i++){
     		cout<<" i is "<<a[i];
     		if(a[i]=='+'){
     			cout<<" cont "<<endl;
     			continue;
			 }
     			
     		if(i+k>a.size()){
     			flag=1;
     			break;
			 }
			 	
     		int j=0;
     		for(;j<k;j++){
     			cout<<a[j+i]<<" ";
     			if(a[j+i]=='+')
	     			break;
			}
			int s=i+j-1;
			cout<<" j is "<<j;
			if(j==k){
				ans++;
				i=s;
				cout<<" here cont "<<endl;
				continue;
			}
			cout<<i<<endl;
			for(;j<k && a[j+i]!='\0';j++){
     			if(a[j+i]=='+')
     			a[j+i]='-';
     			else
     			a[j+i]='+';
			}
			if(j!=k){
				cout<<" flag";
				flag=1;
				break;
			}
			i=s;
			ans++;
     		
		}
		output<<"Case #";
		output<<m;
		output<<": ";
	
		if(flag==0){
			cout<<"Case #"<<m<<" ans is "<<ans<<endl;
			output<<ans;
		}
		else{
			cout<<"Case #"<<m<<"IMPOSSIBLE"<<endl;
			output<<"IMPOSSIBLE";
		}
		output<<"\n";
	
	}				
	input.close();
	output.close();
	return 0;
}
