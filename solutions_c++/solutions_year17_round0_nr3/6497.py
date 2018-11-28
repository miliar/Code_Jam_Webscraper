#include <iostream>
using namespace std;

struct Stall{
  int Ls;
  int Rs;
  int max;
  int min;
  bool occupied;
};

int main(){
  int numTests;
  cin >> numTests;
  for(int testNum = 0; testNum < numTests; testNum++){
    int numStalls, numPeople;
    cin >> numStalls >> numPeople;
    int totalStalls = numStalls + 2;
    Stall* Bathroom = new Stall[totalStalls];
    Bathroom[0].occupied = true;
    Bathroom[totalStalls - 1].occupied = true;
    for(int i = 1; i < totalStalls - 1; i++){
      Bathroom[i].occupied = false;
      Bathroom[i].Ls = i - 1;
      Bathroom[i].Rs = totalStalls - 2 - i;
      if(Bathroom[i].Ls > Bathroom[i].Rs){
	Bathroom[i].max = Bathroom[i].Ls;
	Bathroom[i].min = Bathroom[i].Rs;
      }else{
	Bathroom[i].max = Bathroom[i].Rs;
	Bathroom[i].min = Bathroom[i].Ls;
      }
    }
    
    int currentStall, currentStallMax, currentStallMin;
    while(numPeople!=0){
      currentStall = -1;
      currentStallMax = -1;
      currentStallMin = -1;
      //pick stall
      for(int i = 1; i < totalStalls - 1; i++){
	if(!Bathroom[i].occupied){
	  if(Bathroom[i].min > currentStallMin){
	    currentStall = i;
	    currentStallMax = Bathroom[i].max;
	    currentStallMin = Bathroom[i].min;
	  }else if(Bathroom[i].min == currentStallMin){
	    if(Bathroom[i].max > currentStallMax){
	      currentStall = i;
	      currentStallMax = Bathroom[i].max;
	      currentStallMin = Bathroom[i].min;
	    }
	  }
	}
      } 
      
      //move into stall and update all values
      Bathroom[currentStall].occupied = true;
      int temp = currentStall -1;
      while(!Bathroom[temp].occupied){
	Bathroom[temp].Rs = currentStall - temp - 1;
	if(Bathroom[temp].Ls > Bathroom[temp].Rs){
	  Bathroom[temp].max = Bathroom[temp].Ls;
	  Bathroom[temp].min = Bathroom[temp].Rs;
	}else{
	  Bathroom[temp].max = Bathroom[temp].Rs;
	  Bathroom[temp].min = Bathroom[temp].Ls;
	}
	temp--;
      }
      temp = currentStall + 1;
      while(!Bathroom[temp].occupied){
	Bathroom[temp].Ls = temp - currentStall - 1; 
	if(Bathroom[temp].Ls > Bathroom[temp].Rs){
	  Bathroom[temp].max = Bathroom[temp].Ls;
	  Bathroom[temp].min = Bathroom[temp].Rs;
	}else{
	  Bathroom[temp].max = Bathroom[temp].Rs;
	  Bathroom[temp].min = Bathroom[temp].Ls;
	}
	temp++;
      }
      numPeople--;
    }
    cout << "Case #" << testNum + 1 << ": " 
	 << currentStallMax << " " << currentStallMin << endl;
  }//end test case iteration
  return 0;
}//end main
