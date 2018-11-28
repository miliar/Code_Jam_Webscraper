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
	Case(int number, string n) {
		this->_number = number;

		for (char c : n) {
			_ns.push_back(c - '0');
		}
	};

	string solve() {
		for (size_t i = _ns.size() - 1; i > 0; --i) {
			if (_ns[i] < _ns[i -1] || _ns[i] == 0) {
				for (int j= i; j < _ns.size(); ++j) {
					_ns[j] = 9;
				}
				_ns[i - 1] = _ns[i - 1] - 1;
			}
		}
		return this->to_string();
	}

	string to_string() {
		stringstream ss;
		bool found_non_zero = false;
		for (int n : _ns) {
			if (n != 0) found_non_zero = true;
			if (found_non_zero) ss << n;
		}
		return ss.str();
	}

	int number() { return this->_number; }

private:
	int _number;
	vector<int> _ns;
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
		string n;

		ss >> n;

		cases.push_back(Case(number, n));
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

