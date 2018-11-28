#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>


struct State {
    int start;
    int end;
    char code;
    State(int _start, int _end, char _code) : start(_start), end(_end), code(_code) {}
    State() : start(0), end(0), code('_') {}
};

bool operator< (const State& a, const State& b) {
    if (a.start != b.start) return a.start < b.start;
    else if (a.end != b.end) return a.end < b.end;
    else return a.code < b.code;
}

bool compareStateSize(const State& a, const State& b) {
    int asize = a.end - a.start;
    int bsize = b.end - b.start;
    if (asize != bsize) return asize < bsize;
    else return a < b;
}


int main() {
    int T;
    std::cin >> T;
    for (int t=1; t <= T; ++t) {
        int Ac, Aj;
        std::cin >> Ac >> Aj;
        std::vector<State> fixedStates;
        int Cleft = 720, Jleft = 720;
        for (int i=0; i < Ac; ++i) {
            State s;
            s.code = 'C';
            std::cin >> s.start >> s.end;
            fixedStates.push_back(s);
            Cleft -= s.end - s.start;
        }

        for (int i=0; i < Aj; ++i) {
            State s;
            s.code = 'J';
            std::cin >> s.start >> s.end;
            fixedStates.push_back(s);
            Jleft -= s.end - s.start;
        }

        sort(fixedStates.begin(), fixedStates.end());

        /*
        std::cout << "Ac: " << Ac << ", Aj: " << Aj << std::endl;
        std::cout << "Cleft: " << Cleft << ", Jleft: " << Jleft << std::endl;
        for (int i=0; i < fixedStates.size(); ++i) {
            std::cout << fixedStates[i].start << " " << fixedStates[i].end << " " << fixedStates[i].code << std::endl;
        }
        //*/

        //Now we want to give more code for the non-fixed interval
        // c : in between cameron fixed schedule
        // j : in between james fixed schedule
        // t : transition between cameron and james
        // We will greedily get from the smallest size in c and put cameron time in, the same with james
        // The remainder will be put into transition

        // Notice that between the midnight will be a special interval where end can be more than 720
        //
        std::map<char, std::vector<State> > otherStates;

        int numFixed = Ac + Aj;
        for (int i=0; i < fixedStates.size(); ++i) {
            int prevIndex = (i + numFixed - 1) % numFixed;
            const State& prevState = fixedStates[prevIndex];
            const State& nextState = fixedStates[i];
            int curStart = prevState.end;
            int curEnd = nextState.start;
            if (i == 0) curEnd += 1440;
            if (curStart == curEnd) continue;
            char curCode = 't';
            if (prevState.code == nextState.code) {
                if (prevState.code == 'C') curCode = 'c';
                else if (prevState.code == 'J') curCode = 'j';
            }

            otherStates[curCode].push_back( State(curStart, curEnd, curCode) );
        }

        sort(otherStates['c'].begin(), otherStates['c'].end(), compareStateSize);
        sort(otherStates['j'].begin(), otherStates['j'].end(), compareStateSize);

        /*

        std::cout << "state code c: " << std::endl;
        for (int i=0; i < otherStates['c'].size(); ++i) {
            std::cout << otherStates['c'][i].start << " " << otherStates['c'][i].end << " " << otherStates['c'][i].code << std::endl;
        }

        std::cout << "state code j: " << std::endl;
        for (int i=0; i < otherStates['j'].size(); ++i) {
            std::cout << otherStates['j'][i].start << " " << otherStates['j'][i].end << " " << otherStates['j'][i].code << std::endl;
        }
        //*/
        //

        /*
        int temp_result = Ac + Aj;

        for (int i=0; i < otherStates['c'].size(); ++i) {
            int end = otherStates['c'][i].end;
            int start = otherStates['c'][i].start;
            int size = end - start;
            if (Cleft >= size) {
                temp_result -= 1;
            }
            else {
                temp_result += 1;
            }
        }

        for (int i=0; i < otherStates['j'].size(); ++i) {
            int end = otherStates['j'][i].end;
            int start = otherStates['j'][i].start;
            int size = end - start;
            if (Jleft >= size) {
                temp_result -= 1;
            }
            else {
                temp_result += 1;
            }
        }

        if (fixedStates[0].start == 0 && fixedStates.back().end == 1440) temp_result -= 1;
        if (temp_result < 2) temp_result = 2;

        std::cout << "Case #" << t << ": " << temp_result << std::endl;

        //*/
            

        //*

        {
            int pos = 0;
            while (Cleft > 0 && pos < otherStates['c'].size()) {
                int end = otherStates['c'][pos].end;
                int start = otherStates['c'][pos].start;
                int size = end - start;
                if (Cleft >= size) {
                    fixedStates.push_back( State(start, end, 'C') );
                    Cleft -= size;
                }
                pos += 1;
            }
        }

        {
            int pos = 0;
            while (Jleft > 0 && pos < otherStates['j'].size()) {
                int end = otherStates['j'][pos].end;
                int start = otherStates['j'][pos].start;
                int size = end - start;
                if (Jleft >= size) {
                    fixedStates.push_back( State(start, end, 'J') );
                    Jleft -= size;
                }
                pos += 1;
            }
        }

        sort(fixedStates.begin(), fixedStates.end());

        /*
        std::cout << "Final fixedStates: " << std::endl;
        for (int i=0; i < fixedStates.size(); ++i) {
            std::cout << fixedStates[i].start << " " << fixedStates[i].end << " " << fixedStates[i].code << std::endl;
        }
        //*/

        std::vector<char> fullSchedule(1440, 't');

        for (int i=0; i < fixedStates.size(); ++i) {
            int start = fixedStates[i].start;
            int end = fixedStates[i].end;
            char code = fixedStates[i].code;
            for (int j=start; j < end; ++j) {
                int index = j % 1440;
                fullSchedule[index] = code;
            }
        }

        // Scan through all fullSchedule and replace the transition with the previous code (if there is a time left)
        int startScan = 0;
        int numConsidered = 0;
        while (fullSchedule[startScan] == 't' && numConsidered < 1440) {
            startScan++;
            numConsidered++;
        }
        char curCode = fullSchedule[startScan];
        if (curCode != 't') {
            //std::cout << "startScan: " << startScan << std::endl;
            while (fullSchedule[startScan] == curCode && numConsidered < 1440) {
                startScan = (startScan + 1440 - 1) % 1440;
                numConsidered++;
            }
            int result = 0;
            char prevCode = curCode;
            for (int i=1; i <= 1441; ++i) {
                int index = (i + startScan)%1440;
                if (fullSchedule[index] == prevCode) {
                    continue;
                }
                else {
                    if (fullSchedule[index] == 't') {
                        if (prevCode == 'C') {
                            if (Cleft > 0) {
                                Cleft--;
                                fullSchedule[index] = 'C';
                                prevCode = 'C';
                            }
                            else {
                                Jleft--;
                                fullSchedule[index] = 'J';
                                prevCode = 'J';
                                result += 1;
                                //std::cout << "ADD RESULT at index: " << index << ", with curCode: " << prevCode << std::endl;
                            }
                        }
                        else if (prevCode == 'J') {
                            if (Jleft > 0) {
                                Jleft--;
                                fullSchedule[index] = 'J';
                                prevCode = 'J';
                            }
                            else {
                                Cleft--;
                                fullSchedule[index] = 'C';
                                prevCode = 'C';
                                result += 1;
                                //std::cout << "ADD RESULT at index: " << index << ", with curCode: " << prevCode << std::endl;
                            }
                        }
                    }
                    else {
                        prevCode = fullSchedule[index];
                        result += 1;
                        //std::cout << "ADD RESULT at index: " << index << ", with curCode: " << prevCode << std::endl;
                    }
                }
            }

            std::cout << "Case #" << t << ": " << result << std::endl;


        }
        else {
            std::cout << "Case #" << t << ": 2" << std::endl;
        }
    //*/




            


    }

    return 0;
}
