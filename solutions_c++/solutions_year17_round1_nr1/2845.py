#include <stdlib.h>
#include <stdio.h>
#include <vector>

#define TESTING_CODE if(false)

struct Rect{
  int x1,x2,y1,y2;
  char letter;
  Rect(int x1, int x2, int y1, int y2, char L): x1(x1), x2(x2), y1(y1), y2(y2), letter(L){
    //TESTING_CODE printf("making rect\n");
  }
};
void doTestCase(int questionNumber);

int main(){
  int T;
  scanf("%d", &T);

  for (int i = 1; i<=T; i++){
    TESTING_CODE printf("%d\n",i);
    doTestCase(i);
  }
  return EXIT_SUCCESS;
}

void doTestCase(int questionNumber){
  int R,C;
  scanf("%d%d",&R,&C);

  char **grid = new char*[R];
  for (int i = 0; i<R; i++){
    grid[i] = new char[C]();
  }

  std::vector<Rect> rects;

  for (int i = 0; i<R; i++){
    for (int j = 0; j<C; j++){
      int c = getchar();
      while (c==' '||c=='\n') c = getchar();
      char T = c;
      grid[i][j] = T;
      if (T!='?') rects.push_back(Rect(j,j,i,i,T));
      TESTING_CODE printf("%d %d %c\n",i,j,T);
    }
  }


  for (Rect r: rects){
    TESTING_CODE printf("doing letter %c\n",r.letter);
    int topY = r.y1;
    int bottomY = r.y2;
    int topX = r.x1;
    int bottomX = r.x2;

    int a = 0;
    int b = 0;
    int c = 0;
    bool ltY = true;
    bool lbY = true;
    while (true){
      TESTING_CODE printf("topY %d bottomY %d topX %D bottomX %d\n",topY,bottomY,topX,bottomX);
      bool tY = topY>0;
      if (tY) for (int i = topX; i<=bottomX; i++) if (grid[topY-1][i]!='?'){
          tY = false;
          break;
        }

      bool bY = bottomY<R-1;
      if (bY) for (int i = topX; i<=bottomX; i++) if (grid[bottomY+1][i]!='?'){
        bY = false;
        break;
      }

      bool tX = topX>0;
      if (tX) for (int i = topY; i<=bottomY; i++) if (grid[i][topX-1]!='?'){
        tX = false;
        break;
      }

      bool bX = bottomX<C-1;
      if (bX) for (int i = topY; i<=bottomY; i++) if (grid[i][bottomX+1]!='?'){
        bX = false;
        break;
      }

      if (!(tY||bY||tX||bX)) break;
      TESTING_CODE printf("ty %d by %d tx %d bx %d\n",tY, bY, tX, bX);
      c++;

      int d = -1; //0 = bx, 1 = tX, 2 = by, 3 = tY

      if ((!(bY||tY)||c%2) && (bX||tX) ){
        b++;
        if (( (!tX) ||b%2) && bX){
          d = 0;
        } else{
          d = 1;
        }
      } else{
        a++;
        if (( (!tY) || a%2) && bY){
          d = 2;
        } else{
          d = 3;
        }
      }

      TESTING_CODE printf("d = %d\n",d);
      if (d==0){
        bottomX++;
        for (int i = topY; i<=bottomY; i++){
          grid[i][bottomX]=r.letter;
        }
      } else if (d==1){
        topX--;
        for (int i = topY; i<=bottomY; i++){
          grid[i][topX]=r.letter;
        }
      } else if(d==2){
        bottomY++;
        for (int i = topX; i<=bottomX; i++){
          grid[bottomY][i] = r.letter;
        }
      } else{
        topY--;
        for (int i = topX; i<=bottomX; i++){
          grid[topY][i] = r.letter;
        }
      }
    }
  }

  printf("Case #%d:\n", questionNumber);
  for (int i = 0; i<R; i++){
    for (int j = 0; j<C; j++){
      printf("%c",grid[i][j]);
    }
    printf("\n");
  }
}
