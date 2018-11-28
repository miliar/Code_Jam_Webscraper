/*
tags: 
LANG: C++11
*/

#ifdef __APPLE__
#include "./problems/stdc++.h"
#else
#include<bits/stdc++.h> //g++ -std=c++11
#endif

using namespace std;

//#define DEBUG
#ifndef DEBUG
  #define din if(0) cin
  #define dout if(0) cout
#else
  #define din cin
  #define dout cout
#endif


#define inf (1 << 30)
#define pi (2*asin(1))
#define repall(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define rep(i,x,y) for (int i = x; i < y; i++)
#define irep(i,x,y) for (int i = x; i >= y; i--)
#define clr(A,x) memset(A, x, sizeof A)
#define pb push_back
#define mp make_pair
#define MAX 100005

typedef vector < int > vi;
typedef pair < int , int > pii;
typedef vector < pii > vii;
typedef long long int i64;
typedef vector < i64 > vi64;

int n, m;
string grid[30];
int cnt[30];
vii let;

bool valid (int i , int j)
{
  return i>= 0  and j >= 0 and i < n and j < m;
}
void full_up_right(int i, int j, char letter)
{
  if(!valid(i, j)) return;
  if(grid[i][j] == '?')
    grid[i][j] = letter;
  if(grid[i][j] != letter) return;
  
  full_up_right(i - 1, j, letter);
  full_up_right(i, j - 1, letter);
    
}
void full_down_right(int i, int j, char letter)
{
  if(!valid(i, j)) return;
  if(grid[i][j] == '?')
    grid[i][j] = letter;
  if(grid[i][j] != letter) return;
  
  full_down_right(i + 1, j, letter);
  full_down_right(i, j - 1, letter);
    
}
void full_up_left(int i, int j, char letter)
{
  if(!valid(i, j)) return;
  if(grid[i][j] == '?')
    grid[i][j] = letter;
  if(grid[i][j] != letter) return;
  
  full_up_left(i - 1, j, letter);
  full_up_left(i, j + 1, letter);
    
}
void full_down_left(int i, int j, char letter)
{
  if(!valid(i, j)) return;
  if(grid[i][j] == '?')
    grid[i][j] = letter;
  if(grid[i][j] != letter) return;
  
  full_down_left(i + 1, j, letter);
  full_down_left(i, j + 1, letter);
    
}
int main() {
  int test;
  scanf("%d", &test);
  rep(te, 1, test + 1)
  {
    scanf("%d %d", &n, &m);
    memset(cnt, 0, sizeof  cnt);
    let.clear();
    
    rep(i, 0, n)
    {
      cin>>grid[i];
      rep(j, 0, m)
      {
        if(grid[i][j] != '?')
        {
          cnt[i]++;
          let.push_back(pii(i, j));
          dout<<i<< " " <<j<<endl;
        }
        
      }
    }  
       
    rep(i, 0, (int)let.size())
    {
      if(cnt[let[i].first] == 1)
      {
        full_up_left(let[i].first, let[i].second, grid[let[i].first][let[i].second]);
        full_up_right(let[i].first, let[i].second, grid[let[i].first][let[i].second]);
      }
      else
      {
        full_up_right(let[i].first, let[i].second, grid[let[i].first][let[i].second]);
        if((i + 1 < (int)let.size() and let[i].first != let[i+1].first) or i + 1 >= (int)let.size())
        {
          full_up_left(let[i].first, let[i].second, grid[let[i].first][let[i].second]);
        }
      }
    }
    
    irep(i, (int)let.size() -1, 0)
    {
      if(cnt[let[i].first] == 1)
      {
        full_down_right(let[i].first, let[i].second, grid[let[i].first][let[i].second]);
        full_down_left(let[i].first, let[i].second, grid[let[i].first][let[i].second]);
      }
      else
      {
        full_down_left(let[i].first, let[i].second, grid[let[i].first][let[i].second]);
        if((i - 1 >= 0 and let[i].first != let[i - 1].first) or i - 1 < 0)
        {
          full_down_right(let[i].first, let[i].second, grid[let[i].first][let[i].second]);
        }
      }
    }
    
    printf("Case #%d:\n", te);
    rep(i, 0, n)
    {
      cout<<grid[i]<<endl;
    } 
  }
}
