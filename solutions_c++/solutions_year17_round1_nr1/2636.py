#include <iostream>
using namespace std;

void printArr(char a[][100], int r, int s){
    f cout<<"Case #"<<a0<<":\n";
    for(int i = 0; i<r;i++)
    {
      for(int j = 0; j< s;j++)
      {
        cout<<a[i][j];
      }
      cout<<endl;
    }
}
int main(){
    
    char arr2[100][100],init_;
    int testCases,r,s,k;
    
    cin >> testCases;
    cin >> r >> s;
    
    for(int i = 0 ; i < r; i++)
        for(int j = 0 ; j < s ; j++)
            cin >> arr2[i][j];
        
        
    
  for(int i = 0 ; i < r ; i++){
        for(int j = 0 ; j < s ; j++){
            
                if(arr2[i][j] != '?'){
                   
                    init_ = arr2[i][j];
                    k = j+1;
                   while(arr2[i][k] =='?' && k<j){
                         arr2[i][k] = init_;
                        k++;
                      }
                   int z = j-1;
                   while(arr2[i][k1] =='?' && z>=0){
                       arr2[i][k1] = init_;
                       z--;
                  } 
                }
        }
     printArr(arr2,r,s);
            
            
            cout << endl;
    
  
    
    
    }}