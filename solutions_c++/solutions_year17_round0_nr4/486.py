
#include <iostream>
#include <memory>
#include <vector>
#include <sstream>
using namespace std;

void printStage( const vector<vector<char>>& aStage ) {
  cout << "\n\n";
  for( int i = 0; i < aStage.size(); ++i ) {
    for( int j = 0; j < aStage[i].size(); ++j ) {
      cout << aStage[i][j];
    }
    std::cout << "\n";
  }
  cout << "\n";
}

int getPoints( const vector<vector<char>>& aStage ) {
  int points = 0;
  for( int i = 0; i < aStage.size(); ++i ) {
    for( int j = 0; j < aStage[i].size(); ++j ) {
      if( aStage[i][j] != '.' ) points++;
      if( aStage[i][j] == 'o' ) points++;
    }
  }
  return points;
}

int getDif( const vector<vector<char>>& anOld, const vector<vector<char>>& aNew ) {
  int dif = 0;
  
  for( int i = 0; i < anOld.size(); ++i ) {
    for( int j = 0; j < anOld[i].size(); ++j ) {
      if( anOld[i][j] != aNew[i][j] ) dif++;
    }
  }
  return dif;
}

void main() {
  int T;
  cin >> T;
  for( int iT = 1; iT <= T; ++iT ) {
    int N, M;
    cin >> N >> M;
    //cout << "orig: " << N << " " << M << ", ";

    vector<vector<char>> stage( N, vector<char>( N, '.' ) );

    for( int iM = 0; iM < M; ++iM ) {
      char style;
      int R, C;
      cin >> style >> R >> C;
      stage[R-1][C-1] = style;
    }

    vector<vector<char>> orig = stage;
    /*
    vector<bool> usedR( N, false ), usedC( N, false ), usedDiagR( 2 * N, false ), usedDiagC( 2 * N, false );
    for( int i = 0; i < N; ++i ) {
      for( int j = 0; j < N; ++j ) {
        if( stage[i][j] != '.' ) {
          if( stage[i][j] != '+' ) {
            if( usedR[i] || usedC[j] ) {
              continue;
            }
            usedR[i] = true;
            usedC[j] = true;
          }
          else if( stage[i][j] != 'x' ) {
            if( usedDiagR[i + j] || usedDiagC[i - j + N] ) {
              continue;
            }
            usedDiagR[i + j] = true;
            usedDiagC[i - j + N] = true;
          }
        }
      }
    }
    */
    
    //printStage( stage );

    int pos_x = -1;
    int pos_o = -1;
    for( int iC = 0; iC < N; ++iC ) {
      if( stage[0][iC] == 'x' ) pos_x = iC;
      if( stage[0][iC] == 'o' ) pos_o = iC;
    }

    stringstream msgChange;
    int modelsChange = 0;
    if( pos_x != -1 ) {
      msgChange << "o 1 " << pos_x + 1 << endl;
      modelsChange++;
      stage[0][pos_x] = 'o';
      pos_o = pos_x;
    }
    if( pos_o == -1 ) {
      msgChange << "o 1 1" << endl;
      modelsChange++;
      stage[0][0] = 'o';
      
      for( int iC = 1; iC < N; ++iC ) {
        if( stage[0][iC] == '.' ) {
          msgChange << "+ 1 " << iC + 1 << endl;
          modelsChange++;
          stage[0][iC] = '+';
        }
      }
      for( int iC = 1; iC < N-1; ++iC ) {
        msgChange << "+ " << N << " " << iC + 1 << endl;
        modelsChange++;
        stage[N-1][iC] = '+';
      }
      for( int i = 1; i < N; ++i ) {
        msgChange << "x " << i + 1 << " " << i + 1 << endl;
        modelsChange++;
        stage[i][i] = 'x';
      }
    }
    else {
      for( int iC = 0; iC < N; ++iC ) {
        if( stage[0][iC] == '.' ) {
          msgChange << "+ 1 " << iC + 1 << endl;
          modelsChange++;
          stage[0][iC] = '+';
        }
      }
      for( int iC = 1; iC < N-1; ++iC ) {
        if( iC == pos_o - 1 ) continue;
        msgChange << "+ " << N << " " << iC + 1 << endl;
        modelsChange++;
        stage[N-1][iC] = '+';
      }
      
      for( int i = pos_o + 1; i < N; ++i ) {
        msgChange << "x " << i - pos_o + 1 << " " << i + 1 << endl;
        modelsChange++;
        stage[i - pos_o][i] = 'x';
      }
      for( int i = 0; i < pos_o - 1; ++i ) {
        msgChange << "x " << i + (N - pos_o) + 1 << " " << i + 1 << endl;
        modelsChange++;
        stage[i + (N - pos_o)][i] = 'x';
      }
      if( pos_o > 0 ) {
        if( pos_o > 1 ) {
          msgChange << "o " << N << " " << pos_o << endl;
          stage[N - 1][pos_o - 1] = 'o';
        }
        else {
          msgChange << "x " << N << " " << pos_o << endl;
          stage[N - 1][pos_o - 1] = 'x';
        }
        modelsChange++;
      }
    }
    
    //printStage( stage );

    cout << "Case #" << iT << ": " << getPoints( stage ) << " " << modelsChange << endl << msgChange.str();
    
    /*if( modelsChange != getDif( orig, stage ) ) {
      cout << "\ndif!!!\n";
      break;
    }
    if( N > 1 && getPoints( stage ) != N * 3 - 2 ) {
      cout << "\npoints!!!\n";
      break;
    }
    */
  }

}

