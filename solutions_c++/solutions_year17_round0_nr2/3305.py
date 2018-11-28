#include <iostream>
#include <fstream>

using namespace std;

long long process(string num);

int main(int argc, char **argv){
	ifstream in(argv[1]);
	ofstream out("b.out");
	int num;
	in>>num;

	for(int i=0;i<num;i++){
		string word;
		in>>word;;

		out<<"Case #"<<(i+1)<<": "<<process(word)<<endl;
	}

	in.close();
	out.close();
}

long long process(string num){
	for(int i=num.length()-1;i>0;i--){
		if(num[i]<num[i-1]){
			num[i]='9';
			int j;
			for(j=i;j<num.length();j++)
				num[j]='9';
			for(j=i-1;num[j]==0;j--){
				num[j]='9';
			}
			num[j]-=1;
			i=num.length()-1;
		}
	}
	cout<<num<<endl<<atol(num.c_str())<<endl;
	return atoll(num.c_str());
}