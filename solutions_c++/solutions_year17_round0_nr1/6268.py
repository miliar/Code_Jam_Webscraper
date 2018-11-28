#include <iostream>
#include<fstream>
#include<string>

using namespace std;

int main(){
int t =0,s=0,fc=0,flipped = 1;
string p;
ifstream infile("A-large.in");
ofstream ofile("outfile.out");

infile >> t;

for (int j =1;j <= t;j++){
infile >> p;
infile >> s;
int size = p.length();
fc = 0;
flipped = 1;

for(int i=0;i< size; i++){
char c = p.at(i);
if (c == '+'){}
else if ( c == '-'){
if (i+s-1 < size){
 for (int j =0;j < s;j++){
  if ( p.at(i+j) == '-'){ p[i+j] = '+';}
  else if (p.at(i+j) == '+'){p[i+j] = '-';}
 }
fc++;
}

}

}

for(int i=0;i< size; i++){
 if (p.at(i) == '-'){
    flipped = 0;
    break;
 }
}

if(flipped){
    ofile << "Case #"<<j<<": "<<fc <<endl;
}
else {
    ofile << "Case #"<<j<<": "<<"IMPOSSIBLE" <<endl;
}

}


return 0;
}
