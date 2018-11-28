#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

pair <long long, long long> findMax(vector <long long> stalls){
   pair <long long, long long> answer;
   long long etalon = 0;

   for (long long i = 1; i < stalls.size(); i++){
        if (stalls[i] - stalls[i-1] > etalon)
        {
            etalon = stalls[i] - stalls[i-1];
            answer = {stalls[i-1], stalls[i]};
        }
   }

   return answer;
}

pair <long long, long long> findAnswer(long long n, long long k){
    vector <long long> stalls = {0, n+1};
    pair <long long, long long> l_r;
    long long newStall;

    for (long long i = 0; i < k; i++){
        l_r = findMax(stalls);
        newStall = l_r.first + (l_r.second - l_r.first)/2;
        stalls.push_back(newStall);
        sort(stalls.begin(), stalls.end());
    }

    pair <long long, long long> answer = {l_r.second - newStall - 1, newStall - l_r.first - 1};
    return answer;
}

int main(){
    int cases;

    cin >> cases;

    for (int i = 0; i < cases; i++){
        long long n, k;
        cin >> n >> k;
        pair <long long, long long> answer = findAnswer(n, k);
        cout << "Case #" << i+1 << ": " << answer.first << " " << answer.second << endl;;
    }

    return 0;
}
