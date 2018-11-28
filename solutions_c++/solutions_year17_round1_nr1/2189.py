#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

char mat[100][100];
int v[30], values[30], valuesdouble[30];
int minrow[30], maxrow[30], maxcol[30], mincol[30];

int hei[30], wid[30];

int main () {
  ofstream myfile;
  ifstream input;
  input.open("input.txt");
  myfile.open ("output.txt");
  int t;
  input>>t;
  for(int i=1; i<=t; i++){
		int r, c;
		char s;
		input>>r>>c;

    for(int j = 0; j<30; j++){
      v[j]=0;
      maxrow[j]=-1;
      maxcol[j]=-1;
      minrow[j]=30;
      mincol[j]=30;
    }

    int cont = 0;
    int contdouble = 0;

		for(int j=0; j<r; j++) {
      for(int k=0; k<c; k++) {
  			input>>s;
        mat[j][k] = s;
        if (s != '?') {
          int aux = s - 'A';
          v[aux]++;
          if(v[aux] == 1) {
            values[cont] = aux;
            cont++;
          }
          if(v[aux] > 1) {
            valuesdouble[contdouble] = aux;
            contdouble++;
          }
          minrow[aux] = min(minrow[aux], j);
          maxrow[aux] = max(maxrow[aux], j);
          mincol[aux] = min(mincol[aux], k);
          maxcol[aux] = max(maxcol[aux], k);
        }
  		}
		}
    /*for(int j=0; j<r; j++) {
      for(int k=0; k<c; k++) {
        cout<<mat[j][k];
      }
      cout<<endl;
    }
    cout<<"----------------"<<endl;*/

    for(int j=0; j<contdouble; j++) {
      int aux = valuesdouble[j];
      for(int r1=minrow[aux]; r1<=maxrow[aux]; r1++) {
        for(int c1=mincol[aux]; c1<=maxcol[aux]; c1++){
          mat[r1][c1] = 'A' + aux;
        }
      }
    }

    for(int j=0; j<cont; j++) {
      int aux = values[j];
      hei[aux] = maxrow[aux] - minrow[aux] + 1;
      wid[aux] = maxcol[aux] - mincol[aux] + 1;
    }
    /*for(int j=0; j<r; j++) {
      for(int k=0; k<c; k++) {
        cout<<mat[j][k];
      }
      cout<<endl;
    }
    cout<<"----------------"<<endl;*/

    int atual = -1;
    bool ok;

    for(int j=0; j<r; j++) {
      atual = -1;
      for(int k=0; k<c; k++) {
        if (mat[j][k] == '?') {
          if (atual != -1) {
            if (hei[atual] == 1) {
              mat[j][k] = atual + 'A';
              maxcol[atual]++;
              wid[atual]++;
            } else {
              ok = true;
              for(int r1=minrow[atual]; r1<=maxrow[atual]; r1++) {
                if (mat[r1][k] != '?') {
                  ok = false;
                }
              }
              if (ok) {
                for(int r1=minrow[atual]; r1<=maxrow[atual]; r1++) {
                  mat[r1][k] = atual + 'A';
                }
              } else {
                atual = -1;
              }
            }
          }
        } else {
          atual = mat[j][k] - 'A';
        }
      }
    }
    /*for(int j=0; j<r; j++) {
      for(int k=0; k<c; k++) {
        cout<<mat[j][k];
      }
      cout<<endl;
    }
    cout<<"----------------"<<endl;*/

    for(int j=r-1; j>=0; j--) {
      atual = -1;
      for(int k=c-1; k>=0; k--) {
        if (mat[j][k] == '?') {
          if (atual != -1) {
            if (hei[atual] == 1) {
              mat[j][k] = atual + 'A';
              mincol[atual]--;
              wid[atual]++;
            } else {
              ok = true;
              for(int r1=minrow[atual]; r1<=maxrow[atual]; r1++) {
                if (mat[r1][k] != '?') {
                  ok = false;
                }
              }
              if (ok) {
                for(int r1=minrow[atual]; r1<=maxrow[atual]; r1++) {
                  mat[r1][k] = atual + 'A';
                }
              } else {
                atual = -1;
              }
            }
          }
        } else {
          atual = mat[j][k] - 'A';
        }
      }
    }
    /*
    for(int j=0; j<r; j++) {
      for(int k=0; k<c; k++) {
        cout<<mat[j][k];
      }
      cout<<endl;
    }
    cout<<"----------------"<<endl;
*/

    for(int k=0; k<c; k++) {
      atual = -1;
      for(int j=0; j<r; j++) {
        if (mat[j][k] == '?') {
          if (atual != -1) {
            if (wid[atual] == 1) {
              mat[j][k] = atual + 'A';
              maxrow[atual]++;
              hei[atual]++;
            } else {
              ok = true;
              for(int c1=mincol[atual]; c1<=maxcol[atual]; c1++) {
                if (mat[j][c1] != '?') {
                  ok = false;
                }
              }
              if (ok) {
                for(int c1=mincol[atual]; c1<=maxcol[atual]; c1++) {
                  mat[j][c1] = atual + 'A';
                }
              } else {
                atual = -1;
              }
            }
          }
        } else {
          atual = mat[j][k] - 'A';
        }
      }
    }
    /*for(int j=0; j<r; j++) {
      for(int k=0; k<c; k++) {
        cout<<mat[j][k];
      }
      cout<<endl;
    }
    cout<<"----------------"<<endl;*/

    for(int k=c-1; k>=0; k--) {
      atual = -1;
      for(int j=r-1; j>=0; j--) {
        if (mat[j][k] == '?') {
          if (atual != -1) {
            if (wid[atual] == 1) {
              mat[j][k] = atual + 'A';
              minrow[atual]--;
              hei[atual]++;
            } else {
              ok = true;
              for(int c1=mincol[atual]; c1<=maxcol[atual]; c1++) {
                if (mat[j][c1] != '?') {
                  ok = false;
                }
              }
              if (ok) {
                for(int c1=mincol[atual]; c1<=maxcol[atual]; c1++) {
                  mat[j][c1] = atual + 'A';
                }
              } else {
                atual = -1;
              }
            }
          }
        } else {
          atual = mat[j][k] - 'A';
        }
      }
    }
    /*
    for(int j=0; j<r; j++) {
      for(int k=0; k<c; k++) {
        cout<<mat[j][k];
      }
      cout<<endl;
    }
    cout<<"----------------"<<endl;*/

		myfile<<"Case #"<<i<<":"<<endl;
    for(int j=0; j<r; j++) {
      for(int k=0; k<c; k++) {
        myfile<<mat[j][k];
      }
      myfile<<endl;
    }
  }
  myfile.close();
  input.close();
  return 0;
}
