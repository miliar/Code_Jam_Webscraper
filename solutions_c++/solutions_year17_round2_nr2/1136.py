#include <iostream>
#include <string>
using namespace std;

int main() {
	unsigned cases;
	cin >> cases;

	for (unsigned caseIndex = 1; caseIndex <= cases; ++caseIndex) {
        unsigned N, R, O, Y, G, B, V;

        cin >> N >> R >> O >> Y >> G >> B >> V;

        string s = "";

        string BOB = "B";
        string RGR = "R";
        string YVY = "Y";

        unsigned r = R;
        unsigned y = Y;
        unsigned b = B;

        if (O != 0) {
            b -= O;

            BOB = "B";
            for (unsigned i = 0; i < O; ++i)
                BOB += "OB";
        }

        if (G != 0) {
            r -= G;

            RGR = "R";
            for (unsigned i = 0; i < G; ++i)
                RGR += "GR";
        }

        if (V != 0) {
            y -= V;

            YVY = "Y";
            for (unsigned i = 0; i < V; ++i)
                YVY += "VY";
        }

        unsigned total = r + y + b;
        if (total == 0) {
            unsigned count = 0;
            if (BOB != "B") ++count;
            if (RGR != "R") ++count;
            if (YVY != "Y") ++count;

            if (count > 1)
                cout << "Case #" << caseIndex << ": IMPOSSIBLE\n";
            else {
                if (BOB != "B")
                    s = BOB.substr(1);
                else if (RGR != "R")
                    s = RGR.substr(1);
                else if (YVY != "Y")
                    s = YVY.substr(1);

                cout << "Case #" << caseIndex << ": " << s << "\n";

            }
        }
        else if (2 * r > total || 2 * y > total || 2 * b > total)
            cout << "Case #" << caseIndex << ": IMPOSSIBLE\n";
        else {
            unsigned count[3];
            count[0] = r;
            count[1] = y;
            count[2] = b;
    
            unsigned priority[3];
            priority[0] = 0;
            priority[1] = 1;
            priority[2] = 2;
    
            for (unsigned i = 0; i < 3; ++i) {
                for (unsigned j = i; j > 0; --j) {
                    if (count[j] > count[j - 1]) {
                        unsigned temp = priority[j];
                        priority[j] = priority[j - 1];
                        priority[j - 1] = temp;
                    }
                }
            }

            unsigned prevIndex = 3;
    
            while (count[0] + count[1] + count[2] != 0) {
                unsigned index = priority[0];
                if (index == prevIndex)
                    index = priority[1];

                for (unsigned i = 0; i < 3; ++i) {
                    if (i != prevIndex && count[i] > count[index])
                        index = i;
                }

                --count[index];
                prevIndex = index;

                if (index == 0) {
                    s += RGR;
                    RGR = "R";
                } else if (index == 1) {
                    s += YVY;
                    YVY = "Y";
                } else if (index == 2) {
                    s += BOB;
                    BOB = "B";
                }                
            }
    
            cout << "Case #" << caseIndex << ": " << s << "\n";

        }
	}
}
