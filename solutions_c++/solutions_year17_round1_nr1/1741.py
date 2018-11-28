#include <bits/stdc++.h>
using namespace std;



int main () {

  freopen ( "A-large.in" , "r" , stdin );
  freopen ( "out.txt" , "w" , stdout );

  int t , r , c;
  int lft , rgt;
  char mat[30][30];
  bool used[30];
  bool flag;

  scanf ( "%d" , &t );

  for ( int y = 0 ; y < t ; y++ ) {

    scanf ( "%d%d" , &r , &c );
    for ( int i = 0 ; i < r ; i++ )
      scanf ( "%s" , mat[i] );

    memset ( used , 0 , sizeof used );

    for ( int i = 0 ; i < r ; i++ ) {
      for ( int h = 0 ; h < c ; h++ ) {

        if ( mat[i][h] == '?' or used[mat[i][h] - 'A'] )
          continue;

        lft = h , rgt = h;
        while ( lft and mat[i][lft-1] == '?' )
          lft--;
        while ( rgt < c - 1 and mat[i][rgt+1] == '?' )
          rgt++;

        for ( int j = i ; j >= 0 ; j-- ) {
          flag = true;
          for ( int it = lft ; it <= rgt ; it++ )
            if ( mat[j][it] != '?' and mat[j][it] != mat[i][h] )
              flag = false;
          if ( !flag )
            break;
          for ( int it = lft ; it <= rgt ; it++ )
            mat[j][it] = mat[i][h];
        }

        for ( int j = i + 1 ; j < r ; j++ ) {
          flag = true;
          for ( int it = lft ; it <= rgt ; it++ )
            if ( mat[j][it] != '?' )
              flag = false;
          if ( !flag )
            break;
          for ( int it = lft ; it <= rgt ; it++ )
            mat[j][it] = mat[i][h];
        }

        used[mat[i][h] - 'A'] = true;

      }
    }

    printf ( "Case #%d:\n" , y + 1 );
    for ( int i = 0 ; i < r ; i++ )
      printf ( "%s\n" , mat[i] );

  }

  return 0;

}
