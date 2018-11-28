#include <vector>
#include <string.h>
#include <iostream>
#include <sstream>
#include <map>

using namespace std;
bool cumple(string h){
  for (int i =1; i< h.size(); ++i){
    if (h[i-1] > h[i]){
      return false;
    }
  }
  return true;
}
void dinamicaLlenar(vector <string> &ay){
   for(unsigned long long i =1; i< 10001; ++i){
     stringstream ss;
      ss << i;
      string str = ss.str();
      if(cumple(str)){
        ay.push_back(str);
      }
   }
}
string  buscar(string num,vector <string> ay){
  stoi(num);
  for(int i =1; i< ay.size();++i){
    if(stoi(ay[i-1])==stoi(num)){
      return num;
    }
    if(stoi(ay[i-1])<stoi(num) && stoi(num)<stoi(ay[i])){
      return ay[i-1];
    }
  }
}
int main(){
  int t;
  cin>>t;
  vector <string> ay;
  dinamicaLlenar(ay);
  for(int i=0; i< t;++i){
    string num;
    cin>>num;
    cout<<"Case #"<<i+1<<": "<<buscar(num,ay)<<endl;
  }
  return 0;
}
