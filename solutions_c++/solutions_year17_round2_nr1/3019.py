#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

int main(){
    int testCaseNumber;
    cin>>testCaseNumber;
    for(int tc = 0; tc < testCaseNumber; tc++){
        int horsesNumber;
        double distance;
        //float startPoint[10005], speed[10005];

        cin>>distance>>horsesNumber;
        double longestTime = 0;
        for (int i = 0; i < horsesNumber; i++){
            //cin>>startPoint[i]>>speed[i];
            double st, sp;
            cin>>st>>sp;
            longestTime = max(longestTime, (distance - st)/ sp);
        }
        printf("Case #%d: %lf\n", tc+1, distance/longestTime);
        //cout<<"Case #"<<tc<<": "<<distance/longestTime<<endl;
    }
}
