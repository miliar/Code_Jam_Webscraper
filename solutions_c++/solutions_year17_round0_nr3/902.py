#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <math.h>

using namespace std;

string solveTestCase(unsigned long long N, unsigned long long K);
unsigned long long minInterval(unsigned long long interv);
unsigned long long maxInterval(unsigned long long interv);

int Ls = 0;
int Rs = 0;

int main() {

    ofstream fout;
    fout.open("output.txt");

    if (fout.is_open()) {
        string pancake;
        unsigned long long K;
        unsigned long long N;

        int num_tests = 0;
        cin >> num_tests;

        unsigned count = 1;
        while ( count <= num_tests ) {
            cin >> N >> K;
            fout << "Case #" << count << ": ";
            fout << solveTestCase(N, K) << endl; 
            count++;
        }
        fout.close();
    } else {
        cout << "Can't open file!";
    }
    return 0;
}

string solveTestCase(unsigned long long N, unsigned long long K) {
    typedef pair<unsigned long long, unsigned long long> TestPair;

    TestPair max;
    TestPair min;
    unsigned long long lastMax;
    unsigned long long lastMin;

    max = make_pair(0,0);
    min = make_pair(0,0);

    queue<TestPair> items;
    items.push(make_pair(N, 1));
    //cout << "-----------------------------" << endl;

    TestPair x;
    for (unsigned long long i = 0; i < K; i += x.second) {
        x = items.front();
        items.pop();

        lastMax = maxInterval(x.first);
        lastMin = minInterval(x.first);

        if (!items.empty() && items.back().first == lastMax) items.back().second += x.second;
        else items.push(make_pair(lastMax, x.second));

        if (items.back().first == lastMin) items.back().second += x.second;
        else items.push(make_pair(lastMin, x.second));

/*
        //cout << "x = " << x.first << ", " << x.second << endl;
        if (items.empty() || items.front().first != x.first) {
            if (max.first) {
                max.second += x.second;
                min.second += x.second;
                items.push(max);
                items.push(min);
                max = make_pair(0,0);
                min = make_pair(0,0);
            } else {
                items.push(make_pair(lastMax, 1));
                items.push(make_pair(lastMin, 1));
                //cout << lastMax << ", " << lastMin << endl;
            }
        } else if ( items.front().first == x.first ) {
            max.first = lastMax;
            if (lastMix == lastMin) {
               max.second += x.second + x.second;
            } else {
                min.first = lastMin;
                max.second += x.second;
                min.second += x.second;
            }
        }*/
    }

    //cout << lastMax << " " << lastMin << endl;
    //cout << "-----------------------------" << endl;

    std::stringstream ss;
    ss << lastMax << " " << lastMin;
    return ss.str();
}

unsigned long long minInterval(unsigned long long interv) {
    unsigned long long div = (interv + 1) / 2;
    return (div > 1) ? div - 1 : 0;
}

unsigned long long maxInterval(unsigned long long interv) {
    unsigned long long div = (interv + 1) / 2;
    return (interv > div) ? interv - div : 0;
}