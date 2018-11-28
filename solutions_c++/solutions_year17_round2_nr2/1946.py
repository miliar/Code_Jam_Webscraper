#include<iostream>
#include<cstdio>

using namespace std;

/*char* order (int r, int b, int y) {
  int tab[3] = {r,b,y}; int t;
  char tab2[3] = {'R', 'B', 'Y'}; char tc;
  if (tab[0] < tab[1]) {
    t = tab[0]; tab[0]= tab[1]; tab[1] = t;
    tc = tab2[0]; tab2[0] = tab2[1]; tab2[1] = tc;    
  }
  if (tab[0] < tab[2]) {
    t = tab[0]; tab[0]= tab[2]; tab[2] = t;
    tc = tab2[0]; tab2[0] = tab2[2]; tab2[2] = tc;    
  }
  if (tab[1] < tab[2]) {
    t = tab[1]; tab[1]= tab[2]; tab[2] = t;
    tc = tab2[1]; tab2[1] = tab2[2]; tab2[2] = tc;    
  }

  return tab2;
}*/

struct mane {
  int count;
  char let;
  string out;
};

int main (){
//  ios_base::sync_with_stdio(true);
  int t; cin >> t;
  for (int i = 1; i <= t; i++) {
    int n; int r, o, y, g, b, v; cin >> n >> r >> o >> y >> g >> b >> v;
    mane rm, om, ym, gm, bm, vm; 
//    printf("%d %d %d %d %d %d \n", r, o, y, g, b, v);
    rm.count = r; om.count = o; ym.count = y; gm.count = g; bm.count = b; vm.count = v;
    rm.let = 'R'; om.let = 'O'; ym.let = 'Y'; gm.let = 'G'; bm.let = 'B'; vm.let = 'V';

    mane tab[3] = {rm, bm, ym};
/*    printf("red %d %c\n", rm.count, rm.let);
    printf("blue %d %c\n", bm.count, bm.let);
    printf("yellow %d %c\n", ym.count, ym.let);*/
    mane tmp; 
    if (tab[0].count < tab[1].count) {tmp = tab[0]; tab[0] = tab[1]; tab[1] = tmp;}
    if (tab[0].count < tab[2].count) {tmp = tab[0]; tab[0] = tab[2]; tab[2] = tmp;}
    if (tab[1].count < tab[2].count) {tmp = tab[1]; tab[1] = tab[2]; tab[2] = tmp;}
/*    printf("1 %d %c\n", tab[0].count, tab[0].let);
    printf("2 %d %c\n", tab[1].count, tab[1].let);
    printf("3 %d %c\n", tab[2].count, tab[2].let);*/
    bool possible = true;
    possible = possible && (r <= b+y);
    possible = possible && (b <= r+y);
    possible = possible && (y <= b+r);
    if (possible) {
      char res[n];
      int j = 0;
      while (j < n) {
        int idx = 0; 
        while (!tab[idx].count) idx ++;
        res[j] = tab[idx].let; tab[idx].count --;
        j+=2;
      }
      j = 1;
      while (j < n) {
        int idx = 0; 
        while (!tab[idx].count) idx ++;
        res[j] = tab[idx].let; tab[idx].count --;
        j+=2;
      }
      printf("Case #%d: ", i);
      for (int q = 0; q < n; q++) printf("%c",res[q]);
      printf("\n");

    } else {
      printf("Case #%d: IMPOSSIBLE\n", i);
    }
  }


}
