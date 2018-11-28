#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <climits>
#include <unordered_map>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for( int t = 1; t <= T; t++ )
    {
        cout << "Case #" << t << ": ";

        int ac, aj;
        cin >> ac >> aj;

        if (ac + aj == 1) {
            int begin, end;
            cin >> begin >> end;
            cout << 2;
        }
        else {
            int begin1, end1;
            int begin2, end2;
            cin >> begin1 >> end1;
            cin >> begin2 >> end2;
    
            if (begin1 > begin2) {
                swap(begin1, begin2);
                swap(end1, end2);
            }

            if (ac == 1 && aj == 1) {
                cout << 2;
            }
            else {
                if (end2 - begin1 <= 720 || begin2 - end1 >= 720) {
                    cout << 2;
                }
                else {
                    cout << 4;
                }
    
            }
        }

        cout << endl;
    }

    return 0;
}
