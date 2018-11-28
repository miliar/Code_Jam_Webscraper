#include <iostream>
#include <fstream>
#include <deque>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int cases;
	ofstream output("output.txt");
	ifstream input("input.in");
	input >> cases;
	for (int cas = 0; cas < cases; cas++){
		int N, K;
		input >> N;
		input >> K;
		deque<int> pipe;
		pipe.push_front(N);
		int nextsort = 1;
		for (int i = 0; i < K; i++){
			if (i == nextsort){
				sort(pipe.begin(), pipe.end());
				reverse(pipe.begin(), pipe.end());
				nextsort *= 2;
			}
			pipe.push_back(pipe.front() / 2);
			pipe.push_back((pipe.front() - 1) / 2);
			pipe.pop_front();
		}
		int low = pipe.back();
		pipe.pop_back();
		int high = pipe.back();
		output << "Case #" << cas + 1 << ": " << high << " " << low << endl;


		/*
		int low = 0;
		int high = 0;
		if (K == 1){
			high = N / 2;
			low = N - high - 1;
		}
		else{
			low = (N - K)/4;
			high = (N - K + 2) / 4;
		}
		output << "Case #" << cas + 1 << ": " << high << " " <<  low << endl;
		*/
	}
	return 0;
}

