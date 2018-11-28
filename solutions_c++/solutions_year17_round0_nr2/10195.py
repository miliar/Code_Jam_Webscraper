#include <stdio.h>
#include <vector>

using namespace std;

int isTheArraySorted(vector<int>);
int isTidyNumber(long);

int main(){
  int cases,i=1;
  long n;

  scanf("%d",&cases);

  while(cases--){
    scanf("%ld",&n);

    while(!isTidyNumber(n)){
      n--;
    }

    printf("Case #%d: %ld\n",i++,n);
    
  }

  return 0;
}

int isTidyNumber(long number){
  if(number%10 == 0)
    return 0;

  vector<int> numbers;
  int residue;

  while(number >= 1){
    residue = number%10;
    numbers.push_back(residue);
    number = number/10;
  }

  return isTheArraySorted(numbers);
}

int isTheArraySorted(vector<int> array){
  if(array.size() == 1)
    return 1;

  int isSorted=1;
  int i=array.size()-1;

  while(i > 0 && isSorted){
    if(array[i] > array[i-1])
      isSorted = 0;

    i--;
  }
  
  return isSorted; 
}
