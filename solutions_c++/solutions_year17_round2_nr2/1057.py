#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
using namespace std;

int N,R,O,Y,G,B,V;

void read()
{
  cin >> N >> R >> O >> Y >> G >> B >> V;
}

char rst[1001];

void solve()
{
  if(R>B+Y || B>R+Y || Y>R+B)
    {
      strcpy(rst,"IMPOSSIBLE");
      return;
    }
  int SUM = R+B+Y;
  int RB = SUM-2*Y;
  int RY = SUM-2*B;
  int BY = SUM-2*R;
  if((RB-RY)%2!=0 || (RB-BY)%2!=0)
    {
      strcpy(rst,"IMPOSSIBLE");
      return;
    }

  int min,med,max;
  char MIN_MAX,MIN_MED,MED_MAX;
  int A[]={RB,RY,BY};
  char I[3][3]={
    {' ','R','B'},
    {'R',' ','Y'},
    {'B','Y',' '},};
  int X[]={0,1,2};
  do
    {
      if(A[X[0]] <= A[X[1]] && A[X[1]]<= A[X[2]])
	{
	  min = A[X[0]];
	  med = A[X[1]];
	  max = A[X[2]];
	  MIN_MED = I[X[0]][X[1]];
	  MIN_MAX = I[X[0]][X[2]];
	  MED_MAX = I[X[1]][X[2]];
	  break;
	}
    }while(next_permutation(X,X+3));
  int k=0;
  while(min>0)
  {
    rst[k++]=MIN_MAX;
    rst[k++]=MIN_MED;
    rst[k++]=MED_MAX;
    min--;
    med--;
    max--;
  }
  rst[k++]=MIN_MAX;
  if(max>0)
    {
      rst[k++]=MED_MAX;
      max--;
      while(med>0)
	{
	  rst[k++]=MIN_MED;
	  rst[k++]=MED_MAX;
	  med-=2;
	}
      rst[k++]=MIN_MAX;
      max--;
      while(max>0)
	{
	  rst[k++]=MED_MAX;
	  rst[k++]=MIN_MAX;
	  max-=2;
	}
	
    }
    rst[k-1]='\0';
}

int main()
{
  int T;
  cin >> T;
  for(int t=1;t<=T;t++)
    {
      read();
      cout << "Case #" << t << ": " ;
      solve();
      cout << rst << endl;
    }
  return 0;
}
