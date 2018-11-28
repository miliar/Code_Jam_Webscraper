#include <vector>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <functional>
#include <sstream>
#include <cmath>
using namespace std;


struct Job {
    int id;
    int priority;
    int start;
    int duration;
};



Job read() {
    char c;
    Job job;
    cin >> c >> job.id >> c >> job.priority >> c >> job.start >> c >> job.duration >> c;
    return job;

}

int main()
{
    int T, K;
    cin >> T;
    for(int n = 1; n <= T; ++n)
    {
        string input;
        cin >> input >> K;
        vector<int> remove(input.size());
        int counter = 0, result = 0;
        int size = input.size();
        if(size < K) {
            cout << "Case #" << n << ": IMPOSSIBLE" << endl;
            continue;
        }
        for(int i = 0; i <= size - K; ++i) {
            counter -= remove[i];
            if((input[i] == '+' && (counter % 2 == 1)) || (input[i] == '-' && (counter % 2 == 0))) {
                counter++;
                result++;
                if(i < size - K){
                    remove[i + K] = 1;
                }
            }
        }
        bool impossible = false;
        for(int i = size - K + 1; i < size; ++i) {
            counter -= remove[i];
            if((input[i] == '+' && (counter % 2 == 1)) || (input[i] == '-' && (counter % 2 == 0))) {
                impossible = true;
                cout << "Case #" << n << ": IMPOSSIBLE" << endl;
                break;
            }
        }
        if(!impossible){
            cout << "Case #" << n << ": " << result << endl;
        }
    }




}