#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
int main(){
  ifstream is("A.in");
  ofstream os("A.out");

  int T; is >> T;
  for(int l = 0; l < T; ++l){
    int R,C;
    is >> R >> C;
    char matrix[R][C];
    for(int j=0;j<R;j++){
      for(int k=0;k<C;k++){
	is >> matrix[j][k];
      }
    }
    char actual = '?';
    int pos = -1;
    for(int i=0;i<R;i++){
      actual = '?';
      for(int j=0;j<C;j++){
	if(matrix[i][j]!='?' and matrix[i][j]!=actual){
	  actual = matrix[i][j];
      	  pos=j;
	  int itr1=pos-1,itr2=pos+1;
	  while(itr1>-1 and matrix[i][itr1]=='?'){matrix[i][itr1]=actual;itr1--;}
	  while(itr2<C and matrix[i][itr2]=='?'){matrix[i][itr2]=actual;itr2++;}	  
	}
      }
    }
    for(int j=0;j<C;j++){
      actual='?';
      for(int i=0;i<R;i++){
	if(matrix[i][j]!='?' and matrix[i][j]!=actual){
	  actual = matrix[i][j];
	  pos=i;
	  int itr1=pos-1,itr2=pos+1;
	  while(itr1>-1 and matrix[itr1][j]=='?'){matrix[itr1][j]=actual;itr1--;}
	  while(itr2<R and matrix[itr2][j]=='?'){matrix[itr2][j]=actual;itr2++;}
	}
      }
    }
    os << "Case #"<< l+1 << ":\n";
    for(int i=0;i<R;i++){
      for(int j=0;j<C;j++){
	os << matrix[i][j];
      }
      os << '\n';
    }
  }
  is.close();
  os.close();
  return 0;
}
