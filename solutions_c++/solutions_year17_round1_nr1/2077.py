#include <iostream>
#include <string.h>
#include <algorithm>
#include <string.h>
#include <vector>
#include <queue>
#include <cmath>
#include <math.h>
#include <map>
#include <set>
#include <iterator>
using namespace std;
#define FOR(i,f,c) for(int i=f;i<c;i++)
#define FORM(i,f,c) for(int i=f;i>c;i--)
char cake[25][25];
char get(int o, int u)
{
  char x='?';
  FORM(i,u-1,-1)
  {
    if(cake[i][o] != '?')
    {
      x=cake[i][o];
      break;
    }
  }
  return x;
}
char gets(int o, int u,int C)
{
  char x='?';
  FOR(i,u+1,C)
  {
    if(cake[o][i] != '?')
    {
      x=cake[o][i];
      break;
    }
  }
  return x;
}

char getsm(int o, int u)
{
  char x='?';
  FORM(i,u-1,-1)
  {
    if(cake[o][i] != '?')
    {
      x=cake[o][i];
      break;
    }
  }
  return x;
}

char getp(int o,int u,int R)
{
  char x='?';
  FOR(i,u+1,R)
  {
    if(cake[i][o] != '?')
    {
      x=cake[i][o];
      break;
    }
  }
  return x;
}

int main()
{
  int T;
  cin >> T;
  FOR(tt,1,T+1)
  {
    cout << "Case #" << tt << ": ";
      int R,C;
      cin >> R >> C;
      string rc;
      FOR(i,0,R)
      {
        cin >> rc;
        int j = 0;
        for(char c : rc)
        {
          cake[i][j] = c;
          j++;
        }
      }
      FOR(o,0,R)
      {
        FOR(u,0,C)
        {
          if(cake[o][u] == '?')
          {
            if(getsm(o,u) != '?')
            cake[o][u] = getsm(o,u);
            else if(gets(o,u,C) != '?') //&& cake[o][u+2] != cake[o][u+1]
            cake[o][u] = gets(o,u,C);
          }
        }
      }
      FOR(o,0,C)
      {
        FOR(u,0,R)
        {
          if(cake[u][o] == '?')
          {
            if(get(o,u) != '?')
            cake[u][o] = get(o,u);
            else if(getp(o,u,R) != '?')
            cake[u][o] = getp(o,u,R);
          }
        }
      }
      cout << endl;
      FOR(o,0,R)
      {
        FOR(u,0,C)
        {
          cout << cake[o][u];
        }
        cout << endl;
      }
  }
  return 0;
}
