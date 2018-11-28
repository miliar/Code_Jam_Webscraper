#include <iostream>
#include <iomanip>
using namespace std;

int main(int argc, char *argv[])
{
    int T;
    cin >> T;

    for (int index = 0; index < T; ++index) {

        int destination, totalHourses;
        cin >> destination;
        cin >> totalHourses;

        double output = 0;
        for (int inner = 0; inner < totalHourses; ++inner) {
            int initialPosition;
            int maxSpeed;
            cin >> initialPosition >> maxSpeed;
            double diff = destination - initialPosition;
            double divider = diff / maxSpeed;
            double initialOuput = destination / divider;

            if(inner == 0 || initialOuput < output) {
                output = initialOuput;
            }
        }
        cout << "Case #" << index + 1 << ": " << std::fixed << std::setprecision(6) << output << std::endl;
    }

}
