#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>
#include <limits>

typedef std::numeric_limits< double > dbl;

using namespace std;

int main() {
    cout.precision(dbl::max_digits10);
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        int N; //Number of pancakes
        int K; //Stack size
        cin >> N >> K;
        //Take the largest and smallest pancakes, interleaving them
        vector<pair<int, pair<int, double>>> pancakes(N);

        for(pair<int,pair<int,double>> &p : pancakes) {
            cin >> p.first >> p.second.first;
            //Side Area = 2 pi r * H
            p.second.second = 2 * M_PI * p.first * p.second.first;
        }
        //Sort by radius then by height (increasing)
        sort(pancakes.begin(), pancakes.end());

        double max_surface = 0;

        //Consider selecting each pancake as the base, starting with the largest radius
        while(pancakes.size() >= K) {
            //Take the biggest pancake as the base
            pair<int,pair<int, double>> biggest = pancakes.back();
            pancakes.pop_back();
            //Sort the remaining pancakes by side surface area
            vector<double> side_areas;
            for(pair<int,pair<int, double>> &p : pancakes) {
                //add the side surface area
                side_areas.push_back(p.second.second);
            }
            //Sort, largest side area first
            sort(side_areas.begin(), side_areas.end(), greater<double>());
            //Limit to K - 1
            side_areas.resize(K - 1);
            //Top of pancake
            double surface = M_PI * biggest.first * biggest.first;
            //Side of base
            surface += biggest.second.second;
            //Remaining sides
            for(double &side_area : side_areas) {
                surface += side_area;
            }
            //cerr << "base: " << biggest.first << " " << biggest.second.first << ", surface=" << surface << endl;
            max_surface = max(max_surface, surface);
        }

        cout << "Case #" << (t + 1) << ": ";
        cout << max_surface;
        cout << endl;
    }
}
