#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

struct Horse
{
    size_t pos;
    size_t speed;
};

double compute(size_t d, size_t n, vector<Horse> horses)
{
    double time_to_arrival = 0.0;
    bool first = true;
    for (auto h : horses)
    {
        double distance_to_travel = d - h.pos;
        double time_to_arrival_horse = distance_to_travel / h.speed;
        
        if (first) {
            time_to_arrival = time_to_arrival_horse;
            first = false;
        } else {
            time_to_arrival = max( time_to_arrival, time_to_arrival_horse );
        }
    }
    double annie_speed = d / time_to_arrival;
    return annie_speed;
}


int main() {
    int t;
    cin >> t;  // read T
    for (int i = 1; i <= t; ++i) {
        size_t d, n;
        cin >> d; // read D
        cin >> n; // read N
        vector<Horse> horses;
        for (size_t j = 1; j <= n; j++) {
            size_t k;
            size_t s;
            cin >> k;
            cin >> s;
            horses.push_back( Horse{ k, s } );
        }
        cout << "Case #" << i << ": " << setiosflags(ios::fixed) << setprecision(6) << compute(d, n, horses) << endl;
    }
}
