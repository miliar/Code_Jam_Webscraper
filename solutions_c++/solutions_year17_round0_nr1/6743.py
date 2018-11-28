#include <iostream>
#include <fstream>

using namespace std;

char current_state(char c, int flipcount){
  
  if(flipcount%2==0) return c;
  return (c=='+') ? '-' : '+';
}

void flip(int &count, int &flipcount, int fliparay[], int pos){
  count++; flipcount++;
  fliparay[pos] = 1;
}

int main()
{
  ifstream in; ofstream out;
  in.open("input.txt");
  out.open("output.txt");

  int t; in >> t;
  string s; int k;

  for(int i=1; i<=t; i++){
    in>>s; in>>k;

    int flipped = 0, flipcount = 0, count=0;
    int fliparay[s.length()] = {0};

    for(int j=0; j<s.length(); j++){
      if(current_state(s[j], flipcount) == '-'){
        if(j > (s.length()-k)){
          count=-1; break;
        }
        flip(count, flipcount, fliparay, j);
      }
      if(j>=k-1 && fliparay[j-k+1]==1){
        flipcount--;
      }
      // if(j==(flipos+k-1)){
      //   flipped=0;
      // }
    }

    out<<"Case #"<<i<<": ";
    if(count==-1) out<<"IMPOSSIBLE"<<endl;
    else out<<count<<endl;
  }

  return 0;
}
