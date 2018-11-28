#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <iostream>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <stdint.h>
using namespace std;

typedef uint8_t  u8;
typedef uint16_t u16;
typedef uint32_t u32;
typedef uint64_t u64;

typedef int8_t  i8;
typedef int16_t i16;
typedef int32_t i32;
typedef int64_t i64;

struct Horse
{
    double start;
    double speed;
    bool operator<(Horse other) const {
        return start < other.start;
    }
};

int main()
{
    string line;
    u32 inputCount;
    cin >> inputCount;
    for (u32 caseNum = 0; caseNum < inputCount; caseNum++) {
        u32 dist, h;
        cin >> dist >> h;
        vector<Horse> horses(h);
        for (u32 i = 0; i < h; i++) {
            Horse horse;
            cin >> horse.start >> horse.speed;
            horses[i] = horse;
        }
        sort(horses.begin(), horses.end());
        
        double time = 0;
        double curDest = dist;

        u32 i = 0;
        while (i < h) {
            u32 nextHorse;
            bool foundInter = false;

            for (u32 j = i+1; j < h; j++) {
                if (horses[j].speed < horses[i].speed) {
                    double tinter = horses[i].start - horses[j].start;
                    tinter /= horses[j].speed - horses[i].speed;
                    double inter = horses[j].speed * tinter + horses[j].start;

                    if (inter < curDest) {
                        curDest = inter;
                        nextHorse = j;
                        foundInter = true;
                    }
                }
            }

            if (foundInter) {
                i = nextHorse;
            } else {
                break;
            }
        }

        time = (dist - horses[i].start) / horses[i].speed;

        cout << "Case #" << caseNum+1 << ": ";
        cout << fixed << setprecision(6) << (double)dist / time << endl;
    }
}
