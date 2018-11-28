#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	/* code */	
	string s;
	int n, k, u, i, j, ans, len;
	long count;
	cin >> n;
	for (int u = 1; u <= n; u++)
        {
            cin >> s >> k;
            ans = 0;
            len = s.length();
            for(i = 0; i < len - k + 1; i++) {
                if (s[i] == '-') {
                    ans += 1;
                    for(j=0; j < k; j++) {
                    	if(s[i + j] == '+')
                        	s[i + j] = '-'; 
                        else 
                        	s[i + j] = '+';
                    }
                }
            }
	        if(s.find('-') != string::npos)
	        	cout << "Case #" << u << ": IMPOSSIBLE" << endl;
	        else
	        	cout << "Case #" << u << ": " << ans << endl;
        }
        return 0;
    }