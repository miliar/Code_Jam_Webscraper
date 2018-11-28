#include <iostream>
#include <fstream>
#include <map>
using namespace std;

int
main() {
    //fstream in("input.sample");

    string problem = "C";
    //fstream in((problem+"-small-1-attempt0.in").c_str());
    fstream in((problem+"-small-2-attempt0.in").c_str());
    //fstream in(problem+"-large.in");

    ofstream out("result.txt");

    int nbTest;
    int s, p;
    int min, max;
    in >> nbTest;
    for (int i = 1; i <= nbTest; ++i) {
        in >> s >> p;

        map<long, int> m; // sizeEmptySpace, number of them
        m[s] = 1;

        long index0 ;
        long index1;
        for (int j = 0; j < p; j++) {
            index0 = (*(m.rbegin())).first;
            // splitting a biggest
            m[index0] = m[index0] - 1;
            if (m[index0] == 0) {
                m.erase(index0);
            }

            int oldIndex0 = index0;
            index1 = (index0 - 1) / 2;
            index0 = oldIndex0 - index1 - 1;
            m[index0]++;
            m[index1]++;
        }

        out << "Case #" << i << ": " << index0 << " " << index1 << endl;
        cout << "Case #" << i << ": " << index0 << " " << index1 << endl;
    }

    return 0;
}
