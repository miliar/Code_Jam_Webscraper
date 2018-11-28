#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <vector>

using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, n, k;

  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  //cout << t << endl;
  for (int j = 1; j <= t; ++j) {
    cin >> n >> k;  // read n and then m.

    // create status array for toilet
    // left and right are true, false in the middle
    vector<bool> toiletStatus;
    toiletStatus.push_back(true);
    for (int i = 0; i < n; i++){
      toiletStatus.push_back(false);
    }
    toiletStatus.push_back(true);

    int finalBiggestMinDistance;
    int finalBiggestMaxDistance;

    //cout << "Created init" << endl;
    // for each person in the queue...
    for (int i = 0; i < k; i++){

      int biggestMinDistanceIndex = 0;
      int biggestMinDistance = -1;
      bool ignoreBiggestMinDistance = false;

      int biggestMaxDistanceIndex = 0;
      int biggestMaxDistance = -1;
      bool ignoreBiggestMaxDistance = false;

      int leftMostBiggestMaxDistanceIndex = -1;

      vector<int> maxDistance;
      vector<int> minDistance;

      //cout << "Person " << i << endl;

      // iterate over the toilets
      vector<int> usefulToiletIndex;

      for (int z = 0; z < n; z++){


        int currIndex = z + 1;

        if (!toiletStatus[currIndex]){
          //cout << "Stall: " << currIndex << endl;

          // this can be optimised, redundant caluclation
          int leftMostClosed = 0;
          for (int a = currIndex - 1; a >= 0; a--){
            if (toiletStatus[a]){
              leftMostClosed = a;
              break;
            }
          }

          int rightMostClosed = 0;
          for (int a = currIndex + 1; a < toiletStatus.size(); a++){
            if (toiletStatus[a]){
              rightMostClosed = a;
              break;
            }
          }

          //cout << "Rightmost: " << rightMostClosed << endl;
          // Ls and Rs
          int ls = currIndex - leftMostClosed - 1;
          int rs = rightMostClosed - currIndex - 1;

          //cout << "ls: " << ls << endl;
          //cout << "rs: " << rs << endl;
          int minValue = min(ls, rs);
          int maxValue = max(ls, rs);

          if (minValue > biggestMinDistance){
            biggestMinDistance = minValue;
            biggestMinDistanceIndex = currIndex;
            ignoreBiggestMinDistance = false;
            usefulToiletIndex.clear();
            usefulToiletIndex.push_back(currIndex);

          } else if (minValue == biggestMinDistance){
            ignoreBiggestMinDistance = true;
            usefulToiletIndex.push_back(currIndex);
          }



          //cout << "biggestMin: " << biggestMinDistance << endl;
          //cout << "biggestMax: " << biggestMaxDistance << endl;

          //maxDistance.push(maxValue);
          //minDistance.push(minValue);
        }

      }

      int stallToUse;
      //cout << "toilet vector size: " << usefulToiletIndex.size() << endl;
      if (usefulToiletIndex.size() == 1){

        stallToUse = usefulToiletIndex[0];
      } else {

        // check for biggestMaxDistance
        for (int z = 0; z < usefulToiletIndex.size(); z++){

          int currIndex = usefulToiletIndex[z];
          if (!toiletStatus[currIndex]){
            //cout << "Stall: " << currIndex << endl;

            // this can be optimised, redundant caluclation
            int leftMostClosed = 0;
            for (int a = currIndex - 1; a >= 0; a--){
              if (toiletStatus[a]){
                leftMostClosed = a;
                break;
              }
            }

            int rightMostClosed = 0;
            for (int a = currIndex + 1; a < toiletStatus.size(); a++){
              if (toiletStatus[a]){
                rightMostClosed = a;
                break;
              }
            }

            //cout << "Rightmost: " << rightMostClosed << endl;
            // Ls and Rs
            int ls = currIndex - leftMostClosed - 1;
            int rs = rightMostClosed - currIndex - 1;

          //  cout << "ls: " << ls << endl;
          //  cout << "rs: " << rs << endl;
            int minValue = min(ls, rs);
            int maxValue = max(ls, rs);



            if (maxValue > biggestMaxDistance){
              biggestMaxDistance = maxValue;
              biggestMaxDistanceIndex = currIndex;
              ignoreBiggestMaxDistance = false;

              leftMostBiggestMaxDistanceIndex = currIndex;
            } else if (maxValue == biggestMaxDistance){

              ignoreBiggestMaxDistance = true;

            }
          }

        }

        if (!ignoreBiggestMaxDistance){
          stallToUse = biggestMaxDistance;
        } else {
          stallToUse = leftMostBiggestMaxDistanceIndex;
        }

      }


      //cout << "Finished stall check" << endl;


      //cout << "Setting stall: " << stallToUse << endl;
      toiletStatus[stallToUse] = true;


      // check left and right for this stall
      int leftMostClosed = 0;
      for (int a = stallToUse - 1; a >= 0; a--){
        if (toiletStatus[a]){
          leftMostClosed = a;
          break;
        }
      }

      int rightMostClosed = 0;
      for (int a = stallToUse + 1; a < toiletStatus.size(); a++){
        if (toiletStatus[a]){
          rightMostClosed = a;
          break;
        }
      }

      // Ls and Rs
      int ls = stallToUse - leftMostClosed - 1;
      int rs = rightMostClosed - stallToUse - 1;

      finalBiggestMinDistance = min(ls, rs);
      finalBiggestMaxDistance = max(ls, rs);




    }


    cout << "Case #" << j << ": " << finalBiggestMaxDistance << " " << finalBiggestMinDistance << endl;


  }

  return 0;

}
