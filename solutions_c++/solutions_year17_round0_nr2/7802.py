#include <iostream>
#include <string>
#include <stdio.h>
#include <sstream>

using namespace std;

string str, stroriginal;


string removeLeadingZero(string str)
{
  int counter = 0;
  string ans = "";
  for(int i = 0; i < str.length(); i++){
    if(str[i] == '0' && counter == 0) continue;
    ans += str[i];
    counter++;
  }

  return ans;
}

bool isTidy(string str)
{
  int size = str.length();
  if(size == 1) return true;

  for(int i = 1; i < size; i++){
    if(str[i] < str[i-1]) return false;
  }


  long long original = std::stoll(stroriginal);
  long long num = std::stoll(str);

  //return true;
  return num <= original;
}

string solve()
{
  if(isTidy(str)) return str;

  int size = str.length()-1;

  for(int i = size; i >= 1; i--){
    //if(str[i] <= str[i-1]){
      str[i] = '9';
      //str[i-1] = str[i-1] - 1;
      str[i-1] = (str[i-1] == '0') ? '9' : str[i-1] - 1;
      if(isTidy(str)) break;
    //}
  }

  return removeLeadingZero(str);
}

int main()
{
  int T;
  scanf("%d",&T);

  for(int test = 1; test <= T; test++){
    cin >> str;
    stroriginal = str;
    cout << "Case #"<< test <<": "<< solve() << '\n';
  }

  return 0;
}