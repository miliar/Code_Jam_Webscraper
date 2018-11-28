#include <iostream>
 
using namespace std;


int main(void) {
    int t=0;
    cin >> t;

    for (int x=1; x<=t; x++) {
        string s;
        cin >> s;
        int k;
        cin >> k;
        int flips=0;

        int length=s.length();

        for (int i=0; i<length-k+1; i++){
            if (s[i]!='+'){
                flips++;

                for (int j=0; j<k; j++){
                    if (s[i+j]!='+'){
                        s[i+j]='+';
                    } else {
                        s[i+j]='-';
                    }
                }
            }
        }

        bool impossible = false;
        for (int i=length-k+1; i<length; i++){
            if (s[i]!='+'){
                impossible=true;
                break;
            }
        }

        //Case #3: IMPOSSIBLE
        if (impossible){
            cout << "Case #" << x << ": IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << x << ": " << flips << endl;
        }


    }
    return 0;
}