#include <bits/stdc++.h>
using namespace std;

int main()
{
    // cout << "Hello World!" << endl;
    int test;
    cin>>test;
    int all = test;
    while(test--) {
        int n , k;
        cin>>n>>k;
        int diff = n+1;
        map < int , int> s;
        s[diff] = +1;
        int ls , rs;
        map<int , int>::reverse_iterator rit;
        for(int i = 0 ; i < k ;i ++) {
            rit=s.rbegin(); 
            diff = rit->first;
            // cout<<diff<<" j"<<endl;
            s[diff] -= 1;
            if(s[diff] == 0)
            s.erase (diff);
            
            ls = diff/2;
            rs = diff - ls;
            s[ls] +=1;
            s[rs] +=1;
        }
        cout<<"Case #"<<all-test<<": "<<max(rs-1, ls-1)<<" "<<min(rs-1 , ls-1)<<endl;
    }
    return 0;
}

