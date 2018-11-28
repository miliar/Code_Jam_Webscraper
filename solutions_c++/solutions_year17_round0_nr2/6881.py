#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>

void solveCase(std::istream& in, std::ostream& out) {
    std::string n;
    in >> n;

    auto it = n.insert(n.begin(), '0') + 1;

    while (it != std::end(n)) {
        if (*it < it[-1]) {
            --it;
            while (*it == *(--it));
            it++;
            auto sz = std::distance(it, std::end(n)) - 1;
            auto pos = std::distance(std::begin(n), it) + 1;
            n.replace(pos, sz, sz, '9');
            n[pos-1] = (*it)-1;
            break;
        }
        it++;
    }
    auto idx = n.find_last_of('0') + 1;
    n.erase(0, idx);
    out << n;

}

int main(int argc, char** argv) {
    using namespace std;
    string file = "B-large";

    ifstream in(file + ".in", ifstream::in);
    ofstream out(file+ ".out", ofstream::out);
//    auto& out = cout;
    int T;
    in >> T;
    int t = 0;
    while (t++ < T) {
        out << "Case #" << t << ": ";
        solveCase(in, out);
        out << endl;
    }
    return 0;
}