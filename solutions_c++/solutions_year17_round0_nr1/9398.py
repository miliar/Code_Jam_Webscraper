#include <iostream>
#include <fstream>
using namespace std;

int main() {

 ifstream fin;
 ofstream fout;
 fout.open("prog1.txt");
 fin.open("A-large.in");

 int t;
 fin>>t;
 for(int z=0; z<t; z++){
  string s;
  fin>>s;
  int k;
  fin>>k;
  int i, c=0, n=0;
  for(i=0; i<s.size()-(k-1); i++){
    if(s[i]=='+'){
        c++;
        continue;
    }
    else{
        s[i] = '+';
        c++; n++;
        for(int j=i+1; j<i+k; j++){
            if(s[j]=='-')
                s[j] = '+';
            else
                s[j] = '-';
        }
    }
  }
  for(; i<s.size(); i++){
    if(s[i]=='+')
        c++;
  }

  if(c==s.size()){
    fout<<"Case #"<<z+1<<": "<<n<<endl;
    continue;
  }
  fout<<"Case #"<<z+1<<": "<<"IMPOSSIBLE"<<endl;
 }

 fin.close();
 fout.close();
 return 0;
}
