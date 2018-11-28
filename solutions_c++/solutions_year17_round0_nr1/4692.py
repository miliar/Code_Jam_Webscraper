#include<iostream>
#include<stack>
using namespace std;

stack<char> s1;

int check(string s, int n, int l, int j1){
  int i = 0, j, k, temp, temp1 = 0;
  int count1 = 0;
  while(i < n){
    
    for(i=0; i < n; i++){
      if(s[i] == '-'){
	if(i >= (n-l+1)){
	  cout << "Case #" <<j1<< ":" << " " << "IMPOSSIBLE" <<endl;
	  temp1 = 1;
	  break;
	}
	
	j = i;
	while(j < i + l){
	  
	  if(s[j] == '+'){
	    s[j] = '-';
	  }
	  else{
	    s[j] = '+';
	  }
	  j++;
	  
	}
	count1++;
      }
    }
    if(temp1 == 1){
      break;
    }
  }
  
  if(temp1 != 1){
    cout<< "Case #" << j1 << ":" << " " << count1 << endl;
  }
  return 0;
}

int main(){
  string s;
  int t;
  cin >> t;
  int j = 1;
  while(j <= t){
    
    int l;
    cin >> s;
    cin >> l;
    int n = s.length();
    int temp = check(s,n,l,j);
    j++;
  }
  return 0;
}
