#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("data/B-large.in");
    ofstream fout("data/B-large.out");

    int test_cnt = 0;
    fin >> test_cnt;

    for (int test_case = 1; test_case <= test_cnt; ++test_case) {
        std::string line;
        fin >> line;

        std::string output = line;
        for (int i = (int)line.size() - 1; i > 0; --i) {
            if (line[i] < line[i - 1]) {
                line[i - 1]--;
                for (int j = i; j < (int)line.size(); ++j) {
                    line[j] = '9';
                }
            }
        }


        fout << "Case #" << test_case << ": " << (line[0] == '0' ? line.substr(1, (int)line.size() - 1) : line) << endl;
    }

    fin.close();
    fout.close();

    return 0;
}
