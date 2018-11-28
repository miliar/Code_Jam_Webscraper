#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream in("input2.in");
    ofstream out("output2.out");
    int t;
    in >> t;
    for(int i =0;i<t;i++){
        int n,k;
        in >> n>> k;
        map<int,int> v;
        v[n] = 1;
        while(k>1) {
        auto x = v.rbegin();
        int val = x->first;
        val--;
        if(val/2 !=0){
        v[val/2]++;
        }
        if(val - val/2 !=0){
          v[val - val/2]++;
        }
        v[val+1]--;
        if(v[val+1]==0) v.erase(val+1);
        k--;
        }
       auto x = v.rbegin();
       int x1 = x->first;
       out << "Case #" << i+1 << ": " <<  max((x1-1)/2,(x1-1) - ((x1-1)/2)) << " " <<min((x1-1)/2,(x1-1) - ((x1-1)/2))  <<endl;
    }

    return 0;
}
