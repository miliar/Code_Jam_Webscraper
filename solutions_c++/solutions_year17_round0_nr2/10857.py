#include <iostream>
#include <string>
#include <vector>

using namespace std;

int isTidy(vector<int> x){
  int start=0;
  for(int i=0;i<x.size();i++){
    if(x[i]>0){start = i;break;}
  }
  for(int i=start;i<x.size()-1;i++){
    if(x[i]>x[i+1]){
      return -1;
    }
  }
  return 1;
}

void printvec(vector<int>x){
  int start=0;
  for(int i=0;i<x.size();i++){
    if(x[i]>0){start = i;break;}
  }
  for(int i=start;i<x.size();i++){
    cout << x[i];
  }
}

int main(){
  int T;
  string N;
  cin >> T;
  for(int i=0;i<T;i++){
    cin >> N;
    vector<int> a;
    for(int j=0;j<N.length();j++){
  		a.push_back(N[j]-'0');
  	}
    while(isTidy(a)==-1){
      //subtract 1 from vector
      for(int k=a.size();k>-1;k--){
        if(a[k]>0){
          a[k]=a[k]-1;
          break;
        }
        else{
          a[k]=9;
        }
      }
    }
    // print out the interger
    cout << "Case #" << i+1 << ": ";
    printvec(a);
    cout << "\n";
  }
}
