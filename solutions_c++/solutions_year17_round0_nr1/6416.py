#include <vector>
#include <string>
#include <fstream>    /* ifstream / ofstream */
#include <algorithm>  /* std::min */

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

          std::string str = lines.at(t).substr(0, lines.at(t).find(" "));
          size_t k = std::stoi(lines.at(t).substr(lines.at(t).find(" ") + 1, std::string::npos));

          int operations = 0;
          bool flag = false;
          for (size_t i = 0; i < str.size(); ++i) {
            if (str[i] == '-') {
              operations++;
              for (size_t j = 0; j < k; ++j) {
                if (i + j < str.size()) {
                  if (str[i + j] == '-') {
                    str[i + j] = '+';
                  }
                  else {
                    str[i + j] = '-';
                  }
                }else {
                  flag = true;
                }
              }
            }
          }

          if ((str.find('-') != std::string::npos) || (flag)) {
            output << "IMPOSSIBLE";
          }
          else {
            output << operations;
          }

          output << std::endl;
          /* TODO: write your code here :-) */
        }
      }
    }
  }
  return EXIT_SUCCESS;
}
