#include<iostream>

using namespace std;

int main(){
  int c;
  cin >> c;
  for(int cur =1; cur <= c; cur++){
    cin.ignore();
    string s;
    cin >> s;
    int K;
    cin >> K;
    bool possible = true;
    
    int i = 0,res=0, l=s.length();
    while(i<l){
    if(s[i]=='-'){
      if(i+K-1<l){
	for(int j = 0; j < K; j++)
	  s[i+j] = (char)('+'+'-'-s[i+j]);
	res++;
      }else{
	possible = false;
      }
    }
    i++;
  }

  cout << "Case #" << cur << ": " << (possible?to_string(res):"IMPOSSIBLE")<< endl;
  
  }

}
