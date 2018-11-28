#include<iostream>

using namespace std;

int main(){
  int c;
  cin >> c;
  for(int cur =1; cur <= c; cur++){
    cin.ignore();
    string N;
    cin >> N;

    int i = 1, l = N.length();
    bool tidy = false;
    while(!tidy && i < l){
      if(N[i]<N[i-1]){
	int j = i-1;
	while(j>=1 && N[j]==N[j-1])
	  j--;
	N[j] = (char)(N[j]-1);
	for(int k = j+1; k < l; k++)
	  N[k]='9';
	tidy = true;
      }
      i++;
    }

    if(N[0]=='0')
      N=N.substr(1,l-1);
    
  cout << "Case #" << cur << ": " << N << endl;
  
  }

}
