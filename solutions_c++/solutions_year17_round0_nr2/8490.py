#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <stdio.h>
#include <string.h>
#include <cstring>
#include <fstream>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
ofstream myfile;
char* answer;
int data[1003];
int output[1003];
int size;
int ans(string n,int index){
  string tmp = n;size=0;
  for(; size<tmp.length();size++){
    output[size] = tmp.at(tmp.length()-1-size)-48;
  }
  //printf("sz:%d\n",size);
  for(int i=0; i<size;i++){
//    printf("%d",output[i]);
  }
  printf("\n");
  output[size] = -3;
  for(int i=0; i<size; i++){
    if( output[i+1] <= output[i]){
      //output[i] = output[i];
    }else{ // 다른 구간, 앞의 수를 -1하고 뒤를 다 9로 만듬
      output[i+1] = output[i+1]-1;
      //printf("%d",output[i+1]);
      for(int ii=i;ii>=0;ii--){
      //  if(output[ii]==9) break;
        output[ii] = 9;
      }
    }
  }
  myfile << "Case #" << index << ": " ;
  for(int i=size-1; i>=0; i--){
    if(i==size-1&&output[i]<=0)continue;
    myfile << output[i];
    output[i] = 0;
  //  answer[i] = output[i];
  }
  myfile << endl;


  return 1;
}

int main() {
  int t, m; string n;

  myfile.open("AA.txt");
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    //memset(data,0,size);
    cin >> n ;  // read n and then m.
    ans(n,i);
    //myfile << "Case #" << i << ": " <<  << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  myfile.close();
}
