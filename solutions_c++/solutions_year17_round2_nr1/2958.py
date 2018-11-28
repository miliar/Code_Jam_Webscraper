#include<iostream> 
#include<vector> 
#include<fstream>

#include<iomanip>

// max_element
#include<algorithm>

using namespace std;

int main(int argc, char** argv) {

        ifstream my_file;
        my_file.open(argv[1]);

	vector<float> Ki, Si, Ti;

	int T, D, N;
	my_file >> T;

	int cas = 1;

	while(my_file >> D >> N) {

		Ti.clear();
		/*Ki.clear();
		Si.clear();*/

		for(int i = 0; i < N; i++) {

			int K, S;
			my_file >> K >> S;

			/*Ki.push_back(K);
			Si.push_back(S);*/
			Ti.push_back((float)(D-K)/S);

		}

		float m = *max_element(Ti.begin(), Ti.end());
                 
		cout << "Case #" << cas << ": " << setprecision(20) << (float)D / m << endl;
		cas++;

	}

        my_file.close();

        return 0;

}
