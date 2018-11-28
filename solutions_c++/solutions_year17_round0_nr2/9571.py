#include <iostream>
#include <string>
using namespace std;

int main() {
  int T,dropplace;
  char A, B,dropchar;
  bool maybepile, nines;
  std::string maybestring;
  std::string N;
  std::string outstring;

  std::cin>>T;
  for (int t=1;t<=T;t++){
    //reset vars for each test
    maybepile=false;
    nines=false;
    maybestring = "";
    outstring="";
    N="";
    std::cin>>N;
    //print output template
    std::cout <<"Case #" << t << ": ";

    //Edge Case: 1 digit number
    if(N.length()==1){
      std::cout << N <<std::endl;
      continue;
    }


    for(int i=0;i<N.length()-1;i++){
      //set A and B
      A=N[i];
      B=N[i+1];
  //    std::cout <<"i: " << i << " A: " << A << " B: " << B <<std::endl;
      //Case 1: A smaller than B
      if(A<B){
        //Merge Maybe
        if(maybepile){
          maybepile=false;
          outstring += maybestring;

          maybestring="";
        }
        //Add current digit to output
        outstring += A;
      }
      //Case 2: A equals B
      if(A==B){
        if(maybepile==false){
          maybepile=true;
    //      std::cout << "Apre: " <<A;
          dropchar=(--A);
          A++;
  //        std::cout << "Apost: " << A <<std::endl;
          dropplace=i;
        }
        maybestring +=A;
      }
      //Case 3: A bigger than B
      if(A>B){
        if(!maybepile){
          dropchar=--A;
          A++;
          dropplace=i;

        }

  //      std::cout << "Start Final - Dropchar: " << A << " Dropplace: " << i <<std::endl;
       if(dropchar!='0'){outstring+= dropchar;} //only zero if N starts with 10...
  //      std::cout << "Outstring - pre-9's: " << outstring << std::endl;
        nines=true;
        while(dropplace<N.length()-1){
          outstring+='9';
  //        std::cout << "Outstring-update: " << outstring << std::endl;
          dropplace++;
        }
        maybepile=false; //Don't want to use the maybepile
        break;
      }
    }
    if(maybepile){outstring+=maybestring;}
    if(!nines){ outstring+=B;}
//    std::cout<<"Printing answer: ";
    std::cout<<outstring<< std::endl;
  }
}
