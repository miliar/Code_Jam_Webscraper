#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <time.h>       /* time */
#include <algorithm>
#include <list>
#include <utility>
#include <stack>
#include <math.h>
#include <iomanip>

using namespace std;


int main() {
    ofstream outfile;
    outfile.open("solution.out");
    std::ifstream infile;
    infile.open("data.in", std::ifstream::in);
    std::string line;
    getline(infile, line);
    std::stringstream lineStream(line);
    int T;
    lineStream >> T;
    for (int caseNr = 1; caseNr <= T; caseNr++) {
        cout << "Solving case number " << caseNr << endl;
        outfile << "Case #" << caseNr << ": ";
        int N, R, O, Y, G, B, V;
        getline(infile, line);
        std::stringstream Stream1(line);
        Stream1 >> N >> R >> O >> Y >> G >> B >> V;
        int Beq = B - O;
        int Req = R - G;
        int Yeq = Y - V;
        int sum = Beq + Req + Yeq;
        int types = 0;
        int twotypes = 0;
        if (R > 0) types++;
        if (O > 0) {
            types++;
            twotypes++;
        }
        if (Y > 0) types++;
        if (G > 0) {
            types++;
            twotypes++;
        }
        if (B > 0) types++;
        if (V > 0) {
            types++;
            twotypes++;
        }
        if (types == 2 && twotypes == 1) {
            if (R > 0 && G > 0 && R == G) {
                while (R > 0) {
                    outfile << "RG";
                    R--;
                }
            } else if (Y > 0 && V > 0 && Y == V) {
                while (Y > 0) {
                    outfile << "YV";
                    Y--;
                }
            } else if (B > 0 && O > 0 && B == O) {
                while (B > 0) {
                    outfile << "BO";
                    B--;
                }
            } else {
                outfile << "IMPOSSIBLE";
            }
        } else {
            if (2 * Beq > sum || 2 * Req > sum || 2 * Yeq > sum || Beq < 0 || Req < 0 || Yeq < 0 || (O>0 && O==B) || (V>0 && V==Y) || (G>0 && G==R)) {
                outfile << "IMPOSSIBLE";
            } else {
                vector<int> stalls;
                vector<int> color;
                color.push_back(Beq);
                color.push_back(Req);
                color.push_back(Yeq);
                if (Beq >= Req && Beq >= Yeq) {
                    stalls.push_back(0);
                    color[0]--;
                } else if (Req > Beq && Req >= Yeq) {
                    stalls.push_back(1);
                    color[1]--;
                } else if (Yeq > Beq && Yeq > Req) {
                    stalls.push_back(2);
                    color[2]--;
                }
                sum--;
                while (sum > 3) {
                    if (stalls.back() == 0) {
                        if (color[1] >= color[2]) {
                            stalls.push_back(1);
                            color[1]--;
                            sum--;
                        } else {
                            stalls.push_back(2);
                            color[2]--;
                            sum--;
                        }
                    } else if (stalls.back() == 1) {
                        if (color[0] >= color[2]) {
                            stalls.push_back(0);
                            color[0]--;
                            sum--;
                        } else {
                            stalls.push_back(2);
                            color[2]--;
                            sum--;
                        }
                    } else if (stalls.back() == 2) {
                        if (color[0] >= color[1]) {
                            stalls.push_back(0);
                            color[0]--;
                            sum--;
                        } else {
                            stalls.push_back(1);
                            color[1]--;
                            sum--;
                        }
                    }
                }
                if(color[0]>1 || color[1]>1 || color[2]>1){
                    int i1=-1;
                    int i2=-1;
                    if(color[0]>1){
                        i1=0;
                    }
                    if(color[1]>1){
                        i1=1;
                    }
                    if(color[2]>1){
                        i1=2;
                    }
                    if(color[0]==1){
                        i2=0;
                    }
                    if(color[1]==1){
                        i2=1;
                    }
                    if(color[2]==1){
                        i2=2;
                    }
                    if(i1<0 || i2<0) cout<<"ERROR"<<endl;
                    else{
                        stalls.push_back(i1);
                        stalls.push_back(i2);
                        stalls.push_back(i1);
                    }
                }else {
                    if (stalls.front() == stalls.back()) {
                        int i = (stalls.front() + 1) % 3;
                        if (color[i] > 0) {
                            stalls.push_back(i);
                            color[i]--;
                        }
                        i = (i + 2) % 3;
                        if (color[i] > 0) {
                            stalls.push_back(i);
                            color[i]--;
                        }
                        i = (i + 2) % 3;
                        if (color[i] > 0) {
                            stalls.push_back(i);
                            color[i]--;
                        }
                    } else {
                        int i2 = (2 * (stalls.front() + stalls.back())) % 3;
                        int i1 = stalls.front();
                        int i3 = stalls.back();
                        if (color[i1] > 0) {
                            stalls.push_back(i1);
                            color[i1]--;
                        }
                        if (color[i2] > 0) {
                            stalls.push_back(i2);
                            color[i2]--;
                        }
                        if (color[i3] > 0) {
                            stalls.push_back(i3);
                            color[i3]--;
                        }
                    }
                }
                cout << "remaining colors are " << color[0] + color[1] + color[2] << endl;
                for (int i = 0; i < stalls.size(); i++) {
                    if (stalls[i] == 0) {
                        outfile << "B";
                        B--;
                        while (O > 0) {
                            outfile << "OB";
                            O--;
                            B--;
                        }
                    }
                    if (stalls[i] == 1) {
                        outfile << "R";
                        R--;
                        while (G > 0) {
                            outfile << "GR";
                            G--;
                            R--;
                        }
                    }
                    if (stalls[i] == 2) {
                        outfile << "Y";
                        Y--;
                        while (V > 0) {
                            outfile << "VY";
                            V--;
                            Y--;
                        }
                    }

                }
                cout << "2nd remainin colors are: " << B + Y + R + G + O + V << endl;
            }
        }


        outfile << endl;
    }

    infile.close();
    outfile.close();
    return 0;
}


