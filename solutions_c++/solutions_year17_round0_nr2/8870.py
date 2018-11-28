#include <iostream>
#include <fstream>

using namespace std;
bool is_sorted(int num);
int main(){
 ifstream infile;
 ofstream outfile;

  int n, i,j, num;
 infile.open("SMALL_DATA_SET.txt");
 outfile.open("SOLUTION_SMALL_DATA_SET.txt");

  infile>>n;

  for(i=0; i<n; i++){
      infile>>num;
      for(j=num; ;j--){
        if(is_sorted(j)){
         outfile<<"Case #"<<i+1<<": "<<j<<endl;
         break;
        }
      }
  }

 infile.close();
 outfile.close();
 return 0;
}
bool is_sorted(int num){
  int digits[4]={0},i=3,j;

  while(num>0){
    digits[i]=num%10;
    num/=10;
    i--;
  }
   for(i=0; i<4; i++){
     for(j=i;j<4; j++){
        if(digits[i]>digits[j])
            return false;
     }
   }
   return true;
}
