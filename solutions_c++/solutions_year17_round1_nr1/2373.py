#include <bits/stdc++.h>
using namespace std;
int r, c;
char mat[50][50];
char row[50], col[50];

int main(){

    freopen("entretarde-alv.in","r",stdin);
    freopen("ksad.out","w",stdout);

    int tc; cin >> tc;
    for( int caso = 1 ; caso <= tc ; ++caso ){

        cin >> r >> c;

        for( int i = 0 ; i < r ; ++i ){
            for( int j = 0 ; j < c ; ++j ){
                cin >> mat[i][j];
            }
        }

        for( int i = 0 ; i < r ; ++i ){
            for( int j = 0 ; j < c ; ++j ){
                if( mat[i][j] >= 'A' && mat[i][j] <= 'Z' ){
                    char aux = mat[i][j];
                    int lo, hi;
                    for( lo = j - 1 ; ; lo-- ){
                        if( lo < 0 ){
                            break;
                        }
                        if( (mat[i][lo] >= 'A' && mat[i][lo] <= 'Z') || (mat[i][lo] >= 'a' && mat[i][lo] <= 'z') ){
                            break;
                        }
                    }
                    lo++;

                    for( hi = j + 1 ; ; ++hi ){
                        if( hi >= c ){
                            break;
                        }
                        if( (mat[i][hi] >= 'A' && mat[i][hi] <= 'Z') || (mat[i][hi] >= 'a' && mat[i][hi] <= 'z') ){
                            break;
                        }
                    }
                    hi--;
                    //cout << lo << ' ' << hi << '\n';
                    int p = i;
                    while( p < r ){

                        for( int i = lo ; i <= hi ; ++i ){
                            if( mat[p][i] != '?' ){
                                if(  mat[p][i] == aux ){
                                    goto lolzano;
                                }
                                for( int j = i - 1 ; j >= lo ; j-- ){
                                    mat[p][j] = '?';
                                }
                                goto lol;
                            }else{
                                lolzano:;
                                mat[p][i] = tolower(aux);
                            }
                        }

                        ++p;
                    }
                    lol:;
                }
            }
        }
        for( int i = r-1 ; i >= 0 ; i-- ){
            for( int j = 0 ; j < c ; j++ ){
                if( mat[i][j] == '?' ){
                    mat[i][j] = mat[i+1][j];
                }
            }
        }
        cout << "Case #"<<caso<<":\n";
        for( int i = 0 ; i < r ; i++ ){
            for( int j = 0 ; j < c ; j++ ){
                mat[i][j]=toupper(mat[i][j]);
                cout << mat[i][j];
            }cout << '\n';
        }

    }

}
