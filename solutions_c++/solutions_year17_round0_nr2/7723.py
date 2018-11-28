#include <iostream>
#include <fstream>
using namespace std;

int main()
{
  fstream ob;
  fstream ot;
  ot.open("outputs.txt",ios::out);
  ob.open("B-large.in",ios::in);
  string S,s;
  int T;
  ob>>T;
  int tc=0;
  while(T--){
    ob>>S;
    //cout<<S;
   int  chk=0,i,j;

  tc+=1;
  while(1){

    chk=0;
      for(i=0;i<S.length()-1;i++){
        if (int(S[i])>int(S[i+1])){
            //cout<<S[i]<<"here"<<endl;
            S[i]=char(int(S[i])-1);
            j=i+1;
            while(j<S.length()){
             S[j]='9';
             j++;
            }
            chk=1;
        }
      }
    if(chk==0){
        break;
    }
   }
   ot<<"Case #"<<tc<<": ";
    //cout<<"Case #"<<tc<<": ";
   if (S[0]=='0')
   ot<<S.substr(1);
   //cout<<S.substr(1);
   else
    //cout<<S;
    ot<<S;
  ot<<endl;
  //cout<<endl;
  }
}
