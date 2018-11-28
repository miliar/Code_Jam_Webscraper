#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int tt = 1; tt <= t; tt++){
    	cout << "Case #" << tt << ": ";
    	string s;
    	cin >> s;
    	int last = s.size();
    	for(int i=s.size()-1; i>0; i--){
    		if(s[i] < s[i-1]){
    			s[i-1] --;
    			for(int j=i; j<last; j++){
    				s[j] = '9';
    			}
    			last = i;
    		}
    	}
    	int c = 0;
    	while(s[c] == '0') c++;
    	cout << s.substr(c, s.size()-c) << endl;

    }
    return 0;
}

