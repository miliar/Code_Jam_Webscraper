#include <iostream>
#include <fstream>
#include <bitset>

int check_tidy(std::string line) {
    char last = line[line.size() - 1];
    for (int j = (int)line.size() - 2; j >= 0; --j) {
        if (line[j] <= last) {
            last = line[j];
        } else {
            return j;
        }
    }

    return -1;
}

int main() {
    std::ifstream in("B-large.in");
    std::ofstream out("out.txt");
    int num_samples = 0;
    in >> num_samples;
    for (int i = 1; i <= num_samples; ++i) {
        out << "Case #" << i << ": ";

        std::string line = "";
        in >> line;

        // Recursive check tidy
        int tail = 0;
        int mark;
        while (line.size() > 1 && (mark = check_tidy(line)) != -1) {
            tail += (line.size() - mark - 1);
            line[mark]--;
            line = line.substr(0, (unsigned long) mark + 1);
        }

        // Print results
        out << (!line.compare("0") ? "" : line);
        for (int k = 0; k < tail; ++k) out << "9";
        out << std::endl;
    }
}