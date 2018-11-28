#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using std::cout;
using std::cerr;
using std::endl;
using std::stringstream;
using std::string;
using std::vector;

// Defines the case
class Case {
public:
	Case(int number, const string& state, size_t spatula) {
		this->_number = number;
		this->_spatula = spatula;
		this->_pancakes.resize(state.size());
		this->_flips = 0;

		size_t size = state.size();
		size_t x = 0;

		for (size_t i = 0; i < size; ++i) {
			if (state[i] == '+') _pancakes[i] = true;
			else if (state[i] == '-') _pancakes[i] = false;
			else throw("Oh noes.");
		}
	};

	string to_string() {
		stringstream ss;
		for (bool p : _pancakes) {
			ss << (p ? "+" : "-");
		}
		return ss.str();
	};

	void flip(size_t n) {
		for (size_t i = n; i < n + _spatula; ++i) {
			_pancakes[i] = !_pancakes[i];
		}
		this->_flips++;
	}

	bool is_valid() {
		bool is_valid = true;
		for (size_t i = 0; i < _pancakes.size(); ++i) {
			if (!_pancakes[i]) is_valid = false;
		}
		return is_valid;
	}

	string solve() {
		for (size_t i = 0; i < (_pancakes.size() - _spatula + 1); ++i) {
			if (!_pancakes[i]) flip(i);
		}
		if (this->is_valid()) return std::to_string(_flips);
		else return "IMPOSSIBLE";
	}

	int number() { return this->_number; }

private:
	size_t _spatula;
	vector<bool> _pancakes;
	int _number;
	int _flips;
};

vector<Case> read_cases(const string& filename) {
	vector<Case> cases;
	string line;
	std::ifstream f(filename.c_str());
	std::getline(f, line);
	int count = stoi(line);

	int number = 1;
	while (std::getline(f, line)) {
		stringstream ss(line);
		string state;
		size_t size;

		ss >> state;
		ss >> size;

		cases.push_back(Case(number, state, size));
		++number;
	}
	if (count != number - 1) {
		cerr << "Loaded more cases than expected." << endl;
		exit(1);
	}
	return cases;
}

void print_solution(int number, const string& solution) {
	cout << "Case #" << number << ": " << solution << endl;
}

// =============================================================================
int main(int argc, char* argv[]) {
	// Read the problem
	string input_filename = "test.in";
	if (argc == 2) {
		input_filename = argv[1];
	}
	vector<Case> cases = read_cases(input_filename);

	// Solve the cases
	for (Case& c : cases) {
		string solution = c.solve();

		print_solution(c.number(), solution);
	}
	return 0;
}

