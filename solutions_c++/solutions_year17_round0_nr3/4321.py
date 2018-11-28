#include <iostream>
#include <string> 
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int left(int n) {
    if (n==0) {
        return 0;
    }
    else {
        return (n-1)/2;
    }
}

int right(int n) {
    if (n==0) {
        return 0;
    }
    else {
        return (n-1) - (n-1)/2;
    }
}

void print (vector<int> x) {
    for (vector<int>::iterator it = x.begin(); it < x.end(); ++it) {
        cout << " " << *it;
    }
}

int allocate (int num, int k) {
    // Find i such that 2**i < K <= 2**(i+1)
    int i = 0;
    while (k >= pow(2,i)) {
        i++;
    }
    i--;
    // Loop through and compute vi
    vector<int> nms;
    nms.push_back(num);
    for (int j=0; j<i; j++) {
        vector<int> newnums;
        for (int m=0; m<nms.size(); m++) {
            newnums.push_back(left(nms[m]));
            newnums.push_back(right(nms[m]));
        }
        nms = newnums;
    }
    // Sort it and find the right element
    sort(nms.begin(), nms.end(), greater<int>());
    // print(nms);
    int w = k - pow(2,i);
    // cout << "W is " << w << " i is " << i << endl;
    return nms[w];
}

int main() {
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        int num;
        int k;
        cin >> num >> k;
        int z = allocate (num, k);
        if (k != 1) {
            cout << "Case #" << i+1 << ": " << right(z) << " " << left(z) << "\n";
        }
        else {
            cout << "Case #" << i+1 << ": " << right(num) << " " << left(num) << "\n";
        }
    }
	return 0;
}