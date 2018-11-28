#include <iostream>
#include <fstream>

using namespace std;
int max_block_of_stalls(int stall_blocks[], int);
int main(){
 ifstream infile;
 ofstream outfile;

 infile.open("SMALL_DATA_SET.txt");
 outfile.open("SOLUTION_SMALL_DATA_SET.txt");
 int n,stalls,people, i,j,k=0,index;

 infile>>n;
 for(int a=0; a<n; a++){
 int stall_blocks[2000]={0};
  infile>>stalls>>people;
 //stalls=1000;
 //people =127;
 k=0;//keeps track of stall_blocks for each test
 //stall_blocks[k]=stalls;
 cout<<stalls<<"      "<<people<<endl;
  for(i=1; i<=people; i++){
     if(i==people){
          if(stalls%2==0){
              cout<<stalls/2<<"      "<<stalls/2-1<<endl;
              outfile<<"Case #"<<a+1<<": "<<stalls/2<<" "<<stalls/2-1<<endl;
          }
          else{
            cout<<stalls/2<<"       "<<stalls/2<<endl;
            outfile<<"Case #"<<a+1<<": "<<stalls/2<<" "<<stalls/2<<endl;
          }
     }
     if(stalls%2!=0){
        stall_blocks[++k]=stalls/2;
        stall_blocks[++k]=stalls/2;
     }
     if(stalls%2==0){
        stall_blocks[++k]=stalls/2-1;
        stall_blocks[++k]=stalls/2;
     }
     stalls=max_block_of_stalls(stall_blocks,k);

  }
 }
 infile.close();
 outfile.close();
 return 0;

}

int max_block_of_stalls(int stall_blocks[], int k){
     int i=0, max_found,index_of_max=0;

     max_found=stall_blocks[0];
     for(i=0; i<k+1; i++){
         if(stall_blocks[i] > max_found){
             index_of_max=i;
             max_found=stall_blocks[index_of_max];
         }
     }
       stall_blocks[index_of_max]=0;
       return max_found;
}
