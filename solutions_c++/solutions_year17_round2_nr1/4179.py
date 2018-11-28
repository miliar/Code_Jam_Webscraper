#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

typedef struct {
  double Pos;
  double Speed;
} h; 

bool compare(h a1, h a2) {
  return (a1.Pos < a2.Pos);
}


int mymain(int test) {
  int D, N;
  scanf("%d %d",&D,&N);
  vector<h> horses;
  horses.resize(N);
  for (int i=0;i<N;i++) {
    scanf("%lf %lf", &horses[i].Pos, &horses[i].Speed);
  }
  //printf("\nooh");
  sort(horses.begin(),horses.end(),compare);
  double times[N];
  int y;
  y = 0;
  for (int i=0;i<N-1;i++) {
    if (horses[i].Speed < horses[i+1].Speed) {
      y = i;
    }
    else if (i == N-2) y = N-1;
  }
  double time = 0;
  while (horses[0].Pos < (double)D) {
    //printf("\nooh");
    if (y == 0) {
      time += (D-horses[0].Pos)/horses[0].Speed;
      break;
    }
    else {
      double times[y];
      for (int i=y-1;i>=0;i--) {
        times[i] = (((horses[i+1].Pos-horses[i].Pos)*horses[i+1].Speed)/(horses[i].Speed - horses[i+1].Speed))/horses[i+1].Speed;
      }
      int x = -1;
      for (int i=0;i<y;i++) {
        if (times[i] > 0) {
          x = i;
          break;
        }
      }
      if (x == -1) {
        y = 0;
        continue;
      }
      for (int i=1;i<y;i++) {
        if (times[x] > times[i]) x = i;
      }
      //printf("\nhorse %d crosses %d at %lf",x+1,x+2,times[x]);
      if (horses[0].Pos + (times[x]*horses[0].Speed) > (double) D) {
        time += (D-horses[0].Pos)/horses[0].Speed;
        break;
      }
      for (int i=0;i<=y;i++) {
        horses[i].Pos += (times[x]*horses[i].Speed);
        if (x == i) {
          horses[i].Speed = horses[i+1].Speed;
          time += times[i];
        }
      }
      horses.erase(horses.begin()+x);
      y--;
    }
  }
  printf("%lf\n", (double)(D)/time);


      
      

  return 0; 

}

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    int TEST;
    scanf("%d", &TEST);
    for(int i=1; i<=TEST; i++)
    {
        printf("Case #%d: ", i);
        mymain(i);
    }
    return 0;
}
