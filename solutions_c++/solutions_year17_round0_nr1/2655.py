#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int tt = 1; tt <= t; tt++){
        string s;
        int n;
        cin >> s >> n;
        int niza[s.size()+1];
        memset(niza, 0, sizeof(niza));
        int flips = 0;
        int cnt = 0;

        for(int i=0; i<s.size(); i++){
            if(i+n > s.size()){
            	cnt -= niza[i];
            	if((s[i] == '-' && cnt%2 == 0) || (s[i] == '+' && cnt%2 == 1)){
            		flips = -1;
            		break;
            	}
            } else {
				cnt -= niza[i];
				if((s[i] == '-' && cnt%2 == 0) || (s[i] == '+' && cnt%2 == 1)){
					cnt ++;
					flips++;
					niza[i + n] = 1;
				}
            }
        }
        if(flips == -1){
        	cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
        } else {
        	cout << "Case #" << tt << ": " << flips << endl;
        }
    }
    return 0;
}

