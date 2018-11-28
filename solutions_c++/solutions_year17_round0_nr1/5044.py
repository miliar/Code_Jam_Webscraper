#include <iostream>
#include <fstream>
using namespace std;

int
main() {
    //fstream in("input.sample");
    //fstream in("A-small-attempt0.in");
    fstream in("A-large.in");

    ofstream out("result.txt");

    int nbTest, width;
    string str;
    in >> nbTest;
    for (int i = 1; i <= nbTest; ++i) {
        in >> str >> width;
        int rotate = 0;
        for(int j = 0 ; j <= str.length() - width ; j++) {
            if (str.at(j) == '-') {
                for (int k = j ; k < j + width ; k ++ ) {
                    if (str.at(k) == '-') {
                        str.at(k) ='+';
                    } else {
                        str.at(k) ='-';
                    }
                }
                cerr << "rotate at " << j << " " << str << endl;
                rotate ++;
            } else {
            }
        }

        bool imposible = false;
        for(int j = str.length() - 1 ; j >= str.length() - width + 1 ; j--) {
            if (str.at(j) == '-') {
                imposible = true;
                break;
            }
        }
        if (imposible) {
            out << "Case #" << i << ": IMPOSSIBLE" << endl;
            cout << "Case #" << i << ": IMPOSSIBLE" << endl;
        } else {
            out << "Case #" << i << ": " << rotate << endl;
            cout << "Case #" << i << ": " << rotate << endl;
        }
    }

    return 0;
}
