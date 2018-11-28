#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main() {
	int T,cases = 1;
	cin>>T;
	for (cases = 1; cases <= T;cases++) {
        string s;
        int n,flips = 0,slen;
        bool possible = true;
        cin>>s>>n;
        slen = s.length();
        for(int i = 0; i < slen; i++) {
            if(s[i] == '-') {
                if( (i + n) > slen) {
                    possible = false;
                    break;
                }
                for ( int j = i; j < (i+n); j++) {
                    if ( s[j] == '-')
                        s[j] = '+';
                    else s[j] = '-';
                }
                flips ++;
            }
        }
        if ( possible == true ) 
            cout<<"Case #"<<cases<<": "<<flips<<endl;
        else    
            cout<<"Case #"<<cases<<": "<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
