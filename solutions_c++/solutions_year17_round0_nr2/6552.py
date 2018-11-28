#include<bits/stdc++.h>
using namespace std;
int tot;
bool check(int* arr,int len)
{
  for(int i=1;i<len;i++)
  {
     if(arr[i]-arr[i-1] < 0)
       return false;
  }
  return true;
}
void solve()
{
tot++;
  string inp;
  cin >> inp;
  int x = inp.length();
  int arr[x];
  for(int i =0;i<x;i++)
    arr[i] = inp[i] - '0';
    
  
  for(int i=x-1;i>0;i--)
  {
    if(!check(arr,x))
    {
      arr[i] = 9;
      arr[i-1] -=1;
    }
    else
     break;
  }
  
  int flag = 0;
  cout << "Case #"<<tot<<": ";
  for(int i=0;i<x;i++)
  {
    if(arr[i] == 0 && flag == 0)
    {
      
    }
    else
    {
      cout << arr[i];
      flag = 1;
    }
  }
  cout << endl;
}

int main()
{
  tot = 0;
  int t;
  cin >> t;
  while(t--)
    solve();
}
