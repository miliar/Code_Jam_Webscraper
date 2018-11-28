#include <iostream>
#include <fstream>
using namespace std;

ifstream in;
ofstream out;

int main()
{
	in.open("B-large.in");
	out.open("output.txt");
	int t;
	in>>t;
	for (int tt=1; tt<=t; tt++){
		string A;
		in>>A;
		for (int i=1; i<A.length(); i++){
			if (A[i-1]>A[i]){
				for (int j=i-1; j>=0; j--){
					if (j==0){
						A[j]--;
						break;
					}
					if (A[j-1]==A[j]){
						A[j]='9';
						if (j==1){
							A[0]--;
							break;
						}
					}
					else{
						A[j]--;
						break;
					}
				}
				for (;i<A.length(); i++) A[i]='9';
			}
		}
		out<<"Case #"<<tt<<": ";
		int k=0;
		if (A[0]=='0') k++;
		for (int i=k; i<A.length(); i++) out<<A[i];
		out<<endl;
	}
	
	return 0;
}
