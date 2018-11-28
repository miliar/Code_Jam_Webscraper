#include <iostream>
#include <vector>
#include <cstdio>
#include <iomanip>


using namespace std;


int main() {
    size_t T; // num of test cases

    cin >> T;
    cin.ignore();
    cout << fixed << setprecision(6);

    for (size_t i = 0; i < T; ++i)
    {
        size_t D;  // distance
        size_t N;  // num of horses
        cin >> D >> N;
        cin.ignore();
        cerr << D << " " << N << endl;

        double longest = 0;

        for (size_t j = 0; j < N; ++j)
        {
            size_t pos;
            size_t speedMax;
            cin >> pos >> speedMax;
            double time_left = (D-pos)/(double)speedMax;
            cerr << pos << " " << speedMax << endl;
            if  (time_left > longest)
                longest = time_left;
        }

        // ANSWER
        double avg_speed;
        if (longest>0)
            avg_speed = D/longest;
        else
            avg_speed = D;
        cout << "Case #" << i + 1 << ": " <<  avg_speed << endl;
    }
}
