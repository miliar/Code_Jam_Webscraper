#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include <iomanip>


# define M_PIl          3.141592653589793238462643383279502884L

struct State {
    int numStack;
    int lastR;
    double area;

    State(int _numStack, int _lastR, double _area) : numStack(_numStack), lastR(_lastR), area(_area) {}
};

int main() {
    int T;
    std::cin >> T;
    for (int t=1; t <= T; ++t) {
        int N, K;
        std::cin >> N >> K;
        std::vector<std::pair<int,int> > RH(N);
        for (int i=0; i < N; ++i) {
            std::cin >> RH[i].first >> RH[i].second;
        }


        sort(RH.begin(), RH.end());
        std::reverse(RH.begin(), RH.end());

        std::vector< std::vector<State> > states(N);
        for (int i=0; i < RH.size(); ++i) {
            //Use the cake as the beginning
            {
                int numStack = 0;
                int lastR = RH[i].first;
                double area = M_PIl * lastR * lastR + 2 * M_PIl * lastR * RH[i].second;
                states[i].push_back(State(numStack, lastR, area));
            }
            for (int j=0; j < i; ++j) {
                //we scan through all that end with radius R_j
                for (int k=0; k < states[j].size(); ++k) {
                    //We scan through all that prev numStack k and look the case where we assume putting the current cake on top is optimal
                    if (k >= K-1) break;
                    {
                        int numStack = k+1;
                        int lastR = RH[i].first;
                        double area = states[j][k].area + 2 * M_PIl * lastR * RH[i].second;
                        if (states[i].size() == k+1) {
                            states[i].push_back( State(numStack, lastR, area) );
                        }
                        else if (states[i].size() > k+1 && area > states[i][k+1].area) {
                            states[i][k+1].area = area;
                        }
                    }

                }
            }
        }

        double bestResult = 0.0;
        for (int i=0; i < states.size(); ++i) {
            if (states[i].size() >= K && states[i][K-1].area > bestResult) {
                bestResult = states[i][K-1].area;
            }
        }
        std::cout << std::fixed << std::setprecision(7) <<  "Case #" << t << ": " << bestResult << std::endl;



    }

    return 0;
}
