#include<iostream>

using namespace std;

char cake[25*25];
int R, C;

char assignUp(int i, int j){
  if(i == R-1 || cake[i*C+j] != '?')
    return cake[i*C + j];
  if(cake[i*C+j] == '?')
    cake[i*C+j] = assignUp(i+1, j);
  return cake[i*C + j];
}

char assignDown(int i, int j){
  if(i == 0 || cake[i*C+j] != '?')
    return cake[i*C + j];
  if(cake[i*C+j] == '?')
    cake[i*C+j] = assignDown(i-1, j);
  return cake[i*C + j];
}

char assignRight(int i, int j){
  if(j == 0 || cake[i*C+j] != '?')
    return cake[i*C + j];
  if(cake[i*C+j] == '?')
    cake[i*C+j] = assignRight(i, j-1);
  return cake[i*C + j];
}

char assignLeft(int i, int j){
  if(j == C-1 || cake[i*C+j] != '?')
    return cake[i*C + j];
  if(cake[i*C+j] == '?')
    cake[i*C+j] = assignLeft(i, j+1);
  return cake[i*C + j];
}

void solveOneProblem(int c){
  cout << "Case #" << c << ":" << endl;

  cin >> R >> C;
  char xc;
  
  for(int i = 0; i < R; i++)
    for(int j = 0; j < C; j++){
      cin >> xc;
      cake[i*C+j] = xc;
    }
  
  for(int i = 0; i < R; i++)
    for(int j = 0; j < C; j++)
      assignUp(i, j);

  for(int i = 0; i < R; i++)
    for(int j = 0; j < C; j++)
      assignDown(i, j);

  for(int i = 0; i < R; i++)
    for(int j = 0; j < C; j++)
      assignLeft(i, j);

  for(int i = 0; i < R; i++)
    for(int j = 0; j < C; j++)
      assignRight(i, j);

  for(int i = 0; i < R; i++){
    for(int j = 0; j < C; j++){
      cout << cake[i*C+j];
    }
    cout << endl;
  }
}

int main(){

  int T;
  cin >> T;
  for(int i = 0; i < T; i++)
    solveOneProblem(i+1);
}

