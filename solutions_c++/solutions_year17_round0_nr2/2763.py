#include<iostream>
#include<string>
using namespace std;

int to_int(char &x){
  switch(x){
  case '0' : return 0;
  case '1' : return 1;
  case '2' : return 2;
  case '3' : return 3;
  case '4' : return 4;
  case '5' : return 5;
  case '6' : return 6;
  case '7' : return 7;
  case '8' : return 8;
  case '9' : return 9;
  }
  return 0;
}

void solve(){
  string input = "";
  long long int output = 0, consecutive = 1;
  cin >> input;
  
  while(!input.empty()){
    long long int buff = to_int(input[0]), output_buff = output % 10;

    if(output_buff <= buff){
      output = 10 * output + buff;
      input = input.substr(1);
    }
    else{
      output = consecutive * ((output / consecutive) - 1) + consecutive - 1;
      for(int l = input.length(); l != 0; l--)
	output = 10 * output + 9;
      break;
    }

    if(output_buff == buff)
      consecutive *= 10;
    else
      consecutive = 1;
    
  }
  cout << output;
}

int main(){
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++){
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }
  return 0;
}
