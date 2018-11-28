#include <iostream>
#include <string>

using namespace std;

int cas, r, c;
char grid[64][64];

void sol() {
  int minr, maxr, minc, maxc;

  for (char x='A'; x<='Z'; ++x) {
    minr = maxr = minc = maxc = -1;
    for (int i=0; i<r; ++i) for (int j=0; j<c; ++j) if (grid[i][j]==x) {
      if (minr<0) minr=i;
      else if (i<minr) minr=i;
      if (maxr<0) maxr=i;
      else if (i>maxr) maxr=i;
      if (minc<0) minc=j;
      else if (j<minc) minc=j;
      if (maxc<0) maxc=j;
      else if (j>maxc) maxc=j;
    }
    if (minr>=0) {
      for (int i=minr; i<=maxr; ++i)
        for (int j=minc; j<=maxc; ++j)
          grid[i][j]=x;
    }
  }


while (1) {
  int fix=0;

  for (int i=0; i<r; ++i) for (int j=0; j<c; ++j) if (grid[i][j]=='?') {
    if (i>0) {
      char x=grid[i-1][j];
      if (x!='?') {
        minr = maxr = j;
        while (minr>0 && grid[i-1][minr-1]==x) --minr;
        while (maxr<c-1 && grid[i-1][maxr+1]==x) ++maxr;
        int ok = 1;
        for (int jj=minr; jj<=maxr; ++jj)
          if (grid[i][jj]!='?') {ok=0; break;}
        if (ok) {
          for (int jj=minr; jj<=maxr; ++jj)
            grid[i][jj]=x;
          fix=1;
          continue;
        }
      }
    }
    if (i<r-1) {
      char x=grid[i+1][j];
      if (x!='?') {
        minr = maxr = j;
        while (minr>0 && grid[i+1][minr-1]==x) --minr;
        while (maxr<c-1 && grid[i+1][maxr+1]==x) ++maxr;
        int ok = 1;
        for (int jj=minr; jj<=maxr; ++jj)
          if (grid[i][jj]!='?') {ok=0; break;}
        if (ok) {
          for (int jj=minr; jj<=maxr; ++jj)
            grid[i][jj]=x;
          fix=1;
          continue;
        }
      }
    }
    if (j>0) {
      char x=grid[i][j-1];
      if (x!='?') {
        minr = maxr = i;
        while (minr>0 && grid[minr-1][j-1]==x) --minr;
        while (maxr<r-1 && grid[maxr+1][j-1]==x) ++maxr;
        int ok = 1;
        for (int jj=minr; jj<=maxr; ++jj)
          if (grid[jj][j]!='?') {ok=0; break;}
        if (ok) {
          for (int jj=minr; jj<=maxr; ++jj)
            grid[jj][j]=x;
          fix=1;
          continue;
        }
      }
    }
    if (j<c-1) {
      char x=grid[i][j+1];
      if (x!='?') {
        minr = maxr = i;
        while (minr>0 && grid[minr-1][j+1]==x) --minr;
        while (maxr<r-1 && grid[maxr+1][j+1]==x) ++maxr;
        int ok = 1;
        for (int jj=minr; jj<=maxr; ++jj)
          if (grid[jj][j]!='?') {ok=0; break;}
        if (ok) {
          for (int jj=minr; jj<=maxr; ++jj)
            grid[jj][j]=x;
          fix=1;
          continue;
        }
      }
    }
  }

  if (fix==0) break;
}



}


int main() {
  cin>>cas;

  for (int k=1; k<=cas; ++k) {
    cin>>r>>c;
    for (int i=0; i<r; ++i)
      for (int j=0; j<c; ++j)
        cin>>grid[i][j];
    sol();
    cout<<"Case #"<<k<<":"<<endl;
    for (int i=0; i<r; ++i) {
      for (int j=0; j<c; ++j)
        cout<<grid[i][j];
      cout<<endl;
    }
  }
  return 0;
}
