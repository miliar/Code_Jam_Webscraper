#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string solution(string,int);
void flip(int start,int k,string &in);

int main(){
  ofstream OUT("out.txt");

  int T;
  cin >> T;
  for(int i=1;i<=T;i++){
    string buffer;
    int K;
    cin >> buffer;
    cin >> K;
    string answer = "Case #";
    answer += to_string(i);
    answer += ": ";
    //string gg = solution(buffer,K);
    answer.append(solution(buffer,K));
    answer += "\n";

    cout << answer;
    OUT << answer;

  }

  return 0;
}

string solution(string in,int K){
  int count = 0;
  for(int i=0;i<in.size();i++){
    if(in[i] == '-'){
      if(i+K-1 < in.size()){
        flip(i,K,in);
        count++;
      }
      else return "IMPOSSIBLE";
    }
  }
  return to_string(count);
}

void flip(int start,int k,string &in){
  for(int i=0;i<k;i++){
    if(in[start+i] == '-') in[start+i]='+';
    else if(in[start+i] == '+') in[start+i]='-';
  }
}
