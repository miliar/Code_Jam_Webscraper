//
//  main.cpp
//  ssh hpl240@access.cims.nyu.edu
//  ssh energon1.cims.nyu.edu

#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <sstream>
#include <random>
#include <unordered_map>
#include <algorithm> // for sort()
using namespace std;


class interval{
public:
    interval(long long int l_ = 0 , long long int r_ = 0){
        l = l_;
        r = r_;
    }
    long long int l;
    long long int r;
};
bool comp (interval a, interval b) {
    if (a.r-a.l < b.r-b.l) {
        return true;
    }
    else if(a.r-a.l > b.r-b.l){
        return false;
    }
    else{ // ==
        return (a.l > b.l);
    }
}
interval findAns(long long int n, long long int k){
    vector<interval> data;
    interval temp(1,n-2);
    data.push_back(temp);
    while (k > 1) {
        sort(data.begin(), data.end(), comp);
        temp = data[data.size()-1];
        data.pop_back();
        long long int left = temp.l;
        long long int right = temp.r;
        long long int mid = (left + right)/2;
        temp.l = left;
        temp.r = mid-1;
        data.push_back(temp);
        temp.l = mid+1;
        temp.r = right;
        data.push_back(temp);
        --k;
    }
    sort(data.begin(), data.end(), comp);
    temp = data[data.size()-1];
    long long int m = (temp.l + temp.r)/2;
    
    interval ans(max(m-temp.l, temp.r-m), min(m-temp.l, temp.r-m));
    return ans;
}

int main(int argc, const char * argv[]) {
    /*Input */
    
    string filename = "/Users/xinpeilin/Desktop/Google_Code/C-small-1-attempt0.in";
    ifstream fin;
    fin.open(filename);
    if (fin.fail()) {
        cout << "Failed to open input file\n";
        exit(1);
    }
    long long int num = 0;
    vector<interval> ans;
    fin >> num;
    for (long long int i = 0; i < num; ++i) {
        long long int N = 0;
        long long int K = 0;
        fin >> N;
        fin >> K;
        interval inter = findAns(N+2, K);
        ans.push_back(inter);
    }
    
    
    fin.close();
    ofstream fout;
    fout.open("/Users/xinpeilin/Desktop/Google_Code/output_C-1.txt");
    for (long long int i = 0; i < ans.size(); ++i) {
        fout << "Case #" << i+1 << ": " << ans[i].l << " " << ans[i].r << endl;
    }
    fout.close();
    return 0;
}




