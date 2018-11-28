#include <vector>
#include <string>
#include <fstream>    /* ifstream / ofstream */
#include <algorithm>  /* std::min */
#include <iostream>
bool has_prefix(const std::string &str, const std::string &prefix) {
  return str.size() >= prefix.size() && str.compare(0, prefix.size(), prefix) == 0;
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
        for (size_t i = 0; i < totalTestcases; i++) {
          size_t t = i + 1;
          output << "Case #" << t << ": ";
          for (size_t index = 0; index < lines[t].size();++index) {
            if ((index >= 1) && (lines[t][index] < lines[t][index-1])) {
              int backIndex = index - 1;
              while ((backIndex >= 1) && (lines[t][backIndex] == lines[t][backIndex -1]) ) {
                --backIndex;
              }
              backIndex = std::max(0, backIndex);
              lines[t][backIndex] = lines[t][backIndex] - 1;
              for (size_t newIndex = backIndex + 1; newIndex < lines[t].size(); ++newIndex) {
                lines[t][newIndex] = '9';
              }
              if (has_prefix(lines[t], "0")) {
                lines[t] = lines[t].substr(lines[t].find_first_not_of("0"), std::string::npos);
              }
              break;
            }
            
          }
          output << lines[t];
          output << std::endl;
        }
      }
    }
  }
  return EXIT_SUCCESS;
}
