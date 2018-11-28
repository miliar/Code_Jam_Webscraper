#include<iostream>
#include<vector>
#include<string>
#include<fstream>

using namespace std;


class PancakePile{
	public:
	string pile;
	int n; // number of pancakes
	int flipperSize;
	int flippedTimes = 0;
	
	PancakePile(string p, int f) : pile(p), flipperSize(f), n(p.size()){}

	

	string solve(){
		cout<<"SOLVING: "<<pile<<endl;
		for (int i = 0; i<= n-flipperSize; i++) if (pile[i]=='-'){
			flippedTimes++;
			for (int j=i; j<i+flipperSize; j++) pile[j] = (pile[j]=='+')? '-':'+';
		}
		cout<<pile<<endl;
		cout<<flippedTimes<<endl;

		for (int i = n-flipperSize-1; i<n; i++) if (pile[i]=='-') return string("IMPOSSIBLE");
		return to_string(flippedTimes);
	}

};

int main(int argc, char **argv){

	ifstream input(argv[1], ios::in);
	ofstream output;
	output.open("output", ios::out);	
	
	int T; input >> T;
	for (int t = 0; t<T; t++){
		string S; int K;
		input >> S >> K;
		PancakePile pancakePile(S,K);
		output <<"Case #"<<t+1<<": "<<pancakePile.solve()<<endl;

	}
	
	input.close();
	output.close();
}


