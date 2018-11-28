#include<iostream>
#include<vector>
#include<string>
#include<fstream>
#include<sstream>
#include<iterator>

using namespace std;


class SS{
	public:
	unsigned long long count;
	unsigned long long size;
	
	SS(unsigned long long s_, unsigned long long c_): count(c_), size(s_){
	}

};

class Bathroom{
	public:

	// Attributes
	vector<SS> stalls;
	long long users;
	unsigned long long finalL, finalR;

	// Constructor
	Bathroom(unsigned long long size, unsigned long long users_){
		stalls.push_back(SS(size,1));
		users = users_;
	}

	//
	SS biggestStall(){
		auto biggest = stalls.begin();
		for (auto it = stalls.begin(); it!=stalls.end(); it++){
			if ((*it).size > (*biggest).size){
				biggest = it;
			}

		}
		SS returnValue = *biggest;
		stalls.erase(biggest);
		return returnValue;
	}

	void add2Stalls(unsigned long long size, unsigned long long count){

		for (int i = 0; i<stalls.size(); i++) if (stalls[i].size == size){
			stalls[i].count+=count;
			return;

		}
		stalls.push_back(SS(size,count));
	
	}

	void solve(){
		while(users>0){
			SS bi = biggestStall();
			
			add2Stalls(bi.size/2,bi.count);
			add2Stalls(bi.size/2-(bi.size%2==0),bi.count);
			users-= bi.count;	
			
	
			if (users<=0){
				finalL = bi.size/2;
				finalR = bi.size/2-(bi.size%2==0);
			}
			
		}
	}

};

int main(int argc, char **argv){

	ifstream input(argv[1], ios::in);
	ofstream output;
	output.open("output", ios::out);	
	
	int T; input >> T;
	for (int t = 0; t<T; t++){
		cout<<"solving.. "<<t<<endl;
		unsigned long long N;
		unsigned long long K;
		input >> N >> K;
		Bathroom b(N,K);
		b.solve();
		output <<"Case #"<<t+1<<": "<<max(b.finalL,b.finalR)<<" "<<min(b.finalL,b.finalR)<<endl;

	}
	
	input.close();
	output.close();
}

