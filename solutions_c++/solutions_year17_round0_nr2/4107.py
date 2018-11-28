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
    int T;
    string input;
    cin >> T;
    for(int n = 1; n <= T; ++n)
    {
        cin >> input;
        vector<int> digits(input.size());
        for(int i = 0; i < input.size(); ++i){
            digits[i] = input[i] - '0';
        }
        bool changed = false;
        do{
            bool cut = false;
            changed = false;
            for(int i = 0; i < input.size(); ++i) {
                if(cut) {
                    digits[i] = 9;
                } else {
                    if(i+1 < input.size() && digits[i] > digits[i+1]) {
                        --digits[i];
                        cut = true;
                        changed = true;
                    }
                }
            }
        } while(changed);



        int idx = 0;
        while(digits[idx] == 0 && idx < digits.size())
            ++idx;

        cout << "Case #" << n << ": ";
        for(; idx < digits.size(); ++idx){
            cout << digits[idx];
        }
        cout << endl;

    }




}