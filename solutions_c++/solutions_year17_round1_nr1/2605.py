#include<iostream>
#include<map>
#include<ctype.h>
using namespace std;
char A[26][26];
int R, C;
struct tw{int x,y;};
map<char,int> count;
map<char,tw> rect;

int explore(int r, int c){
  if(count[A[r][c]] > 1){
    int downrow = r, rightcol = c, uprow = r, leftcol = c;
    for(int j = c + 1; j < C; j++)
      if(A[r][j] == A[r][c]) rightcol = j;
    for(int i = r + 1; i < R; i++)
      for(int j = 0; j < C; j++)
	if(A[i][j] == A[r][c]){
	  if(j > rightcol) rightcol = j;
	  if(j < leftcol)  leftcol = j;
	  if(i > downrow)  downrow = i;
	}

    for(int i = uprow; i <= downrow; i++)
      for(int j = leftcol; j <= rightcol; j++)
	A[i][j] = A[r][c];
    rect[A[r][c]].x = rightcol - leftcol;
    rect[A[r][c]].y = downrow - uprow;
  }
  count[A[r][c]] = 0;
  return 0;
}

void expand(int r, int c){
  //cout << A[r][c] << "\t" << rect[A[r][c]].x << rect[A[r][c]].y << endl;
  if(rect[A[r][c]].x == -1) return;
  int i,j;
  bool replace = true;
  
  for(j = c - 1; j >= 0; j--){
    for(i = r; i <= r + rect[A[r][c]].x; i++)
      if(A[i][j] != '?'){
	replace = false;
	break;
      }
    if(replace == true){
      for(i = r; i <= r + rect[A[r][c]].x; i++)
	if(A[i][j] == '?') A[i][j] = A[r][c];
      rect[A[r][c]].y++;
      c = j;
    }
    else{
      c = j + 1;
      replace = true;
      break;
    }
  }
  for(j = c + rect[A[r][c]].y + 1; j < C; j++){
    for(i = r; i <= r + rect[A[r][c]].x; i++)
      if(A[i][j] != '?'){
	replace = false;
	break;
      }
    if(replace == true){
      for(i = r; i <= r + rect[A[r][c]].x; i++)
	if(A[i][j] == '?') A[i][j] = A[r][c];
      rect[A[r][c]].y++;
    }
    else{
      replace = true;
      break;
    }
  }

  for(i = r - 1; i >= 0; i--){
    for(j = c; j <= c + rect[A[r][c]].y; j++)
      if(A[i][j] != '?'){
	replace = false;
	break;
      }
    if(replace == true){
      for(j = c; j <= c + rect[A[r][c]].y; j++)
	if(A[i][j] == '?') A[i][j] = A[r][c];
      rect[A[r][c]].x++;
      r = i;
    }
    else{
      r = i + 1;
      replace = true;
      break;
    }
  }

  for(i = r + rect[A[r][c]].x + 1; i < R; i++){
    for(j = c; j <= c + rect[A[r][c]].y; j++)
      if(A[i][j] != '?'){
	replace = false;
	break;
      }
    if(replace == true){
      for(j = c; j <= c + rect[A[r][c]].y; j++)
	if(A[i][j] == '?') A[i][j] = A[r][c];
      rect[A[r][c]].x++;
    }
    else{
      replace = true;
      break;
    }
  }
  rect[A[r][c]].x = -1;
  rect[A[r][c]].y = -1;
}

void solve(){
  cin >> R >> C;
  for(int i = 0; i < R; i++)
    for(int j = 0; j < C; j++){
      cin >> A[i][j];
      count[A[i][j]]++;
    }	
  for(int i = 0; i < R; i++)
    for(int j = 0; j < C; j++)
      if(A[i][j] != '?') explore(i, j);

  for(int i = 0; i < R; i++)
    for(int j = 0; j < C; j++)
      if(A[i][j] != '?') expand(i, j);
  
  for(int i = 0; i < R; i++){
    for(int j = 0; j < C; j++)
      cout << A[i][j];
    cout << endl;
  }
}

int main(){
  int T;
  cin >> T;

  for(int i = 1; i <= T; i++){
    for(char x = 'A'; x <= 'Z'; x++) rect[x].x = rect[x].y = 0;
    for(char x = 'A'; x <= 'Z'; x++) count[x] = 0;
    cout << "Case #" << i << ": " << endl;
    solve();
  }
  return 0;
}
