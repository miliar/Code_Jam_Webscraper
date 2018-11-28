//
// Created by Snehil Vishwakarma on 4/7/17.
//
// Bathroom Stalls

#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <string>
#include <numeric>

using namespace std;

int main() {
    int T;
    long long n,k,temp,temp2;
    cin>>T;
    for(int i=0; i<T; ++i)
    {
        cin>>n>>k;

        priority_queue<long long> maxdiff;
        maxdiff.push(n);
        while(k>0)
        {
            temp = maxdiff.top();
            maxdiff.pop();
            if(temp%2==1)
            {
                temp = temp/2;
                temp2 = temp;
            }
            else
            {
                temp = temp/2;
                temp2 = temp-1;
            }
            maxdiff.push(temp);
            maxdiff.push(temp2);
            --k;
        }
        cout << "Case #" << (i+1) << ": " << temp << " " << temp2;
        if(i!=(T-1))
            cout << endl;
    }
    return 0;
}