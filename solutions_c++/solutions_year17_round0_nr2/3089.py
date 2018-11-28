#include <iostream>
#include <string>

using namespace std;

bool check(int a[]){
  for(int i = 0;i < 19;++i)
    if(a[i] < 0) return false;
  for(int i = 0;i < 18;++i)
    if(a[i + 1] < a[i]) return false;
  return true;
}

void print(int a[]){
  long long aux = 0;
  for(int i = 0;i < 19;++i){
    aux = aux * 10 + a[i];
  }
  cout << aux << "\n";
}

int main(){
  int T;
  cin >> T;

  int d[19],d2[19];

  for(int tc = 1;tc <= T;++tc){
    long long N;
    cin >> N;

    for(int i = 18;i >= 0;--i){
      d[i] = N % 10;
      N /= 10;
    }

    cout << "Case #" << tc << ": ";

    if(check(d)) print(d);
    else{
      for(int i = 18;i >= 0;--i){
        for(int j = 0;j < i;++j)
          d2[j] = d[j];
        d2[i] = d[i] - 1;
        for(int j = i + 1;j < 19;++j)
          d2[j] = 9;

        if(check(d2)){
          print(d2);
          break;
        }
      }
    }
  }

  return 0;
}
