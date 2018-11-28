#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

string disp (string s, int ind);

int main () {
	
	int T;
	int tc;
	cin >> T;
    char c;
	string s;
    int l;

    getchar();

    for (tc=1;tc<=T;tc++){
        s = "";

        do {
            c = getchar();
            if (c != '\n') {
                s+=c;
            }
            
        } while(c != '\n');

        // cout << "s: " << s << endl;

        l = s.size();

        for (int i = 0; i < l-1; i++) {
            if ((int)s[i] > (int)s[i+1]) {
                s = disp(s, i);
                break;
            }
        }

        cout << "Case #" << tc << ": " << s << endl;
    } 
	
	return 0;
}

string disp (string s, int ind) {

    // cout << "s: " << s << " ind: " << ind << endl;

    s[ind] = (char)((int)s[ind] - 1);
    if (ind == 0 || (int)s[ind - 1]<=(int)s[ind]) {
        for(int i=ind+1;i<s.size();i++) {
            s[i] = '9';
        }

        if (s[0] == '0' && s.size() > 1) {
            s = s.substr(1, s.size()-1);
        }

        // cout << "ans: " << s << endl;

        return s;
    } else {
        return disp(s, ind-1);
    }
}
