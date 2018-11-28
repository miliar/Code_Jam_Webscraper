#include <iostream>
#include <string>

using namespace std;

main() {
  int T;
  cin >> T;
  for (int c=1; c<=T; c++) {
    int N, M, row, col;
    cin >> N >> M;
    char A[N+1][N+1], B[N+1][N+1];
    for (int i=1; i<=N; i++)
      for (int j=1; j<=N; j++)
	A[i][j] = B[i][j] = '.';

    for (int i=0; i<M; i++) {
      char ch;
      cin >> ch >> row >> col;
      A[row][col] = ch;
      if (row>1) cout << "WARNING: Row " << row << " > 1" << endl;
    }

    // Find solution
    
    if (N==1) {
      B[1][1] = 'o';
    } else { // N >= 2
      int dot_col = -1, cross_col = -1;
      for (int j=1; j<=N; j++)
	if (A[1][j] == 'o') dot_col = j;
	else if (A[1][j] == 'x') cross_col = j;
      
      if (dot_col<0) dot_col = cross_col >= 0 ? cross_col : 1;
      
      if (N==2) {
	B[1][1] = B[1][2] = '+';
	B[1][dot_col] = 'o';
	B[2][3 - dot_col] = 'x';
      } else if (N==3 && dot_col==2) {
	B[1][1] = B[1][3] = B[3][2] = '+';
	B[2][1] = B[3][3] = 'x';
	B[1][2] = 'o';
      } else { // n >= 3
	int dot2_col = dot_col != 2 ? 2 : 3;
	
	for (int j=1; j<=N; j++) B[1][j] = '+';
	for (int j=2; j<N;  j++) B[N][j] = '+';
	B[1][dot_col] = B[N][dot2_col] = 'o';
	
	for (int i=2, j=1; i<N; i++, j++) {
	  while (j == dot_col || j == dot2_col) j++;
	  B[i][j] = 'x';
	}
      }
    };
    
    // Output answer
    
    int score=0, changes=0;
    
    for (int i=1; i<=N; i++)
      for (int j=1; j<=N; j++) {
	if (A[i][j] != B[i][j]) changes ++;
	if (B[i][j] == 'o') score += 2;
	if (B[i][j] == '+') score++;
	if (B[i][j] == 'x') score++;
      }
    
    cout << "Case #" << c << ": " << score << " " << changes << endl;
    // Print board

    if (N>=2 && score != 3*N-2) cout << "ERROR UNEXPECTED SCORE!" << endl;
    /*
    cout << "N=" << N << endl;
    for (int i=1; i<=N; i++) {
      for (int j=1; j<=N; j++) cout << A[i][j];
      cout << " ";
      for (int j=1; j<=N; j++) cout << B[i][j];
      cout << endl;
    };
    */

    // Check rows
    for (int i=1; i<=N; i++) {
      int o_count = 0, x_count = 0;
      for (int j=1; j<=N; j++) {
	if (B[i][j]=='o') o_count ++;
	if (B[i][j]=='x') x_count ++;
      }
      if (o_count + x_count > 1) cout << "OX ERROR (ROW)" << endl;
    }
    // Check columns
    for (int j=1; j<=N; j++) {
      int o_count = 0, x_count = 0;
      for (int i=1; i<=N; i++) {
	if (B[i][j]=='o') o_count ++;
	if (B[i][j]=='x') x_count ++;
      }
      if (o_count + x_count > 1) cout << "OX ERROR (COLUMN)" << endl;
    }

    for (int i=1; i<=N; i++)
      for (int j=1; j<=N; j++)
	if (A[i][j] != B[i][j])
	  cout << B[i][j] << " " << i << " " << j << endl;
  };
};
