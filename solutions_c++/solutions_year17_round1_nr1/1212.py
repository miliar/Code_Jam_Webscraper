#include <bits/stdc++.h>

using namespace std;
vector<string> s(44);

int main (){
	freopen("a.inp", "r", stdin);
	freopen("a.out", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
	    int r, c;
	    cin >> r >> c;
	    for (int i = 0; i < r; i++){
	        cin >> s[i];
	        for (int j = 0; j < c; j++){
	        	if (s[i][j] != '?'){
	        		for (int k = j - 1; k >= 0; k--){
	        			if (s[i][k] != '?') break;
	        			s[i][k] = s[i][j]; 
	        		}
	        		for (int k = j + 1; k < c; k++){
	        			if (s[i][k] != '?') break;
	        			s[i][k] = s[i][j];
	        		}
	        	}
	        }
	        for (int j = 0; j < c; j++){
	        	for (int k = i - 1; k >= 0; k--){
	        		if (t == 2 && i == 2 && j == 3){
	        		}
	        		if (s[k][j] != '?') break;
	        		s[k][j] = s[i][j];
	        	}
	        }

	    }
	    for (int i = 0; i < r; i++){
	    	for (int j = 0; j < c; j++){
	    		for (int k = i+1; k < r; k++){
	    			if (s[k][j] != '?') break;
	    			s[k][j] = s[i][j];
	    		}
	    	}
	    }
	    cout << "Case #" << t << ":" << endl;
	    for (int i = 0; i < r; i++){
	    	cout << s[i] << endl;
	    }
	}

    return 0;
}
