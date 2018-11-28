#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int main()
{ int n ;
ifstream inp ;
ofstream outp ;
inp.open("input.txt");
outp.open("output.txt");

inp>>n ;
cout << n<<endl;
string s;
for (int i=1 ;i<=n ;i++){
bool b=true;
 int compte = 0;
s="" ;
inp>>s ;cout<<s<<endl;

 int l =s.length();cout<<l<<endl;
 int r;
  inp>> r;
  cout<<r<<endl;
 int v = l-r;

 for (int j=0 ;j<=v ;j++){
    char w = s[j];
    if (w=='-'){
            compte++;
    for (int k=j ;k<j+r ;k++){

        if (s[k]=='-'){
            s[k]='+';
        } else s[k]='-';      }

                 }

 }
 int c = l-r;
 int d=c+r;
 for (int a=c ;a<d ;a++){
    if (s[a]=='-'){b=false;}
 }
if (!b){outp<< "Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;}
else {
        outp<< "Case #"<<i<<": "<<compte<<endl;}
 }






    return 0;
}

