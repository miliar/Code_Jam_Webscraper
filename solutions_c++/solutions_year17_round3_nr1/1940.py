#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <algorithm>
#include <iomanip>  


using namespace std;

bool mysort(pair<int, int>a, pair<int, int>b){
    if (a.first != b.first){
        return a.first < b.first;
    } else {
        return a.second < b.second;
    }
}

unsigned long get_syrup(int n, int k, vector<pair<int, int> >& rh){

    sort(rh.begin(), rh.end(), mysort);

    unsigned long maxa = 0;

    for (int i = n-1; i >= k-1; i--){

        priority_queue<unsigned long>pq;

        for (int j = i - 1; j >= 0; j--){
            unsigned long temp = (unsigned long)rh[j].first * rh[j].second * 2;
            pq.push(temp);
        }

        unsigned long area = (unsigned long)rh[i].first * rh[i].second * 2 + (unsigned long)rh[i].first * rh[i].first;

        for (int j = 1; j < k; ++j){
            area += pq.top();
            pq.pop();
        }
        maxa = max(maxa, area);

    }
    return maxa;
}


int main(){

    ifstream infile("A-large.in");
    ofstream outfile("r1c1.out");

    int t;
    infile >> t;

    for (int acase = 0; acase < t; ++acase){
        int n, k;
        infile >> n >> k;
        vector<pair<int, int> >rh (n, pair<int, int>(0,0));
        for (int i = 0; i < n; ++i){
            infile >> rh[i].first >> rh[i].second;
        } 

        outfile << "Case #" << acase+1 << ": ";

        unsigned long result = get_syrup(n, k, rh);
        double addp = result * 3.141592653589793;
        outfile << setprecision(9) << fixed << addp << endl;



    }
}