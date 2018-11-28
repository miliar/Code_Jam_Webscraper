
#include <iostream>
#include <memory>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

stringstream printMatrix( vector<vector<char>>& aMtr ) {
  stringstream msg;
  for( int iR = 0; iR < aMtr.size(); ++iR ) {
    for( int iC = 0; iC < aMtr[iR].size(); ++iC ) {
      msg << aMtr[iR][iC];
    }
    msg << endl;
  }

  return msg;
}

void main() {
  int T;
  cin >> T;
  for( int iT = 1; iT <= T; ++iT ) {
    cout << "Case #" << iT << ": ";
    stringstream msg;
    msg << endl;

    int R, C;
    cin >> R >> C;

    vector< vector< char > > data( R );
    for( int iR = 0; iR < R; ++iR ) {
      data[iR].resize( C );
      for( int iC = 0; iC < C; ++iC ) {
        cin >> data[iR][iC];
      }
    }

    int firstNonEmpty = -1;
    for( int iR = 0; iR < R; ++iR ) {
      char prevInLine = '?';
      for( int iC = 0; iC < C; ++iC ) {
        if( data[iR][iC] == '?' ) {
          data[iR][iC] = prevInLine;
        }
        else {
          if( prevInLine == '?' ) {
            for( int i = 0; i < iC; ++i ) data[iR][i] = data[iR][iC];
          }
          prevInLine = data[iR][iC];
        }
      }
      if( prevInLine == '?' ) {
        if( iR > 0 ) {
          for( int iC = 0; iC < C; ++iC ) data[iR][iC] = data[iR - 1][iC];
        }
      }
      else if( firstNonEmpty == -1 ) firstNonEmpty = iR;
    }


    for( int iR = 0; iR < firstNonEmpty; ++iR ) {
      for( int iC = 0; iC < C; ++iC ) {
        data[iR][iC] = data[firstNonEmpty][iC];
      }
    }
    
    msg << printMatrix( data ).str();


    cout << msg.str() << endl;
  }

}

