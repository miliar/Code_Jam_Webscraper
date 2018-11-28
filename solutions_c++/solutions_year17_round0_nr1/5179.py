#include <iostream>  
#include <string>

using namespace std;  


int main() {
  int t, k,ans;
  string A,ans1 = "";
  cin >> t; 
  for (int i = 1; i <= t; ++i) {
    ans = 0;
    ans1 = "";
    cin >> A;
    cin >> k;
    
    if(k > (A.size())){
        cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
    }
    
    for(int j = 0;j<A.size();j++){
        if(j > ((A.size()) - k) && A[j] == '-'){
            ans1 = "IMPOSSIBLE"; 
            break;
        }
        else if(j <= A.size() - k && A[j] == '-'){
            ans++;
            for(int m = j ; m < j + k ; m++ ){
                if(A[m] == '+'){
                    A[m] = '-';
                }
                else if(A[m] == '-'){
                    A[m] = '+';
                }
            }
        }    
    }
    
    if(ans1 == "IMPOSSIBLE"){
        cout << "Case #" << i << ": " << ans1 << endl;
    }
    else{
        ans1 = to_string(ans);
        cout << "Case #" << i << ": " << ans1 << endl;
    } 
  } 
  return 0;
}
 