#include <iostream>
#include <fstream>
#include <cmath>

int main() {
    std::ifstream in("C-small-1-attempt2.in");
    std::ofstream out("out.txt");
    int num_samples = 0;
    in >> num_samples;
    for (int i = 1; i <= num_samples; ++i) {
        out << "Case #" << i << ": ";
        uint64_t num_stalls;
        uint64_t num_people;
        in >> num_stalls >> num_people;

        bool stalls[num_stalls + 2] = {false};
        stalls[0] = true;
        stalls[num_stalls + 1] = true;

        uint64_t max_ret = 0;
        uint64_t min_ret = 0;

        for (uint64_t j = 0; j < num_people; ++j) {
            uint64_t cur_pos = 0;
            uint64_t next_pos = 0;
            uint64_t taken_pos = 0;
            uint64_t max_space = 0;
            while (cur_pos + 1 < num_stalls + 2) {
                next_pos = cur_pos + 1;
                while (!stalls[next_pos]) next_pos++;
                if (next_pos - cur_pos - 1 > max_space) {
                    max_space = next_pos - cur_pos - 1;
                    taken_pos = cur_pos + (max_space % 2 == 0 ? max_space / 2 : max_space / 2 + 1);
                    max_ret = (max_space - 1) % 2 == 0 ? (max_space - 1) / 2 : ((max_space - 1) / 2 + 1);
                    min_ret = (max_space - 1) / 2;
                }
                cur_pos = next_pos;
            }

            stalls[taken_pos] = true;
        }

        out << max_ret << " " << min_ret << std::endl;
    }
}