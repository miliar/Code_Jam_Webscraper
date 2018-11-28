#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
	int t,T,i,j,k,count,flag;
	string s;
	ifstream in;
	ofstream out;
	
	in.open("q1l.in");
	out.open("a1.out");
	
//	cout<<"Test Cases: ";
	in>>T;
	for(t=1;t<=T;t++){
		count=flag=0;
//		cout<<"String: \n";
		in>>s;
//		cout<<"K: \n";
		in>>k;
		for(i=0;i<=s.length()-k;i++){
			if(s[i]=='-'){
				count++;
			//	cout<<i<<" "<<s<<endl;
				for(j=i;j<i+k;j++){
					s[j]=(s[j]=='+')?'-':'+';
				}
			}
		}
		
		for(j=0;j<k;j++){
			if(s[i+j]=='-'){
				flag=1;
			}
		}
		if(flag==0)
		out<<"Case #"<<t<<": "<<count<<endl;
		else
		out<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
	}
	

	return 0;
}
