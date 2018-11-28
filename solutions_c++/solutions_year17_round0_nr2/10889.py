#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main() {
  int n;
  cin>>n;
  int number[n];

  // Start the main loop
  for(int i=0; i<n; i++) {
    int num_final;
    cin>>number[i];
    for(int temp=1; temp<=number[i]; temp++){
      int c, d, x = 450, m=1;
      if(temp<10){
        num_final=temp;
      }
      else{
        d = temp;
        // Leave the condition of d=10 as It can't be in the answer.
        if(d>10){
          while(d>=1){
            if(d>10){
              c = d % 10;
              d = d / 10;
            }
            else {
              c = d;
              m = 4;
            }
            if(x == 450){
              x = c;
            }
            else{
              if(x>=c){
                x = c;
                if(d<10 && m == 4){
                  num_final = temp;
                  break;
                }
              }
              else{
                break;
              }
            }
          }
        }
      }
    }
    cout<<"case #"<<i+1<<": "<<num_final<<endl;
  }
  return 0;
}
