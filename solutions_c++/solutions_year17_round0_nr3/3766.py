#include <iostream>
#include <map>
using namespace std;
int main() {
    int t;
    long long stallNum, personNum;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        map<long long, long long> manageRoom;
        cin >> stallNum >> personNum;
        if(stallNum == personNum) {
            cout << "Case #" << i << ": 0 0" << endl;
        } else if(stallNum - personNum == 1){
            if(stallNum == 2 && personNum == 1) {
                cout << "Case #" << i << ": 1 0" << endl;
            } else {
                cout << "Case #" << i << ": 0 0" << endl;
            }
        } else {
            // algo...
            // init
            manageRoom[stallNum] = 1;

            for(long long j = 1; j <= personNum; j++) {
                // find the max room
                long long length = manageRoom.rbegin()->first;

                // delete one
                if(manageRoom[length]>1) {
                    manageRoom[length]--;
                } else {
                    manageRoom.erase(length);
                }

                // split room and add room
                long long halfStallNum = length/2;
                if(length %2 == 0) {
                    manageRoom[halfStallNum]++;
                    manageRoom[halfStallNum-1]++;
                    if(j==personNum) {
                        cout << "Case #" << i << ": " << halfStallNum << " " << halfStallNum-1 << endl;
                    }
                } else {
                    manageRoom[halfStallNum] += 2;
                    if(j==personNum) {
                        cout << "Case #" << i << ": " << halfStallNum << " " << halfStallNum << endl;
                    }
                }
                // cout << length << endl;
            }


        }
    }
    return 0;
}
