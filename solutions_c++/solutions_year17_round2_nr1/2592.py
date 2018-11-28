#include <algorithm>
#include <string>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stdio.h>

//#include <bits/stdc++.h>


using namespace std;

//#define DEBUG 1

#ifdef DEBUG
#define D(x) x
#else
#define D(x)
#endif


//char arr[777][777];

int main(){
	int testCases;
    cin >> testCases;

    for(int t = 1 ; t <= testCases ; t++){

        int END;
        int numHorses;
        cin >> END;
        cin >> numHorses;

        float maxTime = -1;
        vector<float> timeToEnd;
        for(int i = 0 ; i < numHorses ; i++){
            int start, speed;
            cin >> start;
            cin >> speed;

            int toEnd = END - start;
            float timeToEnd = (toEnd * 1.0) / speed;
            maxTime = max(maxTime, timeToEnd);
        }
        float ans = (END * 1.0) / maxTime;
        printf("Case #%d: %f\n", t, ans);
    }

}

