//--------------------------------------------------------------------------------------------------------------------------------------
// Constants

//--------------------------------------------------------------------------------------------------------------------------------------
// Include

#include <iostream> 
#include <string>
#include <fstream>

using namespace std;

#define INP "TIDY_NUMBERS.INP"
#define OUT "TIDY_NUMBERS.OUT"

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
	int T;
	string p;   	
    
    cin >> T;
    
	for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": ";

		cin >> p;
		int lenp = p.size();
		if (lenp > 0) {
            int t = lenp - 1;
            do {
                bool found = false;
    			for (int k = 0; k <= t - 1; k++) {
                    int valueK = p[k] - '0';
                    int valueNextK = p[k + 1] - '0';                   

                    if (valueK > valueNextK) {
                        t = k;
                        p[k] = valueK - 1 + '0';
                        for (int j = k + 1; j < lenp; j++) {
                            p[j] = '9'; 
                        }
                        
                        found = true;
                        break;
                    }         
                }
                
                if (!found) {
                    t = -1;
                }               
                
            } while (t >= 0); 
            
            int c = 0;
            
            while (p[c] == '0') {
                c++;
            }
            
            for (int k = c; k < lenp; k++) {
                cout << p[k];
            }
            
            cout << endl;
        }
    }
}

