#include <iostream>
#include <fstream>

using namespace std;

int processStack(bool vals[], int count, int minFlip);

int main(int argc, char **argv){
	ifstream in(argv[1]);
	ofstream out("a.out");
	int num;
	in>>num;

	bool vals[1100];
	for(int i=0;i<num;i++){
		string word;
		int minFlips;
		in>>word>>minFlips;


		for(int i=0;i<word.length();i++){
			vals[i]=word[i]=='+';
			cout<<vals[i]<<" ";
		}
		cout<<endl;

		int flips=processStack(vals, word.length(), minFlips);

		out<<"Case #"<<(i+1)<<": ";
		if(flips==-1){
			out<<"IMPOSSIBLE"<<endl;
		}else{
			out<<flips<<endl;
		}
	}

	in.close();
	out.close();
}

int processStack(bool vals[], int count, int flips){
	int minFlips=0;
	for(int i=0;i<count-flips+1;i++){
		if(!vals[i]){
			cout<<i<<endl;
			minFlips++;
			for(int j=0;j<flips;j++){
				vals[i+j]=!vals[i+j];
			}
		}
	}

	for(int i=count-flips;i<count;i++){
		if(!vals[i])
			return -1;
	}

	return minFlips;
}