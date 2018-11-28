#include<iostream>
#include<cstdlib>
#include<vector>
using namespace std;

bool is_tidy(long long n){
  while(n>=10){
    if(n%10 >= (n/10)%10){
      n = n/10;
    }else{
      return false;
    }
  }
  return true;
}

int main(){

  int t;
  cin >> t;
  long long n;
  for(int i = 1; i <= t; ++i){
    cin >> n;
    int a = n;
    for(long long j = 0; j<=n; ++j){
	if(is_tidy(n-j)){
	  cout << "Case #" << i << ": " << n-j << endl;
	  break;
	}
    }      
  }

return(0);
}

