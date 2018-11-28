#include <iostream> 
using namespace std;

 
long test(long n){
    long a[18] = {-1};
    long temp = n;
    bool mainBreak=false;
    for(long i = 0; i< n && !mainBreak; i++){
        unsigned int number_of_digits = 0;
        do {
         ++number_of_digits;
         a[number_of_digits-1] = temp % 10;
         temp /= 10;
        } while (temp);

        for(int j = 0; j< number_of_digits; ++j){
            if(a[j] < a[j+1] && a[j]!=-1){
                n = n-1;
                temp = n;
              
                break;
            }else if( j+1 == number_of_digits) {
               
                 mainBreak = true;
                break;
            }
        }
    }
  return n;
}
 
int main() {
  long t, n;
  cin >> t; 
  for (int i = 1; i <= t; ++i) {
    cin >> n ;  
    cout << "Case #" << i << ": " << test(n) <<  endl;
  }
  return 0;
}
