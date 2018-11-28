//
//  main.cpp
//  PancakeFlipper
//
//  Created by Tab on 08/04/2017.
//  Copyright © 2017 Tab. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;
void quickSort(vector<int>& x,int left, int right){
    if (left>=right) {
        return;
    }
    int pivot = (x[left]+x[right])/2;
    int i = left;
    int j = right;
    while (i<j) {
        while (x[i]<=pivot && i<j) {
            ++i;
        }
        while (x[j]>pivot && j>i) {
            --j;
        }
        if (i<j) {
            int temp = x[i];
            x[i] = x[j];
            x[j] = temp;
        }
    }
    quickSort(x, left, i-1);
    quickSort(x, i, right);
}

void enterTheBathroom(int lastMaxEmptyNum, int n, int& Ls, int& Rs){
    vector<int> emptys;
    int ls = Ls;
    int rs = Rs;
    if (lastMaxEmptyNum==n) {
        Ls = 0;
        Rs = 0;
        return;
    }
    for (int i=1; i<=n; ++i) {
        ls = lastMaxEmptyNum/2;
        rs = (lastMaxEmptyNum-1)/2;
        if (i==1) {
            lastMaxEmptyNum = ls;
            emptys.push_back(rs);
        }else{
            if (ls>0) {
                emptys.push_back(ls);
            }
            if (rs>0) {
                emptys.push_back(rs);
            }
            quickSort(emptys,0,emptys.size()-1);
            lastMaxEmptyNum = emptys.back();
            emptys.pop_back();
        }
        if (i==n) {
            Ls=ls;
            Rs=rs;
        }
    }
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int t;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        int n,k;
        cin >> n>>k;  // read n and then m.
        int Ls,Rs;
        enterTheBathroom(n, k, Ls, Rs);
        cout << "Case #" << i << ": " <<Ls<<" "<<Rs<< endl;
        // cout knows that n + m and n * m are ints, and prints them accordingly.
        // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    }
    return 0;
}
