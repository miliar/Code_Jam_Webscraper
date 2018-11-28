#include <iostream>
#include <string>

using namespace std; 
 
int main(int argc, char *argv[]) { 
	
    int tests;
    cin >> tests;
    
    for (int t = 1; t <= tests; t++) {
        long long ans;
        cin >> ans;
        string temp = to_string(ans);
        bool invalid = true;
        while (invalid) {
            invalid = false;
            for(int i = 0; i < temp.size()-1; i++) {
                if (temp[i] > temp[i+1]) {
                    for (int j = i+1; j < temp.size(); j++) {
                        temp[j] = '0';
                    }
                    ans = stoll(temp);
                    ans -= 1;
                    temp = to_string(ans);
                    invalid = true;
                    break;
                } 
            }
        }
        
        cout << "Case #" << t << ": " << ans << endl;
    }
    
    
	return 0; 
} 
