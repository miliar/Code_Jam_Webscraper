#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;



int jump_tidy (vector<int> & s) {

    int m = 9;
    
    for (int i=0; i<s.size()-1; ++i) {
        
        if (s[i] > m) {
            //  s[i] <= 0 < m
                --s[i];
                for(int k=i-1; k>=0; --k) {
                    s[k] = 9;
                }
                m = s[i];    
        } else if (s[i] <= 0) {
            //  s[i] <= 0 < m
                --s[i+1];
                for(int k=i; k>=0; --k) {
                    s[k] = 9;
                }
                m = 9;                
        } else {
            // 0 < s[i] < m;
            m = s[i];            
        }
        
        ///printf ("%d %d\n",s[i], m);
        
    }
    
    ///printf("%d %d\n", s[s.size()-1], m);
    if (s[s.size()-1]<=0) {
        s.pop_back();
    }  else if (s[s.size()-1] > m) {
        ///printf("--\n");
        --s[s.size()-1];
        m = 9;        
        for(int k=s.size()-2; k>=0; --k) {
            s[k] = 9;
        }        
    }
    
    return 0;
}

int main(int argc, char **argv)
{
	int T; cin >> T;
    
    for (int t=0; t<T ; ++t ){
        
        //int small; cin >> small;
        string big; cin >> big;
        vector<int>n;
        /*        
        for (;small > 0;) {
            n.push_back(small%10);
            small/=10;
        }
        */
        for(auto a: big) {
            int ia = a - '0';
            n.push_back(ia);
        }
        reverse(n.begin(),n.end()); 
   
        jump_tidy (n);
     
        printf("Case #%d: ", t+1);
        
        for (int t = n.size()-1; t>=0; --t) {
            cout << n[t];
        } 
        cout << endl;
        
//        printf("%d\n", answ);
   
    }
    
	return 0;
}
