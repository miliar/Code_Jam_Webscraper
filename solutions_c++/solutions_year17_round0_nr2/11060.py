#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;


bool isTidy(int n){
int last = 99;
    while(n > 0){
        int temp = n%10;
        if(temp > last) return false;
        last = n%10;
        n/=10;
    }
    return true;
}


int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    vector<int> tidy;
    for(int i=1; i<1010; i++){
         if(isTidy(i)) tidy.push_back(i);
    }
    for(int i=0; i<t; i++){
        int n;
        cin >> n;
        cout << "Case #" << i+1 << ": ";
        int pos = lower_bound(tidy.begin(), tidy.end(), n) - tidy.begin();
        if(tidy[pos] > n || pos == tidy.size()){
            cout << tidy[pos-1] << endl;
        }else{
            cout << tidy[pos] << endl;
        }
    }
    return 0;
}
