#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>


int main() {
    int T;
    std::cin >> T;
    for (int t=1; t <= T; ++t) {
        int N, R, O, Y, G, B, V;
        std::cin >> N >> R >> O >> Y >> G >> B >> V;
        int RR = R-G, BB = B-O, YY = Y-V;
        int NN = RR + BB + YY;
        std::vector<std::pair<int, std::string> > cv;
        cv.push_back( std::make_pair(RR, "R"));
        cv.push_back( std::make_pair(BB, "B"));
        cv.push_back( std::make_pair(YY, "Y"));
        // The algorihtm will exhaust the minimum one with the maximum one first.
        std::string result;
        std::string lastResultChar = "";
        bool isPossible = true;
        std::string curState = "min";
        for (int i=0; i < NN; ++i) {
            sort(cv.begin(), cv.end());
            if (curState == "min") {
                int start = 0;
                while (start < cv.size() && cv[start].first == 0){
                    start++;
                }
                if (lastResultChar == cv[start].second) start++;
                if (start >= cv.size()) {
                    isPossible = false;
                    break;
                }
                result += cv[start].second;
                lastResultChar = cv[start].second;
                cv[start].first--;
                curState = "max";
            }
            else {
                int end = cv.size()-1;
                if (lastResultChar == cv[end].second) end--;
                if (cv[end].first == 0) {
                    isPossible = false;
                    break;
                }
                result += cv[end].second;
                lastResultChar = cv[end].second;
                cv[end].first--;
                curState = "min";
            }
        }
        if ((R > 0 && R == G && N > R + G) || (B > 0 && B == O && N > B + O) || (Y > 0 && Y == V && N > Y + V)) isPossible = false;
        else if (result.size() > 0 && result[0] == result[result.size()-1]) isPossible = false;
        else if (RR < 0 || BB < 0 || YY < 0) isPossible = false;

        //Replace one R, B, or Y to RGRGR, BOBOB, or YVYVYVY (find the first one)
        if (isPossible) {
            if (G > 0) {
                if (RR > 0) {
                    for (int i=0; i < result.size(); ++i) {
                        if (result[i] == 'R') {
                            std::string toInsert = "";
                            for (int j=0; j < G; ++j) {
                                toInsert += "GR";
                            }
                            result.insert(i+1, toInsert);
                            break;
                        }
                    }
                }
                else {
                    result = "";
                    for (int i=0; i < G; ++i) {
                        result += "GR";
                    }
                }
            }

            if (O > 0) {
                if (BB > 0) {
                    for (int i=0; i < result.size(); ++i) {
                        if (result[i] == 'B') {
                            std::string toInsert = "";
                            for (int j=0; j < O; ++j) {
                                toInsert += "OB";
                            }
                            result.insert(i+1, toInsert);
                            break;
                        }
                    }
                }
                else {
                    result = "";
                    for (int i=0; i < O; ++i) {
                        result += "OB";
                    }
                }
            }
            
            if (V > 0) {
                if (YY > 0) {
                    for (int i=0; i < result.size(); ++i) {
                        if (result[i] == 'Y') {
                            std::string toInsert = "";
                            for (int j=0; j < V; ++j) {
                                toInsert += "VY";
                            }
                            result.insert(i+1, toInsert);
                            break;
                        }
                    }
                }
                else {
                    result = "";
                    for (int i=0; i < V; ++i) {
                        result += "VY";
                    }
                }
            }
            if (result.size() == N) {
                std::cout << "Case #" << t << ": " << result << std::endl;
            }
            else {
                std::cout << "Case #" << t << ": IMPOSSIBLE" << std::endl;

            }
        }
        else {
            std::cout << "Case #" << t << ": IMPOSSIBLE" << std::endl;
        }
    }
    return 0;
}

                
            


        
