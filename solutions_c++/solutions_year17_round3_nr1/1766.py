#include <iostream>
#include <algorithm>
//# define M_PI           3.14159265358979323846
using namespace std;

class Pancake{
public:
  long double radius;
  long double height;
  long double sideSurfaceArea;
  
  Pancake(){
    radius = 0;
    height = 0;
    sideSurfaceArea = 0;
  }
  /*
  Pancake(int newRadius, int newHeight){
    radius = newRadius;
    height = newHeight;
  }
  */
};

bool pancakeSA (Pancake i, Pancake j){
  return i.sideSurfaceArea > j.sideSurfaceArea;
}

int main(){
  const long double M_PI = 3.141592653589793238L;
  int numTests, numTotalPancakes, numChosenPancakes;
  cin >> numTests;

  for(int testNum = 1; testNum <= numTests; testNum++){
    int numTotalPancakes, numChosenPancakes;
    cin >> numTotalPancakes >> numChosenPancakes;
    Pancake pancakes[numTotalPancakes];
    for(int pancakeNum = 0; pancakeNum < numTotalPancakes; pancakeNum++){
      long double newRadius, newHeight;
      cin >> newRadius >> newHeight;
      pancakes[pancakeNum].radius = newRadius;
      pancakes[pancakeNum].height = newHeight;  
      pancakes[pancakeNum].sideSurfaceArea = 2 * M_PI * newRadius * newHeight;
    }
    //sort pancakes in descending order by height
    sort(pancakes, pancakes + numTotalPancakes, pancakeSA);
    long double maxExposedArea = 0;
    for(int bottomPancake = 0; bottomPancake < numTotalPancakes; bottomPancake++){
      long double bottomPancakeRadius = pancakes[bottomPancake].radius;
      long double exposedArea = M_PI * bottomPancakeRadius * bottomPancakeRadius;
      exposedArea += pancakes[bottomPancake].sideSurfaceArea;
   
      int pancakesLeft = numChosenPancakes - 1;
      int currentIndex = 0;
      while(pancakesLeft > 0 && currentIndex < numTotalPancakes){
	if(currentIndex != bottomPancake && pancakes[currentIndex].radius <= bottomPancakeRadius){
	  exposedArea += pancakes[currentIndex].sideSurfaceArea;
	  pancakesLeft --;
	}
	currentIndex ++;
      }
      if (pancakesLeft != 0){
	exposedArea = 0;
      }
      if (exposedArea > maxExposedArea){
	maxExposedArea = exposedArea;
      }
    }
    cout.precision(17);
    cout << "Case #" << testNum << ": " << fixed << maxExposedArea << endl;
    /*
    for (int i = 0 ; i < numTotalPancakes; i++){
      cout << pancakes[i].height << "  " << pancakes[i].radius << endl;
    }
    */

  }
  return 0;

}
