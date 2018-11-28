
#include <bits/stdc++.h>
#include <math.h>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::int128_t;
using namespace std;

int main()
{
    int t; cin >> t;
    for(int k=0;k<t;k++){
        int n;
        cin >> n ;
        string str = to_string(n);
        sort(str.begin(),str.end());
        if(str==to_string(n)){
            //cout << n << endl ;
            cout << "Case #"<< k+1 <<": " << str << endl;
            
        }
        else{
        for(int i=n-1;i>0;i--){
            str = to_string(i);
            sort(str.begin(),str.end());
            if(str==to_string(i)){
                cout << "Case #"<< k+1 <<": "<< str << endl; break;
            }
        }
        }
    }
    
    return 0;
}
