#include <iostream>
#include <vector>
#include <list>
using namespace std;

int ford_fulkerson(int C[400][400], int f[400][400], int N, int s, int t, int max){
	int value = 0, parent[N], curr, visited[N], child, minv[N], par;
	list<int> Q;
	bool path;

	while(true){
		path = false;
		for (int i = 0; i < N; i++){
			visited[i] = 0;
			minv[i] = 0;
		}
		Q.clear();
		Q.push_back(s);
		minv[s] = max;
    visited[s] = 1;

		while(Q.size() > 0){
			curr = Q.front();
			Q.pop_front();
			if (curr == t){
				path = true;
				break;
			}
			for (int i = 0; i < N; i++){
				if (C[curr][i] > 0 && visited[i] == 0){
					minv[i] = min(minv[curr], C[curr][i]);
					Q.push_back(i);
					parent[i] = curr;
          visited[i] = 1;
				}
			}
		}

		if (path){
			value += minv[t];
			curr = t;
			while (curr != s){
				par = parent[curr];
				f[par][curr] += minv[t];
        C[par][curr] -= minv[t];
				C[curr][par] += minv[t];

        curr = par;
			}
		} else {
			break;
		}
	}
	return value;
}

void solve_case(int T){
  int N, M;
  cin >> N >> M;
  int row[N], col[N], r, c, X[N][N], P[N][N], A[400][400], f[400][400], output[N][N], value, initial = 0, ptotal = 0;
  char type;

  for (int i = 0; i < N; i++){
    row[i] = 0;
    col[i] = 0;
  }

  for (int i = 0; i < N; i++){
    for (int j = 0; j < N; j++){
      X[i][j] = 0;
      P[i][j] = 0;
      output[i][j] = 0;
    }
  }

  for (int i = 0; i < 4*N; i++){
    for (int j = 0; j < 4*N; j++){
      A[i][j] = 0;
      f[i][j] = 0;
    }
  }

  for (int i = 0; i < N; i++){
    for (int j = 0; j < N; j++){
      A[2+i+j][2*N+1 + i-j+N-1] = 1;
    }
  }

  for (int i = 0; i < 2*N-1; i++){
    A[0][2+i] = 1;
    A[2*N+1 + i][1] = 1;
  }

  for (int i = 0; i < M; i++){
  	cin >> type >> r >> c;
  	if (type == 'x' || type == 'o'){
  		row[r-1] = 1;
  		col[c-1] = 1;
  		X[r-1][c-1] = 1;
      initial++;
      ptotal++;
  	}
  	if (type == '+' || type == 'o') {
  		A[0][2 + r+c-2] = 0;
  		A[2*N+1 + r-c+N-1][1] = 0;
  		P[r-1][c-1] = 1;
      initial++;
  	}
  }

  value = ford_fulkerson(A, f, 4*N, 0, 1, 1);

  for (int i = 0; i < N; i++){
    for (int j = 0; j < N; j++){
      if (f[2+i+j][2*N+1 + i-j+N-1] - f[2*N+1 + i-j+N-1][2+i+j] == 1){
        if (X[i][j] == 1){
          output[i][j] = 3;
        } else {
          output[i][j] = 1;
        }
      }
    }
  }

  int fin = 0;
  int count = 0;
  for (int i = 0; i < N; i++){
    if (row[i] == 0){
      while (col[fin] == 1 && fin < N){
        fin++;
      }
      if (P[i][fin] == 1){
        output[i][fin] = 3;
      } else if (output[i][fin] == 1){
        output[i][fin] = 3;
        count++; 
      } else {
        output[i][fin] = 2;
      }
      fin++;
    }
  }

  cout << "Case #" << T << ": " << initial + value + N - ptotal << " " << value + N - ptotal - count << endl;

  for (int i = 0; i < N; i++){
    for (int j = 0; j < N; j++){
      if (output[i][j] == 1){
        cout << "+ " << i+1 << " " << j+1 << endl;
      } else if (output[i][j] == 2){
        cout << "x " << i+1 << " " << j+1 << endl;
      } else if (output[i][j] == 3){
        cout << "o " << i+1 << " " << j+1 << endl;
      }
    }
  }
}

int main() {
  	int t;
  	cin >> t; 
  	for (int i = 1; i <= t; i++) {
  	  	solve_case(i);
  	}
  	return 0;
}