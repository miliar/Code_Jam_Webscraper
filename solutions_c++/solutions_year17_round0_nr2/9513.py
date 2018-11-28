#include <iostream>

using namespace std;

int main(){
  int t;
  unsigned long long n,num;
  cin>>t;

  for(int i=1;i<=t;i++){
    cin>>n;
    
    num=n;
    
    while(num){

      if( (num%100)/10 <= (num%100)%10) num=num/10;
      else{
	n--;
	num=n;
      }
    }
    
    cout<<"Case #"<<i<<": "<<n<<endl;
      
  }
  
  return 0;
}
