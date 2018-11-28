#include <iostream>
#include <cstdio>
using namespace std;

string s[25];
bool ar[26];

int main() {
  int T; scanf("%d",&T);
  int R,C;
  for(int Case=1; Case<=T; ++Case) {
    scanf("%d%d",&R,&C);
    memset(ar,false,sizeof(ar));
    for(int i=0; i<R; ++i) cin >> s[i];
    for(int i=0; i<R; ++i) {
      for(int j=0; j<C; ++j) {
        if(s[i][j]!='?' && ar[s[i][j]-'A']==false) {
          ar[s[i][j]-'A']=true;
          if( (i+1<R && s[i+1][j]=='?') || (i-1>=0 && s[i-1][j]=='?')) {
            int LL,RR,I,J;
            I=i; while(I+1<R && s[I+1][j]=='?') s[++I][j]=s[i][j]; RR=I;
            I=i; while(I-1>=0 && s[I-1][j]=='?') s[--I][j]=s[i][j]; LL=I;
            // 整排往左右
            J=j; bool allLine = true;
            while(J+1<C && s[i][J+1]=='?' && allLine) {
              ++J;
              for(int k=LL; k<=RR; ++k) 
                if(s[k][J]!='?') { allLine = false; break; }
              if(allLine)
                for(int k=LL; k<=RR; ++k) s[k][J]=s[i][j];
            }
            J=j, allLine = true;
            while(J-1>=0 && s[i][J-1]=='?' && allLine) {
              --J;
              for(int k=LL; k<=RR; ++k) 
                if(s[k][J]!='?') { allLine = false; break; }
              if(allLine)
                for(int k=LL; k<=RR; ++k) s[k][J]=s[i][j];
            }
          }
          else if((j+1<C && s[i][j+1]=='?') || (j-1>=0 && s[i][j-1]=='?')) {
            int J;
            J=j; while(J+1<C && s[i][J+1]=='?') s[i][++J]=s[i][j];
            J=j; while(J-1>=0 && s[i][J-1]=='?') s[i][--J]=s[i][j];
          }
        }
      }
    }
    printf("Case #%d:\n",Case);
    for(int i=0; i<R; ++i) cout << s[i] << endl;
  }
  return 0;
}
