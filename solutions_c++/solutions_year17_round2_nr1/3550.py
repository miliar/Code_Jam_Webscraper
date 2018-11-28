#include <iostream>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <cassert>
#include <string>
#include <algorithm>
#include <iomanip>

using namespace std;

double TimeToDestination(int Destination, int Position, int Speed){
  double Distance = Destination - Position;
  double SPEED = (double)Speed;
  double answer = Distance/SPEED;
  return answer;
}

int main(){

  int numberofTestCases = 0;
  int TEMP;
  cin >> numberofTestCases;
  vector<int> Destinations;
  vector<int> numberofOtherHorses;

  for(int i = 0; i < numberofTestCases; i++){
    cin >> TEMP;
    Destinations.push_back(TEMP);
    cin >> TEMP;
    numberofOtherHorses.push_back(TEMP);


    vector<int> HorsePositions;
    vector<int> HorseSpeeds;

    for(int q = 0; q < numberofOtherHorses[i]; q++){//Take in all speed and position inputs
      cin >> TEMP;
      HorsePositions.push_back(TEMP);
      cin >> TEMP;
      HorseSpeeds.push_back(TEMP);
    }

    vector<double> HorseTimes;

    int SlowestSpeed = HorseSpeeds[0];
    int indexofSlowest;

    for(int r = 0; r < HorsePositions.size(); r++){
      HorseTimes.push_back(TimeToDestination(Destinations[i], HorsePositions[r], HorseSpeeds[r]));
    }
    /*for(int r = 0; r < HorsePositions.size(); r++){
      cout << "Horse time: " << HorseTimes[r] << endl;
    }*/

    double AnnieTime;

    sort(HorseTimes.begin(), HorseTimes.end());

    AnnieTime = HorseTimes[HorseTimes.size()-1];
    double AnnieSpeed = Destinations[i]/AnnieTime;
    std::cout << std::setprecision(9) << std::showpoint << std::fixed;
    cout << "Case #"  << i+1 << ": " << AnnieSpeed << endl;

    /*for(int r = 0; r < HorseSpeeds.size(); r++){//find the slowest horse
      if(SlowestSpeed >= HorseSpeeds[r]){
        SlowestSpeed = HorseSpeeds[r];
        indexofSlowest = r;
      }
    }*/

    //double TimeofSlowest = TimeToDestination(Destinations[i], HorsePositions[indexofSlowest], SlowestSpeed);

    //cout << "Destination: " << Destinations[i] << endl << "Slowest Horse Position: " << HorsePositions[indexofSlowest] << endl << "Index of Slowest: " << indexofSlowest << endl << "Slowest Speed: " << SlowestSpeed << endl << "Time of Slowest: " << TimeofSlowest << endl;










  }



  return 0;
}
