#include<iostream>

using namespace std;

void solveOneProblem(int casenum){
  string x;
  int w;
  cin >> x >> w;

  int len = x.length();
  int count = 0;
  for(int i = 0; i <= len - w; i++){
    if(x[i] == '-'){
      count++;
      for(int j = i; j < i+w; j++)
	x[j] = x[j] == '+' ? '-' : '+';
    }
  }

  bool solvable = true;
  for(int i = len - w; i < len; i++)
    if(x[i] == '-')
      solvable = false;

  if(solvable)
    cout << "Case #" << casenum << ": " << count << endl;
  else
    cout << "Case #" << casenum << ": IMPOSSIBLE" << endl;
}

int main(){
  int N;
  cin >> N;
  for(int i = 0; i < N; i++)
    solveOneProblem(i+1);
}
  
