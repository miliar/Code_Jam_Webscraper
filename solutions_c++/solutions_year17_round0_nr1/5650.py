#include <iostream>
#include <fstream>
#include <bitset>

int main() {
    std::ifstream in("A-large.in");
    std::ofstream out("out.txt");
    int num_samples = 0;
    in >> num_samples;
    for (int i = 1; i <= num_samples; ++i) {
        std::string line = "";
        int flip_size = 0;
        in >> line >> flip_size;

        int num_flips = 0;
        std::bitset<1000> data;
        for (int j = 0; j < line.size(); ++j)  data[j] = line[j] == '+' ? 1 : 0;
        for (int j = 0; j < line.size(); ++j)  {
            if (data[j] == 1) continue;
            if (j + flip_size > line.size()) {
                num_flips = -1;
                break;
            } else {
                for (int k = j; k < j + flip_size; ++k) data[k].flip();
                num_flips++;
            }
        }

        // Print results
        out << "Case #" << i << ": "
            << (num_flips == -1 ? "IMPOSSIBLE" : std::to_string(num_flips)) << std::endl;
    }
}