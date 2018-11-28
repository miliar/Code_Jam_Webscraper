#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>

using namespace std;

int Q;
int N,K;

typedef struct DOOR
{
  int besetzt;
  int left;
  int right;
}Door;

Door o[1000010];

int Cmin(int a, int b)
{
  return a < b ? a : b;
}

int Cmax(int a, int b)
{
  return a > b ? a : b;
}

int getFreeLeft(int loc)
{
  int counter = 0;
  while(o[loc-1].besetzt == 0){
    counter++;
    loc--;
  }
  return counter;
}

int getFreeRight(int loc)
{
  int counter = 0;
  while(o[loc+1].besetzt == 0){
    counter++;
    loc++;
  }
  return counter;
}

int main()
{
  int q,i,j,z;
  int k;
  scanf("%d",&Q);
  for(q = 1; q <= Q; q++)
  {
    scanf("%d %d",&N, &K);
    for(i = 1; i<= N+2; i++)
    {
      o[i].besetzt = 0;
    }

    o[1].besetzt = 1; // besetzt
    o[N+2].besetzt = 1; //besetzt

    int last; //last chosen

    for(k = 1; k <= K; k++)
    {
      int max = 0;
      int max2 = 0;
      for(j = 2; j<=N+1; j++)
      {
        if(o[j].besetzt == 1)continue;
        o[j].left = getFreeLeft(j);
        o[j].right = getFreeRight(j);

      //  printf("NODE: %d left: %d right: %d\n",j,o[j].left, o[j].right);

        max = Cmax(max, Cmin(o[j].left, o[j].right));

      }
      vector<int> vec;
      vector<int> vec2;
      for(j = 2; j<=N+1; j++)
      {
        if(o[j].besetzt == 1)continue;
        if(Cmin(o[j].left, o[j].right) == max)
        {
          vec.push_back(j); //pushing all of them
          max2 = Cmax(max2, Cmax(o[j].left, o[j].right));
        }
      }

      //if size one choose this one!
      if(vec.size() == 1)
      {
        o[vec[0]].besetzt = 1;
        last = vec[0];
      }else
      {
          //size is bigger
          for(j = 0; j < vec.size(); j++)
          {
              if(Cmax(o[vec[j]].left, o[vec[j]].right) == max2)vec2.push_back(vec[j]);
          }

          o[vec2[0]].besetzt = 1; //cos choose the first one or the one which is on the left site!
          last = vec2[0];
      }

    }
    printf("Case #%d: %d %d\n",q, Cmax(o[last].right, o[last].left), Cmin(o[last].right, o[last].left));

  }
  return 0;
}
