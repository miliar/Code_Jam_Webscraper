#include <iostream>
#include <vector>

using namespace std;

int main() {
  int T,R,C,minR,maxR,minC,maxC;
  char copy;
  bool can;
  cin>>T;
  for (int i=1;i<=T;i++) {
    cin>>R>>C;
    vector<vector<char>> matrix(R,vector<char>(C));
    vector<vector<bool>> used(R,vector<bool>(C));
    for (int j=0;j<R;j++) {
      for (int k=0;k<C;k++) {
        cin>>matrix[j][k];
        used[j][k]=false;
      }
    }
    for (int j=0;j<R;j++) {
      for (int k=0;k<C;k++) {
        if (matrix[j][k]=='?'||used[j][k]) continue;
        else {
          copy=matrix[j][k];
          used[j][k]=true;
          minC=maxC=k;
          while(minC>=1&&matrix[j][minC-1]=='?') minC--;
          while(maxC<C-1&&matrix[j][maxC+1]=='?') maxC++;
          minR=j;
          maxR=j;
          can=true;
          while(can&&minR>=1) {
            for (int m=minC;m<=maxC;m++) {
              if (matrix[minR-1][m]!='?') {can=false; break;}
            }
            if (can) minR--;
          }
          can=true;
          while(can&&maxR<R-1) {
            for (int m=minC;m<=maxC;m++) {
              if (matrix[maxR+1][m]!='?') {can=false; break;}
            }
            if (can) maxR++;
          }
          k=maxC;
          for (int m=minR;m<=maxR;m++) {
            for (int n=minC;n<=maxC;n++) {matrix[m][n]=copy; used[m][n]=true;}
          }
        }
      }
    }
    cout<<"Case #"<<i<<":"<<endl;
    for (int j=0;j<R;j++) {
      for (int k=0;k<C;k++) cout<<matrix[j][k];
      cout<<endl;
    }
    matrix.clear();
  }
  return 0;
}
