#include <iostream>
#include <string>

using namespace std;

int main(){
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        string ss;
        int k;
        cin >> ss;
        cin >> k;

        int count = 0;
        bool possible = true;
        int j = 0;

        while (j < ss.size()) {
            if (ss[j] == '-') {
                if (j < ss.size() - k) {
                    for (int p = 0; p < k; p++) {
                        if (ss[j + p] == '-') ss.replace(j+p, 1, 1, '+');
                        else ss.replace(j+p, 1, 1, '-');
                    }
                    count += 1;
                }
		else if (j == ss.size() - k){
			for (int p = 0; p < k; p++){
			  if (ss[j+p] != '-') {
			    possible = false;
			    break;
			  }
		        }
			j += k;
			count += 1;
		}
                else {
                    possible = false;
                    break;
                }
	    }
	    j+=1;
	    //cout << j << ss << endl;
        }


        if (possible) {
            cout << "Case #" << i+1 << ": " << count << endl;
	}
        else {
            cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
	}
    }
    return 0;
}
