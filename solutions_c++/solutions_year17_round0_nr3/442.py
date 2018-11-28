#include <iostream>
#include <map>

using namespace std;

int main () {
    int testCases;
    long long stalls;
    long long people;
    long long min, max;
    map<long long, long long> groups;

    cin >> testCases;
    for (int curCase = 1; curCase <= testCases; curCase++) {
        cin >> stalls >> people;

        groups[stalls] = 1;
        for (long long i = stalls; i > 0; i = i/2) {
            long long temp = i;
            while (groups[temp] != 0) {
                //cout << "There are " << people << " people to enter." << endl;
                //cout << "The largest available space is " << temp << " stalls big." << endl;
                if (temp % 2 == 0) {
                    //cout << "Divided the space in " << 2 * groups[temp] << " spaces of size " << temp/2 << " and " << temp/2 - 1 << "." << endl;
                    groups[temp/2] += groups[temp];
                    groups[temp/2 - 1] += groups[temp];
                }
                else {
                    //cout << "Divided the space in " << 2 * groups[temp] << " spaces of size " << temp/2 << " and " << temp/2 << "." << endl;
                    groups[temp/2] += 2 * groups[temp];
                }

                people -= groups[temp];
                groups[temp] = 0;

                if (people <= 0) {
                    if (temp % 2 == 0) {
                        min = temp/2 - 1;
                        max = temp/2;
                    }
                    else {
                        min = temp/2;
                        max = temp/2;
                    }
                    break;
                }

                temp--;
            }
            if (people <= 0) {
                break;
            }
        }

        cout << "Case #" << curCase << ": " << max << " " << min << endl;

        groups.clear();
    }

    return 0;
}