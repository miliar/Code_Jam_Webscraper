#include<stdio.h>
#include<iostream>
#include<fstream>
using namespace std;
int main(){
	long long t,n,a,b,c,d,count=0;
	short k;
	ifstream infile;
	ofstream outfile;
	infile.open("B-small-attempt1 (1).in");
	outfile.open("tidy_out.txt");
	infile>>t;
	cout<<t;
	while(t!=0){
		count++;
		infile>>n;
		long long tempN=0;
		while(n!=0){
		tempN=n;
		while(tempN>0){
			a=tempN%10;
			b=tempN/10;
			c=b%10;
			if(a>=c)
			 { k=1;
			 //cout<<a           ,b    ;
			 }
			 else{k=0;
			 break;
			 }
			 tempN=b;
		}	
			if(k==0){
			n--;
			}else{
				
				break;
			}
			
		}
		outfile<<"Case #"<<count<<": "<<n<<"\n";
		//cout<<n<<"\n";
		t--;
	}
}
