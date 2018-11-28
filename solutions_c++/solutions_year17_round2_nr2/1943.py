#include <vector>
#include <string>
#include <fstream>    /* ifstream / ofstream */
#include <algorithm>  /* std::min */
#include <iostream>
#include <iomanip>

std::vector<size_t> tokenize_ints(const std::string& str, const std::string& delimiters = " ") {
	std::vector<size_t> retVal;
	std::string::size_type startPos = str.find_first_not_of(delimiters, 0);
	std::string::size_type endPos = str.find_first_of(delimiters, startPos);
	while (std::string::npos != startPos || std::string::npos != endPos) {
		retVal.push_back(std::stoi(str.substr(startPos, endPos - startPos)));
		startPos = str.find_first_not_of(delimiters, endPos);
		endPos = str.find_first_of(delimiters, startPos);
	}
	return retVal;
}
#include <map>
size_t getIndex(char c) {
	if (c == 'R') {
		return 0;
	}else if (c == 'O') {
		return 1;
	}else if (c == 'Y') {
		return 2;
	}else if (c == 'G') {
		return 3;
	}
	else if (c == 'B') {
		return 4;
	}
	else if (c == 'V') {
		return 5;
	}
	return 0;
}

int main(int argc, char* argv[]) {
	std::vector<std::string> args(argv, argv + argc);
	args.erase(args.begin());
	if (args.size() >= 2) {
		std::ifstream input(args.at(0));
		if (input) {
			std::string line;
			std::vector<std::string> lines;
			std::ofstream output(args.at(1));
			while (std::getline(input, line)) {
				lines.emplace_back(line);
			}
			if (lines.size() > 0) {
				size_t totalTestcases = std::stoi(lines.at(0));
				totalTestcases = std::min(totalTestcases, (lines.size() - 1));
				size_t lineNumber = 1;
				for (size_t i = 0; i < totalTestcases; i++) {
					lineNumber = i + 1;
					output << "Case #" << i + 1 << ": ";
					auto values = tokenize_ints(lines[lineNumber]);
					size_t N = values[0], R = values[1], O = values[2], Y = values[3], G = values[4], B = values[5], V = values[6];
					size_t colorNumbers = (R > 0 ? 1 : 0) + (O > 0 ? 1 : 0) + (Y > 0 ? 1 : 0) + (G > 0 ? 1 : 0) + (B > 0 ? 1 : 0) + (V > 0 ? 1 : 0);
					std::string solution;
					size_t lastIndex = 5;

					for (size_t n = 0; n < N; ++n) {

						lastIndex = (lastIndex + 1) % 6;

						size_t max = std::max(R, std::max(O, std::max(Y, std::max(G, std::max(B, V)))));
						if (R == max) {
							lastIndex = 0;
						}else if (O == max) {
							lastIndex = 1;
						}
						else if (Y == max) {
							lastIndex = 2;
						}
						else if (G == max) {
							lastIndex = 3;
						}
						else if (B == max) {
							lastIndex = 4;
						}
						else if (V == max) {
							lastIndex = 5;
						}

						size_t end = lastIndex + 6;
						for (size_t colorIndex = lastIndex; colorIndex < end; ++colorIndex) {
							if ((solution.size()>0) && (colorIndex % 6 == getIndex(solution.back()))) {
								continue;
							}
							if ((R > 0) && ((colorIndex % 6) == 0)) {
								solution.push_back('R');
								R--;
								lastIndex = colorIndex;
								break;
							}
							else if ((O > 0) && ((colorIndex % 6) == 1)) {
								solution.push_back('O');
								O--;
								lastIndex = colorIndex;
								break;
							}
							else if ((Y > 0) && ((colorIndex % 6) == 2)) {
								solution.push_back('Y');
								Y--;
								lastIndex = colorIndex;
								break;
							}
							else if ((G > 0) && ((colorIndex % 6) == 3)) {
								solution.push_back('G');
								G--;
								lastIndex = colorIndex;
								break;
							}
							else if ((B > 0) && ((colorIndex % 6) == 4)) {
								solution.push_back('B');
								B--;
								lastIndex = colorIndex;
								break;
							}
							else if ((V > 0) && ((colorIndex % 6) == 5)) {
								solution.push_back('V');
								V--;
								lastIndex = colorIndex;
								break;
							}
						}
					}
					if (solution.size() > 0) {
						if (solution.front() == solution.back()) {
							char c = solution.back();
							for (size_t i = 1; i < solution.size()-1; ++i) {
								if ((solution[i-1] != c) && (solution[i] != c)) {
									solution.insert(solution.begin() + i, c);
									solution.resize(solution.size()-1);
									c = 0;
									break;
								}
							}
							if (c != 0) {
								solution.clear();
							}
						}
					}
					

					if (solution.size() == N) {
						output << solution << std::endl;
					}
					else {
						output << "IMPOSSIBLE" << std::endl;
					}
				}
			}
		}
	}
	return EXIT_SUCCESS;
}
