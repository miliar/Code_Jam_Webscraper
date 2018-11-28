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
		size_t t = 1;
        for (size_t i = 0; i < totalTestcases; i++) {
          output << "Case #" << i+1 << ": ";
          auto values = tokenize_ints(lines[t]);
		  size_t dest = values[0];
		  size_t horseCount = values[1];
		  std::map<size_t, size_t> data;
		  for (size_t j = 0; j < horseCount; j++) {
			  auto values = tokenize_ints(lines[t+j+1]);
			  data.insert(std::make_pair(values[0], values[1]));
		  }
		  t += horseCount + 1;
		  auto lastIter = data.rbegin();
		  double lastTimeUntilFinish;
		  for (auto iter = data.rbegin(); iter != data.rend(); ++iter) {
			  size_t km = (dest - iter->first);
			  double timeUntilFinish = km / (double)iter->second;
			  if (iter != lastIter) {
				  if (lastTimeUntilFinish > timeUntilFinish) {
					  timeUntilFinish = lastTimeUntilFinish;
				  }
			  }
			  lastTimeUntilFinish = timeUntilFinish;
			  
			  lastIter = iter;
		  }
		  output << std::fixed << std::setprecision(6) << dest/lastTimeUntilFinish << std::endl;
        }
      }
    }
  }
  return EXIT_SUCCESS;
}
