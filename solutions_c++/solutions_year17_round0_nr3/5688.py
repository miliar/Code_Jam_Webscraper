//#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

void partition(vector<pair<unsigned long long, unsigned long long>>& stalls, unsigned long long k)
{
    if (k <= 1)
        return;

    auto choice = stalls.back();
    if (choice.second >= k)
        return;

    stalls.pop_back();

    if (choice.first % 2) {
        // odd - two same sizes
        if (stalls.size() > 0 && stalls.at(0).first == choice.first / 2) {
            stalls.at(0).second += choice.second * 2;
        } else {
            stalls.insert(stalls.begin(), make_pair(choice.first / 2, choice.second * 2));
        }
    } else {
        // even - two different sizes
        if (stalls.size() > 0 && stalls.at(0).first == choice.first / 2 - 1) {
            stalls.at(0).second += choice.second;
        } else {
            stalls.insert(stalls.begin(), make_pair(choice.first / 2 - 1, choice.second));
        }

        if (stalls.size() > 1 && stalls.at(1).first == choice.first / 2) {
            stalls.at(1).second += choice.second;
        } else {
            auto it = stalls.begin();
            stalls.insert(++it, make_pair(choice.first / 2, choice.second));
        }
    }

    partition(stalls, k - choice.second);
}


void findAnswer(unsigned long long n, unsigned long long k)
{
    vector<pair<unsigned long long, unsigned long long>> stalls;
    stalls.push_back(make_pair(n, 1));
    partition(stalls, k);
    
    auto choice = stalls.back().first;

    auto max = choice / 2;
    auto min = (choice % 2) ? max : (max == 0) ? max : max - 1;
    cout << max << " " << min << endl;
}


int main(int argc, char* argv[])
{
    int t;
    cin >> t;

    unsigned long long n;
    unsigned long long k;
    for (int i = 1; i <= t; ++i) {
        cin >> n >> k;
        cout << "Case #" << i << ": ";
        findAnswer(n, k);
    }

    return 0;
}
