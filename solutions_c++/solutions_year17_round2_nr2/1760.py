#include<iostream>

using namespace std;

const int C = 6;
const int MAX_N = 1000;

int colors[C];
char signs[] = {'R','O','Y','G','B','V'};

bool maj[MAX_N]; //majority color
char res[MAX_N];



int main(){
  int c;
  cin >> c;
  for(int cur =1; cur <= c; cur++){
    cin.ignore();
    int N;
    cin >> N;
    for(int i = 0; i < C; i++)
      cin >> colors[i];

    for(int i = 0; i < N; i++)
      res[i] = ' ';
    
    int max_i = -1;
    int max_sum = 0;
    
    bool possible = true;
    for(int i = 0; i < C; i+=2){
      int sum = 0;
      for(int j = -1; j <= 1; j++)
	sum += colors[(i+j+C)%C];
      if(sum > (N/2))
	possible = false;
      if(sum > max_sum){
	max_sum = sum;
	max_i = i;
      }
    }

    //We now have the maximum color
    cout << "Case #" << cur << ": ";

    if(!possible)
      cout << "IMPOSSIBLE";
    else{
      //if a colouring is possible

      int k = 0;
      
      while(max_sum > 0){
	res[k] = signs[max_i];
	k += 2;
	max_sum--;
      }

      colors[max_i] = 0;
	
      k = 0;

      while(k < N && res[k] != ' ')
	k++;

      while(k < N){
	//empty cell in k

	int best_i = max_i;
	if(colors[(max_i+2)%C] > colors[(max_i+4)%C])
	  best_i = (max_i+2)%C;
	else
	  best_i = (max_i+4)%C;

	if(res[k-1] == signs[best_i]){
	  res[k] = signs[(2*max_i+6-best_i)%C];
	  colors[(2*max_i+6-best_i)%C]--;
	}else{
	  res[k] = signs[best_i];
	  colors[best_i]--;
	}
	
	while(k < N && res[k] != ' ')
	  k++;
      }



      for(int i = 0; i < N; i++)
	cout << res[i];
    }

    cout << endl;
  }

}
