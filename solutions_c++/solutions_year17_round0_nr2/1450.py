#include <iostream>
#include <vector>

void printv(std::vector<int> out) {
	auto it = out.begin();
	while(*it == 0) { it++; }
	for(; it < out.end(); it++) {
		std::cout << (*it);
	}
}

void handle_case() {
	std::vector<int> out;
	int fehlstelle = -1;
	std::string in;
	std::cin >> in;
	for(char c: in) {
		if(out.size() == 0) {
			out.push_back(c-'0');
			continue;
		}
		
		if(fehlstelle >= 0) {
			out.push_back(9);
		} else if(out.back() <= c - '0') {
			out.push_back(c - '0');
		} else {
			fehlstelle = out.size()-1;
			out[fehlstelle] -= 1;
			out.push_back(9);
		}
	}
	while(fehlstelle > 0 && (out[fehlstelle] < out[fehlstelle-1])) {
		out[fehlstelle] = 9;
		fehlstelle--;
		out[fehlstelle] -= 1;
	}
	if(out.size() == 0){
		return;
	}
	printv(out);
}


int main() {
	int num_cases;
	std::cin >> num_cases;
	for(int tcase = 1; tcase <= num_cases; tcase++) {
		std::cout << "Case #" << tcase << ": ";
		handle_case();
		std::cout << std::endl;
	}
}
