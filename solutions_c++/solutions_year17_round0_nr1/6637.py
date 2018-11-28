#include <algorithm>  // std::reverse
#include <vector>     // std::vector
#include<iostream>
#include<fstream>

using namespace std;

// precondition : pos + k <= size of vector of pancakes
void flip(vector<char>& v,int pos, int k){ // k = size of the pancake flipper
  for (int i=pos;i<pos+k;++i){
    v[i] = (v[i] == '+') ? '-' : '+';
  }
}
// postcondition : v[pos..pos+k-1] pancake flipped


int solve(vector<char>& v, int k){
  int count = 0;
  for (int i = 0; i < v.size()-k+1;++i ){
    if (v[i]=='-') {
      flip(v,i,k);
      ++count;
    }
  }

  bool imp = false;
  for (int i = v.size()-k+1; i<v.size() && !imp;++i) {
    if (v[i] == '-') {
    imp = true;
    }
  }
  return imp ?  -1 : count;
}

int main()
{
  ifstream INP("in");
  ofstream OUT("out");
  if(!INP || !OUT)
    cout<<"File Error"<<endl;
  else {
    int T;
    INP >> T;

    for (int i = 0; i < T ; i++){
      vector<char> v;
      char c = INP.get();

      while (c=='\n')
        c = INP.get();

      //leggo v
      while (c!='\n' && c!=' ' && !INP.eof()){
          v.push_back(c);
          c = INP.get();
      }

      int k;
      INP>>k;

      int sol = solve(v, k);

      OUT <<"Case #"<<i+1<<": ";
      if (sol < 0)
        OUT << "IMPOSSIBLE";
      else
        OUT<< sol;

      if (i+1 < T)
        OUT<<endl;
     }

     INP.close();
     OUT.close();
  }
}

