#include <bits/stdc++.h>
using namespace std;

int main(void) {
  int t, tt, r, c, i, j, k, b, l;
  char map[30][30];
  char tc;
  int row[30];
  for(i=0; i<30; i++) {
    for(j=0; j<30; j++) {
      map[i][j] = '?';
    }
    row[i] = 0;
  }
  /*  for(l=0; l<30; l++) {
      for(j=0; j<30; j++) {
	printf("%c", map[l][j]);
      }
      cout << endl;
      }*/
  cin >> t;
  for(tt = 1; tt<=t; tt++) {
    cin >> r >> c;
    for(i=0; i<r; i++) {
      row[i] = 0;
    }
    b = 28;
    for(i=0; i<r; i++) {
      for(j=0; j<c; j++) {
	cin >> tc;
	map[i][j] = tc;
	if(tc!='?') row[i]++;
      }
      getchar();
      if(b==28 && row[i]) b = i;
      //cout << i << " and " << b << endl;
    }
    /*
    for(i=0; i<r; i++) {
      for(j=0; j<c; j++) {
	printf("%c", map[i][j]);
      }
      cout << endl;
    }
    */
    //printf("b is %d\n", b);
    for(i=b; i<r; i++) {
      /*      for(l=0; l<r; l++) {
	for(j=0; j<c; j++) {
	  cout << map[l][j];
	}
	cout << endl;
	}*/
      if(row[i]) {
	for(j=0; j<c; j++) {
	  if(map[i][j]=='?') {
	    for(k=j; k < c; k++) {
	      if(map[i][k]!='?') {
		for(;j<k; j++) {
		  map[i][j] = map[i][k];
		}
		break;
	      }
	      else if(k+1 == c) {
		tc = map[i][j-1];
		for(; j<c; j++) {
		  map[i][j] = tc;
		}
	      }
	    }
	  }
	}
      }
      else {
	for(j=0; j<c; j++) {
	  map[i][j] = map[i-1][j];
	}
      }
    }
    if(b>0) {
      for(i=b-1; i>=0; i--) {
	for(j=0; j<c; j++) {
	  map[i][j] = map[b][j];
	}
      }
    }
    printf("Case #%d:\n", tt);
    for(i=0; i<r; i++) {
      for(j=0; j<c; j++) {
	printf("%c", map[i][j]);
      }
      printf("\n");
    }
  }
  return 0;
}
