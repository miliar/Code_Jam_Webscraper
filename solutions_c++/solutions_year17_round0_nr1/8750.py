#include <iostream>
#include <fstream>

using namespace std;
void invert_string(string &pancake, int start, int k);
bool is_happy(string pancake);
bool can_invert(string pancake,int start, int k);
int find_index_of_blank(string pancake);
int main(){
 ifstream infile;
 ofstream outfile;

 infile.open("LARGE_DATA_SET.txt");
 outfile.open("SOLUTION_LARGE_DATA_SET.txt");

 int n,i,j,k,happies=0,blanks=0,start=0;
 string pancake;
int times=0;
   infile>>n;
   for(i=0; i<n; i++){
      infile>>pancake;
      infile>>k;
      start=0;
      times=0;
      cout<<pancake<<"  "<<k<<"     ";
      while(start<pancake.length()){
         start=find_index_of_blank(pancake);
            if(can_invert(pancake,start,k)){
                invert_string(pancake,start,k);
                cout<<"   "<<pancake;
                times++;
            }

            else
                break;
      }
      if(is_happy(pancake)){
      cout<<"    "<<times<<endl;
      outfile<<"Case #"<<i+1<<": "<<times<<endl;
      }
      else{
      cout<<"impossible"<<endl;
      outfile<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
      }



   }
 infile.close();
 outfile.close();
 return 0;
}
void invert_string(string &pancake, int start, int k){
  int i;

  for(i=start;i<start+k; i++){
     if(pancake[i]=='+')
        pancake[i]='-';
     else
        pancake[i]='+';
  }
}
bool is_happy(string pancake){
   for(int i=0;i<pancake.length();i++)
      if(pancake.at(i)=='-')
        return false;

 return true;
}
int find_index_of_blank(string pancake){
    for(int i=0; i<pancake.length();i++){
        if(pancake[i]=='-'){
            return i;
        }
    }
  return pancake.length()+ 1;
}
bool can_invert(string pancake,int start, int k){
  if(start+k<=pancake.length())
    return true;
  return false;
}
