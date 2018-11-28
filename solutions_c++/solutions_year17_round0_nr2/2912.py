#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

#define ULL unsigned long long

using namespace std;

ULL from_vec(const vector<int> & v) {
	ULL acc = 0;
	for (unsigned int i = 0; i < v.size(); i++) {
		acc *= 10;
		acc += v[i];
	}
	return acc;
}

vector<int>& to_vec(ULL n) {
	vector<int> *v = new vector<int>();
	while (n > 0) {
		v->push_back(n % 10);
		n = n/10;
	} 
	reverse(v->begin(),v->end());
	return *v;
}

vector<int>& put_nines(vector<int>& v, unsigned int from) {
	while(from < v.size()) {
		v[from] = 9;
		from++;
	}
	return v;
}

bool is_tidy(const vector<int>& v) {
	if (v.size() < 2) return true;
	for (unsigned int i = 0; i< v.size()-1;i++) {
		if (v[i] > v[i+1]) {
			return false;
		}
	}
	return true;
}

vector<int> & tidy_vec(vector<int>& v) {
	if (is_tidy(v)) return v;
	for (unsigned int i = 0; i< v.size()-1;i++) {
		if (v[i] > v[i+1]) {
			v[i] = v[i] - 1;
			v = put_nines(v,i+1);
			break;
		}
	}
	return tidy_vec(v);
}

ULL getTidy(ULL n) {
	vector<int> v = to_vec(n);
	return from_vec(tidy_vec(v));
}

int main(int argc, char **argv) {
	int t;
	ifstream input;
	ofstream output;
	
	input.open("B-large.in");
	output.open("out.txt");
	input >> t;
	for (int i = 1;i<=t;i++) {
		ULL n;
		input >> n;
		output << "Case #" << i << ": ";
		output << getTidy(n);
		output << endl;
	
	}
    input.close();
	output.close();
	return 0;
}
