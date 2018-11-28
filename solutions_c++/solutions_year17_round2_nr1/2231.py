#include<iostream>
#include <stdio.h>
using namespace std;
int main(){
	freopen ("output.txt","w",stdout);
	freopen ("A-large.in","r",stdin);
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		int d,n;
		cin>>d>>n;
		int k[n],s[n];
		for(int j=0;j<n;j++){
			cin>>k[j]>>s[j];
		}
		double mint=(d-k[0])/double(s[0]);
		for(int j=1;j<n;j++){
			if(((d-k[j])/double(s[j]))>mint){
			mint=((d-k[j])/double(s[j]));		
			}
		}	
		cout<<"Case #"<<i+1<<": ";
		printf ("%.10f", d/mint);
		cout<<endl;
	}

	return 0;	
}
