#include <stdio.h>
#include <algorithm>
#include <vector>
#define ROWS 2

using namespace std;

typedef struct Position{
  long leftDistance;
  long rightDistance;
  long stallIndex;
} Position;

void setLeftAndRightSpaces(vector<Position>*,vector<int>*,vector<long>*);
void merge(vector<Position>*,long,long,long,int);
void mergeAndSort(vector<Position>*,long,long,int);
long getMinOfPosition(Position);
long getMaxOfPosition(Position position);
vector<Position> getMinOrMaxOverSet(vector<Position>*,int);
Position getLeftMostStall(vector<Position>*);

int main(){
  int cases,k,n,i,j=1;
  
  scanf("%d",&cases);

  while(cases--){
    scanf("%d %d",&n,&k);
    vector<int> stalls;
    vector<long> occupiedStalls;
    stalls.insert(stalls.begin(),1);

    for(i=0;i<n;i++)
      stalls.push_back(0);

    stalls.push_back(1);

    occupiedStalls.push_back(0);
    occupiedStalls.push_back(stalls.size()-1);

    Position leftMostPosition;

    for(i=0;i<k;i++){
      sort(occupiedStalls.begin(),occupiedStalls.end());
      vector<Position> positions;
      setLeftAndRightSpaces(&positions,&stalls,&occupiedStalls);
      vector<Position> minSet = getMinOrMaxOverSet(&positions,1);

      if(minSet.size() > 1){
        vector<Position> maxSet = getMinOrMaxOverSet(&minSet,0);
        if(maxSet.size() > 1)
          leftMostPosition = getLeftMostStall(&maxSet);
        else
          leftMostPosition =  maxSet[0];
      }
      else
        leftMostPosition =  minSet[0];

      stalls[leftMostPosition.stallIndex] = 1;
      occupiedStalls.push_back(leftMostPosition.stallIndex);
    }

    printf("Case #%d: %ld %ld\n",j++,getMaxOfPosition(leftMostPosition),getMinOfPosition(leftMostPosition));
    
  }
 
  return 0;
}

void setLeftAndRightSpaces(vector<Position>* positions,vector<int>* stalls,vector<long>* occupiedStalls){
  long i,j=0;

  long nearestLeftBusyStall = occupiedStalls->at(0);
  long nearestRightBusyStall = stalls->size()-1;

  for(i=1;i<stalls->size()-1;i++){
    if(stalls->at(i) == 0){

      while(i > occupiedStalls->at(j)){
        nearestLeftBusyStall = occupiedStalls->at(j);
        j++;
      }

      nearestRightBusyStall = occupiedStalls->at(j);
      
      Position position;
      position.stallIndex = i;
      position.leftDistance = i-1-nearestLeftBusyStall; 
      position.rightDistance= nearestRightBusyStall-1-i;

      positions->push_back(position);
    }
  }

}

vector<Position> getMinOrMaxOverSet(vector<Position>* positions,int isMinSet){
  vector<Position> set;
  mergeAndSort(positions,0,positions->size()-1,isMinSet);
  long i = positions->size()-1;
  Position max = positions->at(i);
 
  if(isMinSet){ 
    while(i >= 0 && getMinOfPosition(positions->at(i)) == getMinOfPosition(max)){
      set.push_back(positions->at(i));
      i--;
    }
  }
  else{
    while(i>=0 && getMaxOfPosition(positions->at(i)) == getMaxOfPosition(max)){
      set.push_back(positions->at(i));
      i--;
    }
  }

  return set;
}

Position getLeftMostStall(vector<Position>* positions){
  Position leftMost = positions->at(0);
  
  for(int i=1;i<positions->size();i++){
    if(leftMost.leftDistance > positions->at(i).leftDistance)
      leftMost = positions->at(i);
  }

  return leftMost;
}

void mergeAndSort(vector<Position>* positions,long p,long r,int isMinSort){
  if(p<r){
    long q = (p+r)/2;
    mergeAndSort(positions,p,q,isMinSort);
    mergeAndSort(positions,q+1,r,isMinSort);
    merge(positions,p,q,r,isMinSort);
  }
}

void merge(vector<Position>* positions,long p,long middle,long r,int isMinSort){
  vector<Position> left;
  vector<Position> right;

  int i,j,k;   
  for(i=0;i<(middle-p+1);i++)
    left.push_back(positions->at(p+i));

  for(j=0;j<(r-middle);j++)
    right.push_back(positions->at(middle+1+j));

  k=p;
  i=j=0;
  
  if(isMinSort){
    while(i<left.size() && j<right.size()){
      if(getMinOfPosition(left[i]) <=  getMinOfPosition(right[j]))
        positions->at(k++) = left[i++];
      else
        positions->at(k++) = right[j++];
    }
  }
  else{
    while(i<left.size() && j<right.size()){
      if(getMaxOfPosition(left[i]) <= getMaxOfPosition(right[j]))
        positions->at(k++) = left[i++];
      else
        positions->at(k++) = right[j++];
    }
  }
  
  while(i<left.size())
    positions->at(k++) = left[i++];

  while(j<right.size())
    positions->at(k++) = right[j++];
}

long getMinOfPosition(Position position){
  if(position.leftDistance > position.rightDistance)
    return position.rightDistance;
  else{
    return position.leftDistance;
  }
}

long getMaxOfPosition(Position position){
  if(position.leftDistance > position.rightDistance)
    return position.leftDistance;
  else
    return position.rightDistance;
}
