#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <set>
#include <assert.h>
#include <deque>
#include <queue>


using namespace std;
void procCase(const string & pattern, int size, int index);
string flip (string pattern, int size, int index);
typedef pair<pair<string, int>,int> patternByMetric;
ofstream outFile("/home/xuan/CLionProjects/untitled/output.txt");
int main() {

    ifstream inFile("/home/xuan/CLionProjects/untitled/A-small-attempt2.in");
    //ofstream outFile("/home/xuan/CLionProjects/untitled/output.txt");
    string str;
    std::vector<string> input_lines;
    if (inFile.is_open()) {
        cout << "File Opened" <<endl;
        getline(inFile, str);
        //cout<<str<<endl;
    } else {
        //cout << "error opening file, exit" << endl;
        return -1;
    }
    int numOfTests = atoi(str.c_str());
    while (numOfTests--) {
        string test;
        getline(inFile, test);
        input_lines.push_back(test);
        //cout<<test<<"\n";
    }

    for (int i = 0; i < input_lines.size();i++) {
        string input = input_lines[i];
        stringstream ss(input);
        string item;
        char i1 = ' ';
        vector<string> tokens;
        while(getline(ss, item, i1)) {
            tokens.push_back(item);
        }
        string pattern = tokens[0];
        int size = atoi(tokens[1].c_str());

        //flip(pattern, size, 2);
        procCase(pattern, size, i);
    }
    return 0;
}

string flip (string  pattern, int size, int index) {
    assert(pattern.size() > index + size -1);
    string flipped = pattern;
    while (size--) {
        if (pattern[index + size] == '+' ) {
            flipped[index + size] = '-';
        } else {
            flipped[index + size] = '+';
        }
    }
    //cout <<"flipped" << flipped << endl;

    return flipped;
}
int metric(const string & pattern) {
    int num = 0;
    for ( int i = 0; i < pattern.size(); i++) {
        if (pattern[i] == '-') num ++;
    }
    return num;
}
void procCase(const string & pattern, int size, int index) {
    int numPancakes = pattern.size();
    set<string> visited;

    string finalString(numPancakes, '+');
    struct cmp {
        bool operator()(const patternByMetric & p1, const patternByMetric & p2) {
            return p1.second > p2.second;
        }
    };
    //std::priority_queue<patternByMetric, vector<patternByMetric>, cmp> explore;
    deque<pair<string,int>> explore;
    //explore.push(make_pair(make_pair(pattern, 0), metric(pattern)));
    explore.push_back(make_pair(pattern,0));
    while (explore.size() != 0) {

        pair<string, int> toExplore = explore[0];
        explore.pop_front();
//        cout<<"curr " << toExplore.first << endl;
        if (toExplore.first.compare(finalString) == 0) {
            outFile << "Case #" << index +1 << ": " << toExplore.second << endl;
            return;
        }
        set<string>::iterator it = visited.find(toExplore.first);
        if (it != visited.end()) {
            continue;
        } else {
            visited.insert(toExplore.first);
            int depth = toExplore.second + 1;
            for (int i = 0; i < numPancakes - size + 1; i ++) {
                // cout << "iter" << endl;
                string flippedPancakes = flip(toExplore.first, size, i);
                pair<string, int> newPattern(flippedPancakes, depth);
                //explore.push(make_pair(newPattern, metric(flippedPancakes)));
                explore.push_back(newPattern);
            }

        }
    }

    outFile << "Case #" << index+1 << ": IMPOSSIBLE" << endl;

}


