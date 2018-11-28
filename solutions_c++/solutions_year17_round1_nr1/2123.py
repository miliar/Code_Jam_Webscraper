#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <math.h>
#include <stdio.h>
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

bool check(string row[25], int r,int c){
    bool let = true;
    for(int i=0;i<r; i++){
        for (int j=0; j<c; j++) {
            if(row[i][j]=='?') {
                let = false;
            }
        }
    }
    return let;
}
void initialize(string row[25], int r,int c) {
    bool jumped = false;
    label:
    for(int i=0;i<r; i++){
        for (int j=0; j<c; j++) {
            
            if(row[i][j]!='?') {
                for (int k = 0; k<j;k++)
                {
                    if (row[i][k] == '?') {
                        row[i][k]=row[i][j];
                    }
                }
            }

        }
        for (int j=c-1; j>=0; j--){
            if(row[i][j]!='?') {
                for (int k = j; k<c;k++)
                {
                    if (row[i][k] == '?') {
                        row[i][k]=row[i][j];
                    }
                }
            }
        }
    }
    for (int i=0;i<r;i++) {
    
    int count = 0;

        for (int j = 0;  j< c; j++)
        {
            if (row[i][j] ==  '?')
            {
                ++ count;
            }
        }
    if (count == c) {
        for (int j = 0;  j< c; j++){
            int steal=-1;
            if(i!=(r-1)) {
                
                for (int k=i+1; k<r;k++){
                    if(row[k][j]!='?'){
                        steal = k;
                        break;
                    }
                }
            }
            if(steal==-1 && i!=0){
                
                for (int k=i-1; k>=0;k--){
                    if(row[k][j]!='?'){
                        steal = k;
                        break;
                    }
                }

                
            }
            if(steal == -1){
                cout<<steal<<"STEAK "<<i<<" "<<j<<" "<<endl;
            }
           
            row[i][j]=row[steal][j];
    }
    }
    }
    for(int i=0;i<r; i++){
        cout<<row[i]<<endl;
    }
    // if (check(row,r,c) == true) {
    //     for(int i=0;i<r; i++){
    //     cout<<row[i]<<endl;
    // }
    // }
    //  else if(check(row,r,c) == false && jumped == false){
    //     jumped = true;
    //     goto label;
    // }
    // else {
    //     for(int i=0;i<r; i++){
    //     cout<<row[i]<<endl;
    // }
    // }
    // //print the result
    
}

int main() {
  int t, r, c;
  string row[25];
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.


  for (int i = 1; i <= t; ++i) {
    cin >> r >> c;  // read n and then m.
    for(int j = 0; j<r;j++) {
            cin>>row[j];
    }
    //if(i==57){
        cout << "Case #" << i << ":"<<endl ;
    initialize(row,r,c);
  

  }

  return 0;
}