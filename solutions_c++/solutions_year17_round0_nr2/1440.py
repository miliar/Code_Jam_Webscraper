#include <bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	long long T, cas, i, flag, j;
	string s;
	
	cin >> T;
	for(cas=1;cas<=T;cas++){
	    cout << "Case #" << cas << ": ";
	    cin >> s;
	    while(1){
	        for(i=1;i<s.size();i++){
	            if(s[i-1]>s[i]){
	                s[i-1]--;
	                for(j=i;j<s.size();j++){
	                    s[j] = '9';
	                }  
	                break;
	            }
	        }
	        if(i==s.size()) break;
        }
        for(i=0;i<s.size();i++){
	        if(s[i]>'0') break;
	    }
	    for(;i<s.size();i++){
	        cout << s[i];
	    }
	    cout << '\n';
	}
	return 0;
}
