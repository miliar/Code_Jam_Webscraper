#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	int n;
	cin >> n;

	for(int j = 0; j < n; ++j)
	{
		string s;
		int num;
		cin >> s >> num;
		
		long long int ans = 0;
		for(int i = 0; i <= s.length() - num; ++i){
    	    if(s[i]=='-'){
    	    	++ans;
    	    	for(int k = 0; k < num; ++k){
    	    		if(s[i + k] == '-'){
    					s[i + k] = '+';
    				}
    				else{
    					s[i + k] = '-';
    				}
    			}
    		}
    	}
 
		bool correct = true;
		for (int i = 0; i < s.length(); ++i) {
			if (s[i] == '-') correct = false;
		}

		if (correct) {
			cout << "Case #" << j + 1 << ": " << ans << endl;
		} else {
			cout << "Case #" << j + 1 << ": " << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}