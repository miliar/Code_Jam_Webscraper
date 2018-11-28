#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <sstream>
#include <stdint.h>
#include <vector>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

typedef struct result{
	uint64_t y;
	uint64_t z;
} res_t;

res_t *solve(uint64_t N, uint64_t K);
uint64_t getLs(vector<int> & stalls, uint64_t loc);
uint64_t getRs(vector<int> & stalls, uint64_t loc);

template <typename T>
  string NumberToString ( T Number )
  {
     ostringstream ss;
     ss << Number;
     return ss.str();
  }



int main() {
	int T;
	uint64_t N, K;
	res_t *res;

	cin >> T;  // read t. cin knows that t is an int, so it reads it as such.
	//cout << "T:" << T <<"\n";
	for (int i = 1; i <= T; ++i) {
		cin >> N >> K;  // read n and then m.
		//decomposeInt(N);
		res = solve(N, K);
		cout << "Case #" << i << ": " << res->y << " " << res->z << endl;
		//cout << "S: " << S << " " << "K:" << K << "\n";
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
	return 0;
}

res_t *solve(uint64_t N, uint64_t K) {
	uint64_t i, j, Ls, Rs, min, max, Min, Max, loc;
	vector<int> stalls;
	res_t *res = new res_t();

	stalls.push_back(1);
	for (uint64_t i = 0; i < N; i++)
		stalls.push_back(0);
	stalls.push_back(1);

	for (uint64_t i = 0; i < K; i++) {
		// initialize for next round
		j = 0;
		while ( j < N) {
			if (stalls[j+1] == 1)
				j++;
			else
				break;
		}

		loc = j;
		Ls = getLs(stalls, loc);
		Rs = getRs(stalls, loc);
		Min = Ls > Rs ? Rs:Ls;
		Max = Ls < Rs ? Rs:Ls;

		for (uint64_t j = 0; j < N; j++) {
			if (stalls[j + 1] == 1)
				continue;
			else {
				Ls = getLs(stalls, j);
				Rs = getRs(stalls, j);
				min = Ls > Rs ? Rs:Ls;
				max = Ls < Rs ? Rs:Ls;

				if (min > Min) {
					Min = min;
					Max = max;
					loc = j;
				} else if (min == Min) {
					if (max > Max) {
						Min = min;
						Max = max;
						loc = j;
					}
				}
			}
		} 

		// fill loc with people
		stalls[loc + 1] = 1;

	}

	res->y = Max;
	res->z = Min;

	return res;
}

uint64_t getLs(vector<int> &stalls, uint64_t loc) {
	uint64_t rloc = loc;
	uint64_t Ls = 0;

	while (rloc > 0) {
		if (stalls[rloc] == 0) {
			Ls ++;
			rloc--;
		} else 
			break;
	}

	return Ls;
}

uint64_t getRs(vector<int> &stalls, uint64_t loc) {
	uint64_t rloc = loc + 2;
	uint64_t size = stalls.size();
	uint64_t Rs = 0;

	while (rloc < size) {
		if (stalls[rloc] == 0) {
			Rs ++;
			rloc++;
		} else 
			break;
	}

	return Rs;
}
