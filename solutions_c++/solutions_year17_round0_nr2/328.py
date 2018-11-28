#include <string>
#include <fstream>
using namespace std;

int main() {
    ifstream    f("in.txt");
    ofstream    g("out.txt");
    int         T; f >> T;
    
    for (int test = 1; test <= T; test++) {
        string  S; f >> S;
        string  R(S.length(), '0');

        for (int i = 0; i < R.length(); i++)
            for (char d = '9'; d >= '0'; d--) {
                fill(R.begin() + i, R.end(), d);
                if (R.compare(S) <= 0) break;
            }
        if (R[0] == '0') R = string(S.length() - 1, '9');
        
        g << "Case #" << test << ": " << R << endl;
    }

    return 0;
}
