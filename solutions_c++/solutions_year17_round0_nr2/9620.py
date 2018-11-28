#include<cstdio>
#include<iostream>
#include <bits/stdc++.h>
using namespace std;

int sizeOfNum;
int getSize(long long int num);
void setDigitArray(int *arr, long long int num);
void printMaxTidyNumber(int *arr);
void getMaxTidyNumber(int* arr);
int getNonZeroValueIndex(int *arr,int index);
int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  freopen( "B-large (2).in", "r", stdin );
	freopen( "tidynumbers_output.txt", "w", stdout );
  int numOfTestCases;
  if((scanf("%d",&numOfTestCases)) == 1);
  int *digits = new int[19];
  long long int N;
  for(int i=0;i<numOfTestCases;i++)
  {
    if((scanf("%lld",&N)) == 1);
    setDigitArray(digits,N);
    getMaxTidyNumber(digits);
    printf("Case #%d: ",i+1);
    printMaxTidyNumber(digits);
  }
  return 0;
}

void setDigitArray(int *arr, long long int num)
{
  sizeOfNum = getSize(num);
  int tempSize = sizeOfNum;
  while(num != 0)
  {
    arr[tempSize - 1] = num%10;
    num = num/10;
    tempSize--;
  }
}

int getSize(long long int num)
{
  int size = 0;
  while(num != 0)
  {
    size++;
    num = num/10;
  }
  return size;
}

void printMaxTidyNumber(int *arr)
{
  for(int i=0;i<sizeOfNum;i++)
  {
    if(i == 0 && arr[i] == 0)
      continue;
    printf("%d",arr[i]);
  }
  printf("\n");
}


void getMaxTidyNumber(int* arr)
{
  for(int j = sizeOfNum-2 ; j>=0 ;j--)
  {
    if(arr[j]>arr[j+1])
    {
        int nonZeroPos = getNonZeroValueIndex(arr,j);
        arr[nonZeroPos] -= 1;
        for(int k = nonZeroPos+1; k<sizeOfNum;k++)
        {
          arr[k] = 9;
        }
    }
  }
}

int getNonZeroValueIndex(int *arr,int index)
{
  while(index !=0)
  {
    if(arr[index] != 0)
      break;
    index--;
  }
  return index;
}
