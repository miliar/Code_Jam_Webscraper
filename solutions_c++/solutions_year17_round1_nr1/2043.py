#include <bits/stdc++.h>
using namespace std;
bool a[28];
char s[28][28];
bool visit[28][28];
int R,C;
bool ok(int x,int y) {
  return x>=0 && x<R && y>=0 && y<C;
}
void solve(int x,int y,int p) {
  char ch = (char)(p+65);
  while(ok(x,y) && s[x][y] == '?') {
     s[x][y] = ch;
     y++;
  }
}
void fille(int x,int y,int p) {
  char ch = (char)(p+65);
  int a = x;
  int b = y+1;
  while(ok(a,b) && s[a][b] == '?') {
     s[a][b] = ch;
     visit[a][b] = true;
     b++;
  }
  a = x;
  b = y-1;
  while(ok(a,b) && s[a][b] == '?') {
     s[a][b] = ch;
     visit[a][b] = true;
     b--;
  }
}
void filly(int x,int y,int p) {
  char ch = (char)(p+65);
  int a = x+1;
  int b = y;
  while(ok(a,b) && s[a][b] == '?') {
     s[a][b] = ch;
     visit[a][b] = true;
     a++;
  }
  a = x-1;
  b = y;
  while(ok(a,b) && s[a][b] == '?') {
     s[a][b] = ch;
     visit[a][b] = true;
     a--;
  }
}
int main() {
  int t;
  freopen("A-large (1).in","r",stdin);
  freopen("ans.txt","w",stdout);
  int d = 1;
  cin >> t;
  while(t--) {
     cout << "Case #" << d++ << ": " << endl;
     cin >> R >> C;
     for(int i=0;i<R;i++) {
          for(int j=0;j<C;j++) {
             cin >> s[i][j];
          }
     }
     memset(visit,false,sizeof visit);
     //memset(a,false,sizeof a);
     int x,y;
     for(int i=0;i<R;i++) {
          for(int j=0;j<C;j++) {
               if(s[i][j] != '?' && visit[i][j] == false) {
                  //cout << i << " " << j << endl;
                  visit[i][j] = true;
                  fille(i,j,s[i][j]-'A');
                  //a[s[i][j]-'A'] = true;
               }
          }
     }
     memset(visit,false,sizeof visit);
     for(int i=0;i<R;i++) {
          for(int j=0;j<C;j++) {
               if(s[i][j] != '?' && visit[i][j] == false) {
                  //cout << i << " " << j << endl;
                  visit[i][j] = true;
                  filly(i,j,s[i][j]-'A');
                  //a[s[i][j]-'A'] = true;
               }
          }
     }
     //for(int p=0;p<26;p++){
       //  bool flag = false;
         //for(int i=0;i<R;i++) {
          //for(int j=0;j<C;j++) {
            //  if(s[i][j] == '?') {
              //   flag = true;
               //  x = i;
                // y = j;
                 //break;
              //}
          //}
          //if(flag) break;
        //}
        //if(a[p] == false) {
          //a[p] = true;
          //solve(x,y,p);
        //}
     //}
     for(int i=0;i<R;i++) {
     for(int j=0;j<C;j++) {
         cout << s[i][j];
      }
      cout << endl;
     }
  }
  return 0;
}
