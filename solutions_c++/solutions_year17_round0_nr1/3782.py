#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream in("input1.in");
    ofstream out("output1.out");
    int t;
    in >> t;
    for(int j =0;j<t;j++){
       string a;
       in >> a;
       int k;
       in >> k;
       int ans =0;
       for(int i =0;i<=a.length()-k;i++){
        if(a[i] == '-') {
           for(int s =i;s<i+k;s++){
             if(a[s]=='-') a[s] = '+';
             else a[s] = '-';
           }
           ans++;
        }
       }
       bool x = false;
       for(int i =0;i<a.length();i++){
        if(a[i] == '-') x= true;
        }
        out << "Case #" << j+1 << ": ";
        if(!x) out << ans <<endl;
        else out << "IMPOSSIBLE" <<endl;
    }

    return 0;
}
