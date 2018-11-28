#include<algorithm>
#include<iostream>
#include<cmath>
#include<string>
#include<assert.h>
#include<vector>
#include<map>
#include<set>
#include<ctime>

#define F0(i,n) for(i=0; i < n; i++)
#define F1(i,n) for(i=1; i < n; i++)
#define Fxy(i,x,y) for(i=x; i < y; i++)

#define LL long long
#define ULL unsigned long long

using namespace std;

int main()
{
  time_t start;
  time(&start);
  int a,b,c,i,j,k,m,x,y,K,N,M,numCases;
  cin >> numCases;

  F1(c, numCases+1){
    cout << "Case #" << c << ": ";

    cin >> N >> M;

    int p_wt[N][N];
    int x_wt[N][N];
    int o_wt[N][N];
    bool p_ok[N][N];
    bool x_ok[N][N];
    bool o_ok[N][N];
    char stage[N][N];

    char addChars[N*N];
    int addXs[N*N];
    int addYs[N*N];
    int addedModels = 0;

    F0(i,N){
      F0(j,N){
	p_wt[i][j] = 3-2*N-4*min(min(i,j),min(N-j-1,N-i-1)); // C++11 requires an extra flag at compile time, which admittedly would've taken less time than typing this comment, but whatever
	x_wt[i][j] = 5-4*N; 
	o_wt[i][j] = p_wt[i][j] + x_wt[i][j];
	p_ok[i][j] = true;
	x_ok[i][j] = true;
	o_ok[i][j] = true;
	stage[i][j] = '.';
      }
    }

    char C;

    F0(m,M){
      // read in each input 
      cin >> C >> x >> y;
      x--;y--;
      stage[x][y] = C;

      if(C == 'x' || C == 'o'){
	p_ok[x][y] = false;
	F0(i,N){
	  // no xs or os along rows
	  x_ok[i][y] = false;
	  x_ok[x][i] = false;
	  if (C == 'o' || i != x) o_ok[i][y] = false;
	  if (C == 'o' || i != y) o_ok[x][i] = false;
	}
      }
      if(C == '+' || C == 'o'){
	x_ok[x][y] = false;
	i = x - min(x,y);
	j = y - min(x,y);
	while(i < N && j < N){
	  p_ok[i][j] = false;
	  if (C == 'o' || i != x) o_ok[i][j] = false;
	  i++; j++;
	}
	i = x - min(x,N-y-1);
	j = y + min(x,N-y-1);
	while(i < N && j >= 0){
	  p_ok[i][j] = false;
	  if (C == 'o' || i != x) o_ok[i][j] = false;
	  i++; j--;
	}
      }

      // recalculate every weight
      F0(i,N){
	F0(j,N){
	  x_wt[i][j] = 1;
	  F0(k,N){
	    if (k != j && x_ok[i][k]) x_wt[i][j]--; 
	    if (k != i && x_ok[k][j]) x_wt[i][j]--; 
	  }
	  p_wt[i][j] = 1;
	  x = i - min(i,j);
	  y = j - min(i,j);
	  while(x < N && y < N){
	    if (x != i && p_ok[x][y]) p_wt[i][j]--;
	    x++; y++;
	  }
	  x = i - min(i,N-j-1);
	  y = j + min(i,N-j-1);
	  while(x < N && y >= 0){
	    if (x != i && p_ok[x][y]) p_wt[i][j]--;
	    x++; y--;
	  }
	  o_wt[i][j] = x_wt[i][j] + p_wt[i][j];
	}
      } 
    }

    //**************************************************
    //**************************************************

    int max_wt;
    while(true){
      max_wt = -1 << 30;
      C = '.';

      F0(i,N){
	F0(j,N){
	  if(x_ok[i][j] && x_wt[i][j] > max_wt){
	    max_wt = x_wt[i][j];
	    C = 'x'; x = i; y = j;
	  }
	  if(p_ok[i][j] && p_wt[i][j] > max_wt){
	    max_wt = p_wt[i][j];
	    C = '+'; x = i; y = j;
	  }
	  if(o_ok[i][j] && o_wt[i][j] > max_wt){
	    max_wt = o_wt[i][j];
	    C = 'o'; x = i; y = j;
	  }
	}
      }

      if(C == '.') break;
      bool replace = false;
      if(C == 'o' && stage[x][y] != '.') replace = true;
      stage[x][y] = C;

      if(C == 'x' || C == 'o'){
	p_ok[x][y] = false;
	F0(i,N){
	  // no xs or os along rows
	  x_ok[i][y] = false;
	  x_ok[x][i] = false;
	  if (C == 'o' || i != x) o_ok[i][y] = false;
	  if (C == 'o' || i != y) o_ok[x][i] = false;
	}
      }
      if(C == '+' || C == 'o'){
	x_ok[x][y] = false;
	i = x - min(x,y);
	j = y - min(x,y);
	while(i < N && j < N){
	  p_ok[i][j] = false;
	  if (C == 'o' || i != x) o_ok[i][j] = false;
	  i++; j++;
	}
	i = x - min(x,N-y-1);
	j = y + min(x,N-y-1);
	while(i < N && j >= 0){
	  p_ok[i][j] = false;
	  if(C == 'o' || i != x) o_ok[i][j] = false;
	  i++; j--;
	}
      }

      // recalculate every weight
      F0(i,N){
	F0(j,N){
	  x_wt[i][j] = (stage[i][j] == '.') ? 1 : (stage[i][j] == 'o') ? -1 : 0;
	  F0(k,N){
	    if (k != j && x_ok[i][k]) x_wt[i][j]--; 
	    if (k != i && x_ok[k][j]) x_wt[i][j]--; 
	  }
	  p_wt[i][j] = (stage[i][j] == '.') ? 1 : (stage[i][j] == 'o') ? -1 : 0;
	  a = i - min(i,j);
	  b = j - min(i,j);
	  while(a < N && b < N){
	    if (a != i && p_ok[a][b]) p_wt[i][j]--;
	    a++; b++;
	  }
	  a = i - min(i,N-j-1);
	  b = j + min(i,N-j-1);
	  while(a < N && b >= 0){
	    if (a != i && p_ok[a][b]) p_wt[i][j]--;
	    a++; b--;
	  }
	  o_wt[i][j] = x_wt[i][j] + p_wt[i][j];
	}
      } 
      // add to list of adds
      bool addedO = false;
      if(replace){
	F0(k,addedModels){
	  if(addXs[k] == x + 1 && addYs[k] == y + 1){
	    addChars[k] = 'o';
	    addedO = true;
	    break;
	  }
	}
	if (!addedO){
	  addChars[addedModels] = C;
	  addXs[addedModels] = x + 1;
	  addYs[addedModels] = y + 1;
	  addedModels++;
	}
      } else {
	addChars[addedModels] = C;
	addXs[addedModels] = x + 1;
	addYs[addedModels] = y + 1;
	addedModels++;
      }

      //cerr << "This step was " << C << " at ("<< x+1 << ","<<y+1<<")\n";
      //cerr << "After this step x_ok:\n\n";
      F0(i,N){
	//	F0(j,N) //cerr << x_ok[i][j];
	//cerr << "\n";
      }
      //cerr << "After this step p_ok:\n\n";
      F0(i,N){
	//	F0(j,N) //cerr << p_ok[i][j];
	//cerr << "\n";
      }
      //cerr << "After this step o_ok:\n\n";
      F0(i,N){
	//	F0(j,N) //cerr << o_ok[i][j];
	//cerr << "\n";
      }
    }


    //**************************************************
    //**************************************************

    int points = 0;

    // calculate points
    cerr << "done with case #" << c << ":\n";
    F0(i,N){
      F0(j,N){
	//cerr << stage[i][j];
	if(stage[i][j] == 'o'){
	  points += 2;
	} else if (stage[i][j] == 'x' || stage[i][j] == '+'){
	  points++;
	}
      }
      //cerr << "\n";
    }

    cout << points << " " << addedModels << "\n";
    F0(k,addedModels){
      cout << addChars[k] << " " << addXs[k] << " " << addYs[k] << "\n";
    }
  }
  time_t finish;
  time(&finish);
  cerr << "took " << difftime(finish,start) << " seconds\n";
}
