#include <iostream>
#include <algorithm>
using namespace std;

/*
bool check(int a[], int x){

  for(int i = 0; i< x;i++){
    if(a[i] <= a[i+1]){
      continue;
    }
    else{
      return false;
    }
  }

  return true;
}

int main(){
  int t;
  cin >>t;
  t++;
  for (int i= 0; i < t; i++){
    string n;
    int a[10000000000000000000] = {0};
    cin >>n;
    int x = n.length() -1;
    for(int j = 0; j <n.length();j++){
        a[j] = n[j] - '0';
    }

    for(int y=x; y >=0; y--){
      if(a[y] == 0){
        continue;
      }

    }

  }


  return 0;
}
*/

bool check(int n){
  int a[1000000];
  int c = 0;
  for(int i=6;i >=0;i--){
    a[i]=n%10;
    n/=10;
    c++;
  }
  //cout <<c<<endl;

  /*for(int i = 0;i < c;i++){
    cout<<a[i];
  }
  cout <<endl;*/

  for(int i = 0;i<c-1;i++){
    //cout <<a[i]<<a[i+1]<<endl;
    if(a[i] >a[i+1]){
      //cout <<a[i]<<a[i+1]<<endl;
      return false;
    }
  }
  //cout <<'x'<<endl;
  return true;

}

int main(){
  int t;
  cin >>t;
  t++;
  for (int i= 1; i < t; i++){
    int n;
    cin >> n;
    bool x = false;
    while(x == false){
      x = check(n);
      n--;
    }
    cout<<"Case #"<<i<<": ";
    cout <<n+1<<endl;
  }


  return 0;
}
