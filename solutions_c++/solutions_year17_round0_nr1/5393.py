//--------------------------------------------------------------------------------------------------------------------------------------
// Constants

//--------------------------------------------------------------------------------------------------------------------------------------
// Include

#include <iostream> 
#include <string>
#include <fstream>

using namespace std;

#define INP "OVERSIZED_PANCAKES.INP"
#define OUT "OVERSIZED_PANCAKES.OUT"

//--------------------------------------------------------------------------------------------------------------------------------------
// Variables

//--------------------------------------------------------------------------------------------------------------------------------------
// Functions

void xuly(void);

//--------------------------------------------------------------------------------------------------------------------------------------
// Main programs

int main() {
	ifstream in(INP);
	streambuf *cinbuf = std::cin.rdbuf();
	cin.rdbuf(in.rdbuf());

	ofstream out(OUT);
	streambuf *coutbuf = std::cout.rdbuf();
	cout.rdbuf(out.rdbuf());
	xuly();
	return 0;
}

//--------------------------------------------------------------------------------------------------------------------------------------
// Solution

void xuly() {
	int T, K;
	string p;   	
    
    cin >> T;
    
	for (int i = 1; i <= T; i++) {
		cin >> p;
        cin >> K;

		int lenp = p.size();
        bool possible = true;
		if (lenp > 0) {
			int count = 0;
			for(int k = lenp - 1; k >= 0; k--) {
                if (p[k] == '-') {
                    if (k < K - 1) {
                        possible = false;
                        break;
                    }
                    count++;
                    for (int j = k; j > k - K; j--) {
                        if (p[j] == '-') p[j] = '+'; else p[j] = '-';
                    }
                }
            }
            
            if (possible) {
                cout << "Case #" << i << ": " << count << endl;
            } else {
                cout << "Case #" << i << ": IMPOSSIBLE" << endl;
            }
        }
    }
}

