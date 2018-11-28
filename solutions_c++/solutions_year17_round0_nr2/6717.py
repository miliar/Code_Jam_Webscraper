#include <iostream>
#include <fstream>

using namespace std;


int main()
{
  ifstream in; ofstream out;
  in.open("input.txt");
  out.open("output.txt");

  int t; in >> t;
  string n;

  for(int i=1; i<=t; i++){
    in>>n;

    // out<<n;
    out<<"Case #"<<i<<": ";
    int pos=-1, dig, dignext=(int) n[n.length()-1];
    for(int j=n.length()-2; j>=0; j--){
      dig = (int) n[j];
      if(dig > dignext){
        pos=j;
        dig--;
        n[j]=dig;
      }
      dignext = dig;
    }

    if(pos == -1){
      out<<n;
    }else if(pos==0 && n[pos]=='0'){
      for(int k=1; k<=n.length()-1; k++){
        out<<'9';
      }
    }else{
      for(int k=0; k<pos; k++){
        out<<n[k];
      }
      out<<n[pos];
      for(int k=pos+1; k<=n.length()-1; k++){
        out<<'9';
      }
    }
    out<<endl;

    
  }
  

  return 0;
}
