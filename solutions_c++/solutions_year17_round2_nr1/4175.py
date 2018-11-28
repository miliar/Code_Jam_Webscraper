#include <iostream>
#include <iomanip>
#include <string>

int main() {
    std::string inpLine;
    int testCases, currentCase;
    long long dest, horses, initpos, speed, horse_count, oldpos, old_speed;
    long double temptime, time_to_reach = 0.0;
    std::getline(std::cin, inpLine);
    testCases = stoi(inpLine);
    inpLine.clear();
    for (currentCase = 0; currentCase != testCases; ++currentCase) {
        std::getline(std::cin, inpLine);
        dest = stoll(inpLine.substr(0, inpLine.find(' ')));
        horse_count = stoll(inpLine.substr(inpLine.find(' ')));
        oldpos = dest;
        old_speed = 0;
        time_to_reach = 0.0;
        for (horses = horse_count; horses != 0; --horses) {
            std::getline(std::cin, inpLine);
            initpos = stoi(inpLine.substr(0, inpLine.find(' ')));
            speed = stoi(inpLine.substr(inpLine.find(' ')));
            if (speed - old_speed > 0) {
                temptime = (oldpos - initpos) / ((long double) (speed - old_speed));
                if (temptime >= time_to_reach) {
                    time_to_reach = (dest - initpos) / ((long double) speed);
                }
            }
            else {
                time_to_reach = (dest - initpos) / ((long double) speed);
            }
            oldpos = initpos;
            old_speed = speed;
            inpLine.clear();
        }
        std::cout << "Case #" << currentCase+1 << ": " << dest / time_to_reach << std::endl;
        inpLine.clear();
    }
    return 0;
}
