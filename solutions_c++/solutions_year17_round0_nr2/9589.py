#include <iostream>

using namespace std;

int main(){
  int cases;
  cin >> cases;
  string cur_case;
  int last_tidy;
  int cur_dig;
  int prev_dig;
  bool done = false;
  for(int j=0;j<cases;++j){
    cin>>cur_case;
    int n = cur_case.length();
    for(int i = n-1;i>0;--i){
     if(cur_case[i] < cur_case[i-1]){
       cur_case[i-1] -= 1;
       for(int j=i;j<n;++j)
         cur_case[j] = '9';
      }
    }
    int i = 0;
    while(cur_case[i] == '0'){
      cur_case = cur_case.substr(1, n-1);
      --n;
    }   
    cout << "Case #" << j+1 << ": " << cur_case << endl;
  }
}

	
