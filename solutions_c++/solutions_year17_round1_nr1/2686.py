#include<iostream>
#include<vector>
using namespace std;

const int MAX = 25;
int R,C;
char A[MAX][MAX];

bool check(){
  for(int i = 0; i < R; i++){
    for(int j = 0; j < C; j++){
      //cerr << A[i][j];
    }
    //cerr << endl;
  }
  for(int i = 0; i < R; i++){
    for(int j = 0; j < C; j++){
      if(A[i][j] == '?')
	return false;
    }
  }
  for(int i = 0; i < R; i++){
    for(int j = 0; j < C; j++){
      cout << A[i][j];
    }
    cout << endl;
  }
  return true;
}

bool find(int p, vector<char> & V){
  if(p == (int)V.size()){
    return check();
  }
  for(int r1 = 0; r1 < R; r1++){
    for(int r2 = r1; r2 < R; r2++){
      for(int c1 = 0; c1 < C; c1++){
	for(int c2 = c1; c2 < C; c2++){
	  //cerr << r1 << " " << r2 << " " << c1 << " " << c2 << endl;
	  int pr=-1, pc=-1;
	  bool B = true;
	  for(int r = r1; r <= r2; r++){
	    for(int c = c1; c <= c2; c++){
	      if(A[r][c] == V[p]){
		pr = r; pc = c;
	      }
	      else if(A[r][c] == '?'){
		A[r][c] = V[p];
	      }
	      else{
		B = false;
	      }
	    }
	  }
	  if(pr != -1 and pc != -1 and B){
	    if(find(p+1, V))
	      return true;
	  }
	  for(int r = r1; r <= r2; r++){
	    for(int c = c1; c <= c2; c++){
	      if(r == pr and c == pc) continue;
	      if(A[r][c] != V[p]) continue;
	      A[r][c] = '?';
	    }
	  }
	  
	}
      }
    }
  }
  return false;
}

int main(){
  int T;
  cin >> T;
  for(int c = 1; c <= T; c++){
    cout << "Case #" << c << ":" << endl;
    vector<char> V;
 
    cin >> R >> C;
    for(int i = 0; i < R; i++){
      for(int j = 0; j < C; j++){
	cin >> A[i][j];
	if(A[i][j] != '?'){
	  //cerr << A[i][j] << endl;
	  V.push_back(A[i][j]);
	}
      }
    }
    find(0,V);

  }
  return 0;
}
