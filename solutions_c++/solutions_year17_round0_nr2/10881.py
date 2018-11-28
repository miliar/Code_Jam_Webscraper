#include <iostream>
#include <cstdio>
#include <bits/stdc++.h>

using namespace std;
int getMaxTidyNumber(int num);
int isTidyNumber(int num);
int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  freopen( "Bsmallinput.txt", "r", stdin );
	freopen( "Boutputsmall.txt", "w", stdout );
  int numOfTestCases;
  if((scanf("%d",&numOfTestCases)) == 1);
  int N;
  for(int i=0;i<numOfTestCases;i++)
  {
    if((scanf("%d",&N))==1);
    printf("Case #%d: %d\n",i+1,getMaxTidyNumber(N));
  }
  return 0;
}

int getMaxTidyNumber(int num)
{
  int foundTidyNumber = 0;
  while(!foundTidyNumber)
  {
    foundTidyNumber = isTidyNumber(num);
    if(!foundTidyNumber) num--;
  }
  return num;
}

int isTidyNumber(int num)
{
  int temp = num;
  int a=0,b=0,i=0;
  while(temp/10 != 0)
  {
    a = temp%10;
    temp = temp/10;
    b = temp%10;
    if(b>a) return 0;
  }
  return 1;
}
