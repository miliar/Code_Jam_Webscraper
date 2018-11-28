#include <iostream>
#include <fstream>
#include <string>
#include <limits.h>
using namespace std;

string solution(long long int);

bool check(long long int);


class solution{
  string gg;
};




int main(){
  ofstream OUT("out.txt");

  int T;
  cin >> T;
  for(int i=1;i<=T;i++){
    long long int buffer;
    int K;
    cin >> buffer;
    string answer = "Case #";
    answer += to_string(i);
    answer += ": ";
    //string gg = solution(buffer,K);
    answer.append(solution(buffer));
    answer += "\n";

    cout << answer;
    OUT << answer;

  }

  return 0;
}

//111111111111111110 size=18 ans-
//99999999999999999
//count = 16
//1 > 0 ? YES

//1100 size=4 ans-999
//count=1
//

//5500 size=4 ans-4999

//1000 size=4
string solution(long long int n){
  long long int x=n;
  for(long long int i=0;i<n;i++){
    if(x % 100000000 == 0)
      cout << "test: " << x << endl;
    if(check(x)) return to_string(x);
    else x -= 1;
  }
}

bool check(long long int N){
  string str = to_string(N);
  for(int i=1;i<str.size();i++){
    if(str[i] < str[i-1]) return false;
  }
  return true;
}

string solution1(string in){
  if(in.size()==1)
    return in;

  string result;
  int count = 0;
  for(int i=1;i<in.size();i++){
    if(in[i-1] > in[i]){
      if(count == 0){
        if(in[i-1]-1 != '0')
          result.push_back(in[i-1]-1);
        for(int j=0;j<in.size()-i;j++){
          result.push_back('9');
        }
        return result;
      }
      else{

      }
    }
    else if(in[i-1] < in[i]){
      result.push_back(in[i-1]);
      if(i == in.size()-1)
        result.push_back(in[i]);
    }
    else{
      count++;
      result.push_back(in[i]);
    }
  }
  return result;
}
