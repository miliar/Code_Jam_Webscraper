#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream in("input1.in");
    ofstream out("output1.out");
    out.precision(21);
    int t;
    in >> t;
    for(int i =0;i<t;i++){
        double d;
        int n;
        in >> d >> n;
        pair<double,double> A[n];
        for(int j =0;j<n;j++) {
                in >> A[j].first >> A[j].second;
        }
        double mn = -1;
        for(int j =0;j<n;j++){
            if(mn < (d - A[j].first)/A[j].second) {
                mn = (d - A[j].first)/A[j].second;
            }
        }
       out << "Case #" << i+1 << ": " << d / mn <<endl;
    }

    return 0;
}
