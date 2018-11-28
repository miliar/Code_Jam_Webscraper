#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


int get_degit(long long int num)
{
  int digit = 0;
  while(num!=0){
    num /= 10;
    digit++;
  }
  return digit;
}

long long int pow_10(int num)
{
  long long int re;
  re = 1;
  for(int i = 0; i < num; i++){
    re = re * 10;
  }
  return re;
}

long long int get_num(long long int value, int num)
{
  return (value / pow_10(num)) % 10;
}


int main()
{
  int n, degit;
  long long int v;
  cin >> n;
  for(int i = 0; i < n; i++){
    cin >> v;
    degit = get_degit(v);
    for(int j = 0; j < degit ; j++){
        if(get_num(v, j) < get_num(v, j + 1)){
          v = v - (v % pow_10(j + 1)) - 1;
          degit = get_degit(v);
        }   
    }
    cout << "Case #" << i + 1 << ": " << v << endl;
  }
  return 0;
}

