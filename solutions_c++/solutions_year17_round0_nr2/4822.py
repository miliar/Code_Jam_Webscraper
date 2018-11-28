#include <iostream>
 
using namespace std;


int main(void) {
    int t=0;
    cin >> t;

    for (int x=1; x<=t; x++) {
        string s;
        cin >> s;
        int length=s.length();

        for (int j=0; j< length; j++){
            bool fill9 = false;
            for (int i=0; i<length-1;i++){
                if (fill9){
                    s[i+1]='9';
                } else if (s[i]>s[i+1]){
                    // TODO: 2001

                    //0-1=...? won't happen. only nothing >0 will be in front?

                    // 549 -> 499
                    // 5>4
                    s[i]--;

                    s[i+1] = '9';

                    fill9=true;
                }
                
            }
            if (fill9){
                s[length-1]='9';
            }
        }

        for (int j=0; j< length; j++){
            if (s[0]=='0'){
                s= s.substr (1,-1); 
            }
        }
        
        cout << "Case #" << x << ": " << s << endl;
    }
    return 0;
}