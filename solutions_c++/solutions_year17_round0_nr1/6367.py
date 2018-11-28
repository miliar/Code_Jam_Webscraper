#include <iostream>
#include <fstream>
using namespace std;

ifstream in;
ofstream out;

int main()
{
	in.open("A-large.in");
	out.open("output.txt");
	int t;
	in>>t;
	for (int tt=1; tt<=t; tt++){
		string A;
		int K, cnt=0;
		in>>A;
		in>>K;
		for (int i=0; i<=A.length()-K; i++){
			if (A[i]=='-'){
				for (int j=i; j<i+K; j++){
					if (A[j]=='-') A[j]='+';
					else A[j]='-';
				}
				cnt++;
			}
		}
		int flag=0;
		for (int i=A.length()-K+1; i<A.length(); i++){
			if (A[i]=='-'){
				flag=1;
				break;
			}
		}
		out<<"Case #"<<tt<<": ";
		if (flag==1) out<<"IMPOSSIBLE"<<endl;
		else out<<cnt<<endl;
	}
	
	return 0;
}
