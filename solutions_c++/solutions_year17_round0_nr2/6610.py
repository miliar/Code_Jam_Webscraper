#include <algorithm>  // std::reverse
#include <deque>     //
#include<iostream>
#include<fstream>

using namespace std;
using std::deque;

void save(const deque<char>& dq, ofstream& os) {
  for (int i=0; i<dq.size();++i)
    os << dq[i];
}

int main()
{
  ifstream INP("in");
  ofstream OUT("out");
  if(!INP || !OUT)
    cout<<"File error"<<endl;
  else {
    int T;
    INP >> T;
    
    for (int i = 0; i < T ; i++){
      deque<char> v;
      char c = INP.get();

      while (c=='\n')
        c = INP.get();

      //read v
      while (c!='\n' && !INP.eof()){
          v.push_back(c);
          c = INP.get();
      }
    
      for (int j=v.size()-1; j>0 ; --j) {
        if (v[j] < v[j-1]) {
          for (int k = j; k<v.size(); ++k)
            v[k] = '9';
          v[j-1] -=1; //  N.B.: v[j-1] was > 0
        }
      } 
      
      // remove leading zero
      if (v[0] == '0') v.pop_front();


      // save data
      OUT <<"Case #"<<i+1<<": ";
      save(v,OUT);
        if (i+1 < T)  
          OUT<<endl;
    }

     INP.close();
     OUT.close();
  }
}
