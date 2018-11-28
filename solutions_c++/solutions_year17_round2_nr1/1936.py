#pragma warning(disable:4996)
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <math.h>
#include <climits>
#include <float.h>
using namespace std;

struct HorsesData {
    int ki;
    int si;
    
    HorsesData(int ki, int si)
    {
        this->ki = ki;
        this->si = si;
    }
};

void readHorsesData(vector<HorsesData>& horsesData, int numHorses)
{
    horsesData.clear();
    
    int ki, si;
    
    for (int i = 0 ; i < numHorses ; ++i)
    {
        cin >> ki >> si;
        
        HorsesData data(ki, si);
        
        horsesData.push_back(data);
    }
}

double calculateMaxTime(vector<HorsesData>& horsesData, int D)
{
    double maxTime = -DBL_MAX;
    
    for (int i = 0 ; i < (int)horsesData.size() ; ++i)
    {
        double currentTime = (double)(D - horsesData[i].ki) / (double)horsesData[i].si;
        
        maxTime = max(maxTime, currentTime);
    }
    
    return maxTime;
}




int main() {
    freopen("A-large.in", "r", stdin);
    
    int T;
    int D, N;
    vector<HorsesData> horsesData;
    
    cin >> T;
    
    for (int iteration = 1 ; iteration <= T ; ++iteration)
    {
        cin >> D >> N;
        
        readHorsesData(horsesData, N);
        
        double maxTime = calculateMaxTime(horsesData, D);
        
        double velocity = (double)D / maxTime;
        std::cout << std::fixed;
    
        cout.precision(6);
        cout << "Case #" << iteration << ": " << velocity << endl;
    }
    
    
    return 0;
}
